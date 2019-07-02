#!usr/bin/env python
#-*-coding:utf-8-*-
import os;
import sys;

myargv=sys.argv;

def cmd():
    logfile="work.log"
    os.system("echo '=========='>>"+logfile);
    os.system("date>>"+logfile+";echo 'FROM: cmd.py'>>"+logfile);

    if len(myargv)>1:
        print(myargv[1])
        os.system("echo 'COMMAND: '>>"+logfile);
        os.system("echo '"+myargv[1]+"'>>"+logfile);

        os.system(myargv[1]);
    else:
        os.system("echo 'ERROR: no command'>>"+logfile);

cmd();
