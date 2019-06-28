import time;
import datetime;
import os;

print("=-=- syc learning python -=-=");

while True:
    t1=input("Please write something:(take 'exit'or'logout' to leave)\n>>> ");
    if t1=="exit" or t1=="logout":
        break;
    print("::: "+t1);

print("\n:::: [END]");


#测试控制命令行
while True:
    t1= input("测试一行命令: \n>>>");
    if t1=="exit" or t1=="logout":
        break;
    print(os.system(t1));
print("\n:::: [END]");

