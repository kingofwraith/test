#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys;

argv_setvim=sys.argv;
#print(argv_setvim[1]);

# set vim in Centos 7
def setVim():
    os.system("echo 'set number'>>/etc/vimrc");
    os.system("echo 'set tabstop=4'>>/etc/vimrc");
    os.system("echo 'set softtabstop=4'>>/etc/vimrc");
    os.system("echo 'set shiftwidth=4'>>/etc/vimrc");
    os.system("echo 'set expandtab'>>/etc/vimrc");
    os.system("echo 'set list'>>/etc/vimrc");

    os.system("echo 'set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936'>>/etc/vimrc");
    os.system("echo 'set termencoding=utf-8'>>/etc/vimrc");
    os.system("echo 'set encoding=utf-8'>>/etc/vimrc");

def setVi():
    os.system("echo 'set number'>>/etc/virc");
    os.system("echo 'set tabstop=4'>>/etc/virc");
    os.system("echo 'set softtabstop=4'>>/etc/virc");
    os.system("echo 'set shiftwidth=4'>>/etc/virc");
    os.system("echo 'set expandtab'>>/etc/virc");
    os.system("echo 'set list'>>/etc/virc");

    os.system("echo 'set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936'>>/etc/virc");
    os.system("echo 'set termencoding=utf-8'>>/etc/virc");
    os.system("echo 'set encoding=utf-8'>>/etc/virc");

def main():
    tOption=None;
    if len(sys.argv)>1:
        tOption=sys.argv[1];
    else:
        print "No option here";

    if tOption=='vim':
        setVim();

    if tOption=='vi':
        setVi();


if __name__=='__main__':
    main();
