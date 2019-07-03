#!/usr/bin/env python
#-*-coding:utf-8-*-

import time;
import sys;
import datetime;
import os;

print("=-=- syc learning python -=-=");

for i in range(5):
    time.sleep(5);
    
    os.system("echo "+i+">>testlog");
    os.system("date>>testlog");
