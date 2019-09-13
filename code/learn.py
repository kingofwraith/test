#!/usr/bin/env python
#-*-coding:utf-8-*-



def learn_1():
    data = ['syc',1987,11.26,(13,25,303)];
    name,year,day,address = data;
    print('------learn 1------');
    print('元组批量赋值给变量');
    print(name);
    print(year);
    print(day);
    print(address[1]);
    print(address);

def learn_2():
    import re;
    line='ab,cd;  ef,gh;ijk,foo';
    t1=re.split(r'[;,\s]\s*',line);
    print('------learn 2------');
    print(t1);

def learn_3():
    print('------learn 3------');
    print('简单易读的字符切片代码');
    t1='abcdefghijklmnopqrstuvwkyz';
    t2='1234567890';
    ##选择切片位置
    qt1=slice(1,4);
    qt2=slice(0,5);
    print(t1[qt1]);
    print(t2[qt2]);

def main():
    learn_1();
    learn_2();
    learn_3();
    print '------END------';

if __name__=='__main__':
    main();
