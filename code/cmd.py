#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys;

logfile="work.log"
os.system("date>>"+logfile+";echo 'FROM: cmd.py'>>"+logfile);

if len(sys.argv)>1:
	os.system("echo 'COMMAND: '"+sys.argv[1]+">>"+logfile);
    os.system(sys.argv[1]);
else:
	os.system("echo 'ERROR: no command'>>"+logfile);
    
