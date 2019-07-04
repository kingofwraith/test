#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,pexpect;


inargv=sys.argv;    #get ip and password from command opition

startword=['#','>>>','>','\$'];
def send_cmd(child,cmd):
    child.sendline(cmd);
    child.expect(startword);
    print child.before;

def connect_ssh(user,host,pwd):
    ssh_key1="want to continue";
    conn='ssh '+user+'@'+host;
    child=pexpect.spawn(conn);
    ret=child.expect([pexpect.TIMEOUT,ssh_key1,'[P|p]assword:']);
    if ret==0:
        print ':::: Error Connecting';
        return;
    if ret==1:
        child.sendline('yes');
        ret=child.expect([pexpect.TIMEOUT,ssh_key1,'[P|p]assword:']);
        if ret==0:
            print ':::: Error Connecting';
            return;
    child.sendline(pwd);
    child.expect(startword);
    return child;


def main():
    host=inargv[1];    #ip
    user='root';
    pwd=inargv[2];    #password
    child=connect_ssh(user,host,pwd);
    send_cmd(child,'ll');
    send_cmd(child,'cd mycode;ll');

if __name__=='__main__':
    main();
