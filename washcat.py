#!/usr/bin/python3
#import requests
import os
import argparse
#import string
import sys
import re

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("jobfile", help="Original Hashcat™ job file containing account names and hashes")
ap.add_argument("potfile", help="Original Hashcat™ pot file containing hashes and cleartext passwords")
ap.add_argument("-o", "--output", required=False,
        help="Name of the output file which should contain the correlated names and cleartext passwords (Default: stdout)")
ap.add_argument("--ntlmv2", required=False,
       help="Switch: Set job file hash type as NTLMv2 (Default: NTLM)", action='store_true')
#ap.add_argument("--ntlmv1", required=False,
#       help="Switch: Set job file hash type as NTLMv1 (Default: NTLM)", action='store_true')
args = vars(ap.parse_args())

potFile = args["potfile"]
potString = ""
jobFile = args["jobfile"]
jobString = ""

#CURATING THE ORIGINAL JOBFILE TO KEEP ONLY ACCOUNT NAMES AND HASHES
if (args["ntlmv2"] == True):
    #NTLMv2 jobfile strings
    file = open(potFile, "r") 
    for line in file: 
        if re.match(r'NONE:', line) is None:
            jobString = jobString + re.sub(r'([^:]*):.*:(.*):.*:.*:.*:(.*)', r'\1:\2:\3', line) + '\n'
            print(jobString)
    file.close()
else:
    #NTLMv1 jobfile strings
#    else if (args["ntlmv1"] == True):
#        
    #NTLM jobfile strings
    file = open(jobFile, "r") 
    for line in file: 
        if re.match(r'NONE:', line) is None:
            jobString = jobString + re.sub(r'([^:]*):.*:(.*):::', r'\2:\1', line) + '\n'
    file.close()

    file = open("job.out", "w")
    file.write(jobString);
    file.close()

    os.system("sort job.out > job-sorted.out")
    os.system("rm job.out")
    os.system("sort "+potFile+" > pot-sorted.out")
    if args["output"] is None:
        os.system("join -t: job-sorted.out pot-sorted.out")
    else:
        os.system("join -t: job-sorted.out pot-sorted.out > "+args["output"])
    os.system("rm job-sorted.out; rm pot-sorted.out")
