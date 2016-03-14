#coding=utf8
import sys
import re
import string
import time
import datetime
'''By 凌晨G度'''
''' 亿级手机相关密码泄露事件，定向威胁分析--文本查看 '''

def search():
        File='filename.txt'
        f=open(File,'r')
        lines = f.readlines(10000) #大批量会内存限制，仅读取前10000行
        for line in lines[1:100]: #仅输出展示1-100行数据
            print line
        f.close()

if __name__=='__main__':
        search()
        
    
