

'''
f = open('test.txt','w')             #打开文件，没有这个文件就新建。有这个文件就重置这个文件
f.write('This is new shit!')            #将字符串放入文件里面

f.close()         #关闭文件
'''

''' #read方法，读取指定字符，开始市定位在文件头部，每次执行都向后移动。
f = open('test.txt','r')         #读取文件，需要关闭，不然后续无法使用这个文件
content = f.read(6)              #读取前6个字符
print(content)
content = f.read(6)
print(content)
f.close()
'''

'''
f = open('test.txt','r')         #####一次性读取文件为列表，每行一个字符串元素
content = f.readlines()
#print(content)
i = 1
for tmp in content:
    print('%d:%s'%(i,tmp))
    i +=1
f.close()
'''
'''
f = open('test.txt','r')         #####一次性读取文件为列表，每行一个字符串元素
content = f.readline()
print('1:%s'%content)
content = f.readline()
print('2:%s'%content)
'''


import os


os.rename('test.txt','test1.txt')