#!/usr/bin/env bash
#author: rangapv@yahoo.com
#03-08-25

account1="639266437671"

repocreate() {
echo "Do you want to create a new repo in ecr for lambda , If yes then press 'y' "
read input11

if [[ "$input11" == "y" ]]
then

   echo "Enter the repo name"
   read reponame
   echo "Enter the region where (like  ... us-west-2/us-east-1 )"
   read region21
   echo "Going to create the repo in the region ${region21} with the name ${reponame} in account-id ${account1}"
   repostat1=`aws ecr create-repository --repository-name ${reponame} --region ${region21}`
   repos="$?"
   if [[ "$repos" == "0" ]]
   then
       echo "Repo creation SUCCESSFUL ${repostat1}"
   else
       echo "Repo creation failed..try again"
   fi
else
       echo "Proceeding with rest of the deployment"
fi

}

rolecreate() {
 echo "Input the TRUST policy json file name"
 read trust1
 echo "input the PERMISSSION policy json file name"
 read permin1
 role1=`aws iam create-role  --role-name ${repo}-role1  --assume-role-policy-document file://${trust1}.json`
 role1s="$?"
 if [[ "$role1s" == "0" ]]
 then
    echo "role with name ${repo}-role1 created successfully with TRUST permissions"
    echo "now lets attach the Permission JSON to this Role"
    permrole1=`aws iam put-role-policy --role-name $[repo}-role1 --policy-document file://${permin1}.json --policy-name simple1`
    permrole1s="$?"
    if [[ "$permrole1s" == "0" ]]
    then
        echo "SUCCESSFULLY attached Permision policy to the role ${repo}-role1"
    else
        echo "FAILED to attach Permission policy to the role ${repo}-role1"
    fi
 else
   echo "Role creation failed"
 fi
}

funclambda() {
echo "If you want to create a new Function in command line for Lambda press 'y'"echo "If you want to create a new Function in command line for Lambda press 'y'"
read lambfunc
if [[ "${lambfunc}" == "y" ]]
then
   echo "Enter Name of the Function"
   read funcname
   echo "Enter the architecture (x86_64/amd64)"
   read lambarch
   echo "Enter Description"
   read lambdesc
   echo "Enter time-out value in seconds(60 for 1 minutes and mulptiples of 60..)"
   read lambtime
   echo "Enter the package type (Image/Zip)"
   read lambpack
   lambfunc1=`aws lambda create-function --function-name ${funcname} --architectures ${lambarch} --description {lambdesc} --timeout ${lambtime} --role arn:aws:iam::${account1}:role/${repo}-role1 --package-type ${lambpack} --code "ImageUri=639266437671.dkr.ecr.us-west-2.amazonaws.com/web1:latest"`
   lambfunc1s="$?"
   echo "Trying to create lambda function with name ${funcname}  and architectures ${lambarch} with timeout ${lambtime} of Package type ${lambpack}"
   if [[ "$lambfunc1s" == "0" ]]
   then
       echo "Lambda Function creation SUCCESSFUL ${lambfunc1}"
       funurl=`aws lambda create-function-url-config --function-name ${funcname} --auth-type NONE`
       funurls="$?"
       if [[ "$funurls" == "0" ]]
       then
          url1=`echo "$funurl" | grep "FunctionUrl"`
          echo "Function URL creation is SUCCESS.."
          echo "You can access your function at ${url1}" 
   else
       echo "Lambda Function creation failed..try again"
   fi
else
   exit
fi


}

repocreate

rolecreate

funclambda
