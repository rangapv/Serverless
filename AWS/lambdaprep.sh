#!/usr/bin/env bash
#author:rangapv@yahoo.com
#updates:26-07-25

awscli() {
awse1=`which aws`
awse1s="$?"

if [[ (( $awse1s -ne 0 )) ]]
then

awscli1=`curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" >/dev/null 2>&1`

awscli2=`sudo apt install unzip -y >/dev/null 2>&1`

awscli3=`unzip ./awscliv2.zip >/dev/null 2>&1`

awscli4=`sudo ./aws/install >/dev/null 2>&1`
else
	echo "aws cli is installed in this box proceeding with other config "
fi
}

awscli_macOS() {
awsmac3=`which aws`
awsmac3s="$?"
if [[ (( "$awsmac3s" -ne 0 )) ]]
then

awsmac1=`curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"`

awsmac2=`sudo installer -pkg ./AWSCLIV2.pkg -target /`
awsmac2s="$?"

if [[ (( "$awsmac2s" -eq 0 )) ]]
then
   echo "aws is installed in this box and is at location \`which aws\`"
else
  echo "aws install on Mac failed"
fi

else
   echo "aws cli is Installed in $awsmac3"
fi
}

aws_configure() {
echo "enter the aws account access-id "
read accid
echo "enter the aws account secret-id"
read secid

awsconf1=`aws configure set aws_access_key_id ${accid}`
awsconf2=`aws configure set aws_secret_access_key ${secid}` 
awsconf3=`aws configure list`
awsconf3s="$?"

if [[ "$awsconf3s" -eq "0" ]]
then
	echo "aws configure was success"
else
	echo "aws configure DID NOT go through"
fi
	echo "$awsconf3"
}

docker_configure() {
echo "Enter the docker config now..."
echo "ENter the docker Login / username"
read dockname
echo "Enter the docker password"
read dockpwd
dc1=`docker login -u $dockname -p $dockpwd`
dc1s="$?"

if [[ "$dc1s" -eq "0" ]]
then
        echo "Docker login was success"
else
        echo "Docker login DID NOT go through"
fi
	echo "$dc1"
}

ecr_login() {
echo "Now authenticating ecr login..."
echo "Pls enter the AWS region where the lambda needs to run..(like us-west-2/us-east-1....)"
read region1
echo "pls enter the AWS account ID of you aws account"
read awsaccid
ecrl1=`aws ecr get-login-password --region ${region1} | docker login --username AWS --password-stdin ${awsaccid}.dkr.ecr.${region1}.amazonaws.com`
#ecrl2=`aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 639266437671.dkr.ecr.us-west-2.amazonaws.com`
ecrls="$?"
if [[ "$ecrls" -eq "0" ]]
then
        echo "ecr login was success"
else
        echo "ecr login DID NOT go through"
fi
        echo "$ecrl1"
}


mac11=$(sw_vers | grep mac)

if [ -z "$mac11" ]
then
 awscli
else
 awscli_macOS
fi

aws_configure

docker_configure

ecr_login

