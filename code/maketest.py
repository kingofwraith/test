#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,os


fileName=sys.argv[1];

toplist=["#!/usr/bin/env python\r\n","#-*-coding:utf-8-*-\r\n"];

myfile=open(fileName+".py","a");
myfile.writelines(toplist);

myfile.close();

os.system("chmod u+x "+fileName+".py");
