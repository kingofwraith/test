#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys,os;

def workForOS():
    intmp=None;
    #os.system("cd /root/mycode/test");
    
    #show pwd
    os.system("pwd");
    print os.getcwd(); # same as before commd
    
    #change DIR
    os.system("cd /root/mycode");# It's not worked
    os.chdir("mycode");
    print os.getcwd();
    
    

def main():
    workForOS();

if __name__=='__main__':
    main();
