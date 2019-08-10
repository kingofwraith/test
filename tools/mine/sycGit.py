#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,pexpect;

startword=['#','>>>','>','\$'];

# use pexpect to work
# git pull
def sycGit():
    commd="git pull origin master";
    
    # write work log
    logfilename="/root/logs/sycGit.log";
    worklog=open(logfilename,"a");
    #check time to logfile
    os.system("echo '----------'>>"+logfilename+";date>>"+logfilename+";echo '------'>>"+logfilename);
    
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
        print ":: WORKED :: PWD OK";
    worklog.close();

# git push;
def sycGit2():
    # write work log
    logfilename="/root/logs/sycGit.log";
    worklog=open(logfilename,"a");
    #check time to logfile
    os.system("echo '----------'>>"+logfilename+";date>>"+logfilename+";echo '------'>>"+logfilename);
    
    os.system("git commit>>"+logfilename);
    os.system('git add -A');
    os.system("git commit -m 'auto upload by python'>>"+logfilename);
    print ":: WORKED :: 'git add + commit'";
    
    #push to master
    commd="git push origin master";
    child=pexpect.spawn(commd);
    child.logfile=worklog;
    
    child.timeout=300;
    ret=child.expect([pexpect.TIMEOUT,'_rsa']);
    if ret==0:
        print ":: ERROR :: ssh_key TIMEOUT";
    if ret==1:
        child.sendline("sycsyc");
        child.logfile=worklog;
        print ":: WORKED :: 'git ssh pwd'";
        ret1=child.expect([pexpect.TIMEOUT,'-> master','Everything']);
        if ret1==0:
            print ":: ERROR :: push TIMEOUT";
        if ret1==1:
            print ":: WORKED :: 'git push ok'";
        if ret1==2:
            print ":: WORKED :: nothing to upload";
    worklog.close();


def main():
    tOption=None;
    if len(sys.argv)>1:
        tOption=sys.argv[1];
    else:
        print 'No option here';
    
    if tOption=='pull':
        sycGit();
    
    if tOption=='push':
        sycGit2();

if __name__=='__main__':
    main();
