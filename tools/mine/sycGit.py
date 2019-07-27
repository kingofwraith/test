#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,pexpect;

startword=['#','>>>','>','\$'];

# use pexpect to work
def sycGit():
    commd="git push origin master";
    # write work log
    worklog=open("sycGit.log","a");
    # keywords of ssh_key
    key="_rsa";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    #child.timeout=300;
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


def sycGit2():
    # write work log
    worklog=open("sycGit.log","a");
    
    commd="git add *";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    print ":: WORKED :: 'git add *' ";
    
    commd="git commit -m 'auto upload by python'";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    print ":: WORKED :: 'git commit'";
    
    commd="git push origin master";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    
    child.timeout=300;
    ret=child.expect([pexpect.TIMEOUT,'_rsa']);
    if ret==0:
        print ":: ERROR :: TIMEOUT";
    if ret==1:
        child.sendline("sycsyc");
        child.logfile=worklog;
        print ":: WORKED :: 'git ssh pwd'";
        ret1=child.expect([pexpect.TIMEOUT,'completed','Everything']);
        if ret1==0:
            print ":: ERROR :: TIMEOUT";
        if ret1==1:
            print ":: WORKED :: 'git push ok'";
        if ret1==2:
            print ":: WORKED :: nothing to upload";
    worklog.close();


def main():
    #sycGit();
    sycGit2();

if __name__=='__main__':
    main();
