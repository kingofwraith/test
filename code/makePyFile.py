#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,os

logfile="/root/logs/makePyFile.log";
fileName="defaultsyc";
pathin=None;

if len(sys.argv)>1:
    fileName=sys.argv[1];
'''
if len(sys.argv)>2:
    pathin=sys.argv[2];
    pathin=pathin+"/";
if len(sys.argv)>3:
    logfile=sys.argv[3];
'''

#write logfile
os.system("echo '=========='>>"+logfile);
os.system("date>>"+logfile);
log=open(logfile,"a");
log.write("FROM::: makePyFile.py \nSTR:::: make file:"+fileName+".py \n");
log.close();

# the top words in "*.py" file
toplist=["#!/usr/bin/env python\n","#-*-coding:utf-8-*-\n","\n\n\n"];
deflist=["def "+fileName+"():\n","    intmp=None;\n","#"+fileName+"();\n\n\n"];
mainlist=["def main():\n","    #"+fileName+"();\n\n","if __name__=='__main__':\n","    main();\n"];

myfile=None;
if pathin==None:
    myfile=open(fileName+".py","a");
else:
    myfile=open(pathin+fileName+".py","a");

myfile.writelines(toplist);
myfile.writelines(deflist);
myfile.writelines(mainlist);

myfile.close();

os.system("chmod u+x "+fileName+".py");
os.system("echo 'END:::: create "+fileName+".py'>>"+logfile);




