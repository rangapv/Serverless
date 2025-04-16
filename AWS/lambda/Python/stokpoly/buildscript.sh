#!/usr/bin/env bash
#author:rangapv@yahoo.com
#16-04-25


tag1="stok1"

bld1=`docker build -t ${tag1} .`
bld1s="$?"
if  ( $bld1s == "0" )
then
bld2=`docker tag ${tag1}:latest 988002206709.dkr.ecr.us-east-2.amazonaws.com/rangapv:latest`
bld2s="$?"
	if ( $bld2s == "0" )
	then
		bld3=`docker push 988002206709.dkr.ecr.us-east-2.amazonaws.com/rangapv:latest`
		bld3s="$?"
		if ( $bld3s == "0" )
		then
			echo "Build push to ECR passed check the ECR registry or proceed with lambda-update command"
			lamb_update=`aws lambda update-function-code --function-name stocks --image-uri $(aws lambda get-function --function-name stocks | grep \"ImageUri\" | awk '{split($0,a," "); print a[2]}' | sed 's/"//g' | sed 's/,//')`
			lamups="$?"
			if ( $lamups == "0" )
			then
				echo "Lambda update to function is SUCCESS"
			else
				echo "lambda update to function FAILED pl chk ${lamb_update}"
			fi
		else
			echo "Build push to ECR faile pl shk ${bld3s}"
		fi
	else
		echo "Build tag to ECR failed pls chk ${bld2}"
	fi

else
	echo "Build failed pls chk ${bld1}"
fi
