import os
import subprocess
import sys

def handler(event, context):
    r1 = hello()
    r2 = imagels()
    return r2
def hello():
    return "Hello World"
def imagels():
    t1 = subprocess.run("ls -la", capture_output=True, shell=True, text=True, check=True)
    imgtlen = t1.stdout
    #print(contlen)
    len1 = len(imgtlen.splitlines())
    #print("**********************")
    #print(f'total images are {len1-1}')
    return(f'total files in the container running are {len1-1} and the list is \n {t1.stdout}')
