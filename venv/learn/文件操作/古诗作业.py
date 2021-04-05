# -*- coding: UTF-8 -*-

#将古诗写进文件gushi.txt里面
#生成文件
#每一句写一行
'''
def writeNewfile(a):
    try:
        try:
            fileName1 = input('请输入指定文件名')
            for i in a:

                file1 = open('%s.txt' %fileName1, 'a' ,encoding='utf-8')
                i = i + '\n'
                file1.write(i)
                print(i)
                file1.close()
        finally:
            file1.close()
    except Exception as eror1:
        print('输入出错')
        print(eror1)
'''




def readNewfile(a):
    try:
        #file1 = open('a','r')
        #fileName2 = input('请输入指定文件名')
        with open('%s'%a, 'r', encoding='utf-8') as file:
            fileresult = file.read()
            print(fileresult)
            print('拷贝完成')
    except Exception as eror2:
        print('拷贝出错')
        print(eror2)






gushi = ['白日依山尽' , '黄河入海流' , '欲穷千里目' , '更上一层楼']


#getNewfile(gushi)
#将gushi.txt文件的内容读出来
#每行都
#


readNewfile('123.txt')