#coding=utf8
import sys
import re
import string
import time
import datetime
''' 定向威胁分析 '''

def search(File):
        
        f=open(File,'r')
        f1=open(r'result.txt','a')
        num=0
        success_num=0  #计数
        flag=0  #标记
        print '>>>Start search file:'+File+'...'
        f1.write('>>>文件标记:'+File)
        while 1:
                lines = f.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        num=num+1
                        linex=re.search(r'(18812341234)|(13512341234)|(18612341234)|(15612341234)|(18712341234)|\
                                        (18912341234)|(15812341234)',line) #被搜查号码
                        if linex:
                            f1.write('    发现目标行:'+line)
                            print '发现目标行:'+line
                            success_num=success_num+1 #标记成功的个数
                        else:
                            continue
                        if success_num==7:#被搜查号码个数
                                flag=1
                if flag==1:#标记，如果全部找出，直接结束
                    break
        f.close()
        f1.write('>>>时间标记:%s \n\n'% datetime.datetime.now())
        f1.close()

        print '>>>报告主人，该文件全部搜查完毕!!总共搜索行数：'+str(num)+',请检查result.txt \n<<<End search file：'+File+' \n'


if __name__=='__main__':
        start=time.clock() #The start time
        file=['test.txt','test2.txt']######这里是扫描的txt数据文件，是list数组形式
        for i in file:
                search(i)
        end=time.clock() #The end time
        i = datetime.datetime.now()
        print "###########程序总耗时 : %.03f seconds" %(end-start)
        print "###########当前的日期和时间是 %s" % i
        
        
    
