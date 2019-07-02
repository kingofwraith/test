#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,os

logfile="work.log";
fileName="default";

if len(sys.argv)>1:
    fileName=sys.argv[1];
if len(sys.argv)>2:
    logfile=sys.argv[2];


#write logfile
os.system("echo '=========='>>"+logfile);
os.system("date>>"+logfile);
log=open(logfile,"a");
log.write("FROM::: makePyFile.py \r\nSTR:::: make file:"+fileName+".py \r\n");
log.close();

# the top words in "*.py" file
toplist=["#!/usr/bin/env python\r\n","#-*-coding:utf-8-*-\r\n"];

myfile=open(fileName+".py","a");
myfile.writelines(toplist);
myfile.close();

os.system("chmod u+x "+fileName+".py");
os.system("echo 'END:::: create "+fileName+".py'>>"+logfile);




