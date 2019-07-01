#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys;

logfile="work.log"
os.system("date>>"+logfile+";echo 'FROM: cmd.py'>>"+logfile);

if len(sys.argv)>1:
	os.system("echo 'COMMAND: '"+sys.argv[1]+">>"+logfile);
	command=sys.argv[1]+" \& 1>>"+logfile+" 2>\&1";
    print(command)
else:
	os.system("echo 'ERROR: no commands'>>"+logfile);
    
