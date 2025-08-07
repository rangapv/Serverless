#!/usr/bin/env bash
#author:rangapv@yahoo.com
#17-04-25

source <(curl -s https://raw.githubusercontent.com/rangapv/Serverless/refs/heads/main/AWS/lambda/Python/stokpoly/pkgchk.sh) > /dev/null 2>&1
source <(curl -s https://raw.githubusercontent.com/rangapv/Serverless/refs/heads/main/AWS/repocreate.sh) > /dev/null 2>&1

tag1="stok1"
region2="us-west-2"
funcname="web2"
account1="639266437671"
repo="web1"
attachRole="web2-role-8jyz9pf3" 

chkifinsta aws docker 

echo "Hope you are Calling this script from the Directory which has the docker build file (dockerfile/Dockerfile)"

echo "The docker build will push the image to the AWS ecr repo ${repo}, if you would like to create a NEW repo press 'y'"
read reponew

if [[ "$reponew" == "y" ]]
then
   repocreate
else
   echo "Proceeding to push the build docker to repo ${repo}"
fi

echo "This build will deploy lambda in the region ${region2} at a Function-named ${funcname} in the account# ${account1}"
echo "if you need to deploy at a different account press y"
read input1 

if [[ "$input1" == "y" ]] 
then
       echo "Enter the region where"
       read region2
       echo "Enter the account # to deploy this"
       read account1
       echo "Enter the tag details for the build"
       read tag1
       echo "Enter the repo name in AWS"
       read repo
else
       echo "proceeding with build..."
fi

#bld1=`docker build -t ${tag1} .`
bld1=`docker build --platform linux/amd64 --provenance=false -t ${tag1} .` 
bld1s="$?"

while :
do
        lc1=`docker images ${tag1}:latest | sed -n '$='`
        #lc1=`docker images ${tag1}:latest | wc -l`
        if [[ "$lc1" != "2" ]]
        then
                echo "inside wait"
                sleep 2
        else
                break
        fi
done

if  [[ "$bld1s" == "0" ]]
then
bld2=`docker tag ${tag1}:latest ${account1}.dkr.ecr.${region2}.amazonaws.com/${repo}:latest`
bld2s="$?"
        if [[ "$bld2s" == "0" ]]
        then
		bldauth=`aws ecr get-login-password --region ${region2} | docker login --username AWS --password-stdin ${account1}.dkr.ecr.${region2}.amazonaws.com`
		bldauths="$?"
        	if [[ "$bldauths" == "0" ]]
                then
			echo "aws ecr re-auth passed proceeding "
		else
			echo "aws ecr re-auth failed pls chk ${bldauth}"
			exit
		fi
                bld3=`docker push ${account1}.dkr.ecr.${region2}.amazonaws.com/${repo}:latest`
                bld3s="$?"
                if [[ "$bld3s" == "0" ]] 
                then
                        echo "Build push to ECR passed check the ECR registry or proceed with lambda-update command"
                        
                        echo "Do you want to create a new lambda FUNCTION the current lambda function is set to ${funcname}'
                        read newfunc
                        if [[ "$newfunc" == "y" ]]
                        then
                            funclambda
                        else
                            lamb_update=`aws lambda update-function-code --function-name ${funcname} --image-uri  ${account1}.dkr.ecr.${region2}.amazonaws.com/${repo}:latest`
			    lamups="$?"
                            if [[ "$lamups" == "0" ]]
                            then
                                echo "Lambda update to function is SUCCESS"
                            else
                                echo "lambda update to function FAILED pl chk ${lamb_update}"
                            fi
                        fi
                else
                        echo "Build push to ECR failed pls shk ${bld3}"
                fi
        else
                echo "Build tag to ECR failed pls chk ${bld2}"
        fi
else
        echo "Build failed pls chk ${bld1}"
fi
