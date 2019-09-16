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
    print('复合符号进行分割');
    print(t1);

def learn_3():
    t1='abcdefghijklmnopqrstuvwkyz';
    t2='1234567890';
    ##选择切片位置
    qt1=slice(1,4);
    qt2=slice(0,5);
    print('------learn 3------');
    print('简单易读的字符切片代码');
    print(t1[qt1]);
    print(t2[qt2]);

def learn_4():
    from collections import Counter;
    data=['syc','shj','jly','yzw','yzw','syc','jly','zw','zw','yzw','syc','syc','shj','yzw','syc','jly','shj','syc'];
    word_count=Counter(data);
    ## 查找前三频次最高的元素
    top_three=word_count.most_common(3);
    ## 查找某元素的出现次数
    someone=word_count['yzw'];
    print('------learn 4------');
    print('统计元素出现次数');
    print(data);
    print(word_count);
    print(top_three);
    print(someone);

def main():
    learn_1();
    learn_2();
    learn_3();
    learn_4();
    print '------END------';

if __name__=='__main__':
    main();
