#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,pexpect;

startword=['#','>>>','>','\$'];

# use pexpect to work
def sycGit():
    commd="git push origin master";
    # write work log
    worklog=open("sycGit.log","w");
    # keywords of ssh_key
    key="_rsa";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    #child.timeout=300
    ret=child.expect([pexpect.TIMEOUT,pexpect.EOF,key]);
    if ret==0:
        print ":: ERROR :: TIMEOUT";
    if ret==1:
        print ":: ERROR :: EOF";
    if ret==2:
        #catch the keywords and  send ssh_key
        child.sendline("sycsyc");
        child.logfile=worklog;
    worklog.close();

# use os.system to work
def sycGit2():
    commd="git pull origin master";

sycGit();
