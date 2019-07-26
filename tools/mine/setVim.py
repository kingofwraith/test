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

def setVi():
    os.system("echo 'set number'>>/etc/virc");
    os.system("echo 'set tabstop=4'>>/etc/virc");
    os.system("echo 'set softtabstop=4'>>/etc/virc");
    os.system("echo 'set shiftwidth=4'>>/etc/virc");
    os.system("echo 'set expandtab'>>/etc/virc");
    os.system("echo 'set list'>>/etc/virc");

#setVim();
#setVi();

