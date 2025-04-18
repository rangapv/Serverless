#!/usr/bin/env bash
#author:rangapv@yahoo.com
#17-04-25

source <(curl -s https://raw.githubusercontent.com/rangapv/Serverless/refs/heads/main/AWS/lambda/Python/stokpoly/pkgchk.sh) > /dev/null 2>&1

tag1="stok1"
region2="us-west-2"
funcname="web2"
account1="639266437671"
repo="web1"

chkifinsta aws docker 

echo "This build will deploy lambda in the region ${region2} at a Function-named ${funcname} in the account# ${account1}"
echo "if you need to deploy at a different account press y"
read input1

if ( "$input1" == "y" )
then
       echo "Enter the region where"
       input region2
       echo "Enter the account # to deploy this"
       input account1
       echo "Enter the function name wheret he image needs to be deployed as lambda code"
       input funcname
       echo "Enter the tag details for the build"
       input tag1
       echo "Enter the repo name in AWS"
       input repo
else
       echo "proceeding with build..."
fi


bld1=`docker build -t ${tag1} .`
bld1s="$?"


tag1="stok1"

while :
do
        lc1=`docker images ${tag1}:latest | wc -l`
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
                bld3=`docker push ${account1}.dkr.ecr.${region2}.amazonaws.com/${repo}:latest`
                bld3s="$?"
                if [[ "$bld3s" == "0" ]] 
                then
                        echo "Build push to ECR passed check the ECR registry or proceed with lambda-update command"
                        lamb_update=`aws lambda update-function-code --function-name ${funcname} --image-uri  ${account1}.dkr.ecr.${region2}.amazonaws.com/${repo}:latest`
			lamups="$?"
                        if [[ "$lamups" == "0" ]]
                        then
                                echo "Lambda update to function is SUCCESS"
                        else
                                echo "lambda update to function FAILED pl chk ${lamb_update}"
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
