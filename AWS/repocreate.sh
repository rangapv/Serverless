#!/usr/bin/env bash
#author: rangapv@yahoo.com
#03-08-25

repocreate() {

echo "Do you want to create a new repo in ecr for lambda , If yes then press 'y' "
read input11

if [[ "$input11" == "y" ]]
then
   echo "Enter the new repo name"
   read reponame
   echo "Enter the region where you would like to create it (like us-west-2/us-east-1/... )"
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
 echo "Do you want to create a NEW Role for your FUNCTION ?"
 echo "If yes press 'y' "
 read roleres
 if  [[ "$roleres" == "y" ]]
 then
 echo "Now we are going to create a Role with Trust and Permission policy attached to it for our Lambda FUNCTION"
 echo "Input the TRUST policy json file name"
 read trust1
 echo "input the PERMISSSION policy json file name"
 read permin1
 echo "The format for naming will be repoName-rolesubscript !"
 echo "Enter the repo name under which this Role will be Active(hint:your ECR repo Name that you may have created earlier/one which exists)"
 read repoName
 echo "Enter the role subscript name(hint:it can be anything so that you distinguish on a First glance..)"
 read rolesubscript
 echo "Going to create a New ROLE named ${repoName}-${rolesubscript} with TRUST policy in file ${trust1} and Permission policy in file ${permin1}"
 role1=`aws iam create-role --role-name ${repoName}-${rolesubscript} --assume-role-policy-document file://${trust1}.json`
 role1s="$?"
 if [[ "$role1s" == "0" ]]
 then
    echo "role with name ${repoName}-${rolesubscript} created successfully with TRUST policy"
    echo "now lets attach the Permission JSON to this Role ${repoName}-${rolesubscript}"
    echo "PERMISSION policy are named you give an arbitary name (ex:simple1/simple23/...)"
    read perpolname
    permrole1=`aws iam put-role-policy --role-name ${repoName}-${rolesubscript} --policy-document file://${permin1}.json --policy-name ${perpolname}`
    permrole1s="$?"
    if [[ "$permrole1s" == "0" ]]
    then
        echo "SUCCESSFULLY attached Permision policy to the role ${repoName}-${rolesubscript}"
    else
        echo "FAILED to attach Permission policy to the role ${repoName}-${rolesubscript}"
    fi
 else
   echo "Role creation failed for the role named ${repoName}-${rolesubscript} check logs..."
 fi
 else
  echo "No New Role requested by the USER"
 fi
}

funclambda() {
echo "If you want to create a new Function in command line for Lambda press 'y'"
#echo "If you want to create a new Function in command line for Lambda press 'y'"
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
   echo "Enter the Role that this lambda function will ASSUME . currently it is set to ${repoName}-${rolesubscript}, press 'y' to CHANGE it !"
   read rolechange 
   if [[ "${rolechange}" == "y" ]]
   then
      echo "Enter the NEW Role name to be ATTACHED to the lambda FUNCTION"
      read  attachRole
   else
      attachRole="${repoName}-${rolesubscript}"
   fi
   if [[ ! -z "${attachRole}" ]]
   then
   echo "Trying to create lambda function with name ${funcname}  and architectures ${lambarch} with timeout ${lambtime} of Package type ${lambpack}"
   lambfunc1=`aws lambda create-function --function-name ${funcname} --architectures ${lambarch} --description {lambdesc} --timeout ${lambtime} --role arn:aws:iam::${account1}:role/${attachRole} --package-type ${lambpack} --code "ImageUri=${account1}.dkr.ecr.${region21}.amazonaws.com/${repoName}:latest"`
   lambfunc1s="$?"
   if [[ "${lambfunc1s}" == "0" ]]
   then
       echo "Lambda Function creation SUCCESSFUL ${lambfunc1}"
       funurl=`aws lambda create-function-url-config --function-name "${funcname}" --auth-type NONE`
       funurls="$?"
       if [[ "${funurls}" == "0" ]]
       then
          url1="echo ${funurl} | grep FunctionUrl"
          echo "Function URL creation is SUCCESS.."
          echo "You can access your function at ${url1}" 
       else
         echo "Function URL (HTTPS-endpoint) creation failed.."
       fi
   else
       echo "Lambda Function creation failed..try again"
   fi
   else
      echo "No VALID role name mentioned hence exiting"
   fi      
else
   exit
fi
}

#The function in this script gets called by other Scripts at runtime on user's Discretion!
