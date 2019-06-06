# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:47:56 2018

@author: HASEE
"""
f = open('a.txt', encoding='utf-8')
str_all=[]
for line in f:
    arr= line.split('\t')
    if int(arr[2].strip()) <= 1:
        str_all.append(arr[0].strip() + "\t" + arr[1].strip() + "\t" +'0')
    else:
        str_all.append(arr[0].strip() + "\t" + arr[1].strip() + "\t" +'1')
f.close()
f = open("out.txt", "w")
for str in str_all:
	print(str, file=f)
	
f.close()