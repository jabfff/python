####异常捕获
'''

print('------test----1-----')

f = open('123.txt','r')

print('------test----2-----')

'''


'''
try:
    print('------test----1-----')

    f = open('123.txt', 'r')         #文件没找到，属于IO异常（出入输出异常）

    print('------test----2-----')    #捕获异常后，执行代码

except IOError:
    pass
'''


'''
try:
    print(num)
#except  IOError:                 #异常类型想要被捕获到，需要一致
except NameError:              
    print('产生错误了')
'''

'''
try:
    print('------test----1-----')

    f = open('test1.txt', 'r')  # 文件没找到，属于IO异常（出入输出异常）

    print('------test----2-----')  # 捕获异常后，执行代码
    print(num)
#except  IOError:                 #异常类型想要被捕获到，需要一致
except(NameError,IOError):         #将可能产生的所有异常类型，都放到括号中
    print('产生错误了')
    
'''



'''
#获取错误描述
try:
    print('------test----1-----')

    f = open('123.txt', 'r')  # 文件没找到，属于IO异常（出入输出异常）

    print('------test----2-----')  # 捕获异常后，执行代码
    print(num)
#except  IOError:                 #异常类型想要被捕获到，需要一致
except(NameError,IOError) as result:         #将可能产生的所有异常类型，都放到括号中
    print('产生错误了')
    print(result)
'''



'''
#捕获所有异常
try:
    print('------test----1-----')

    f = open('123.txt', 'r')

    print('------test----2-----')
    print(num)
#except  IOError:
except Exception as result:         #Exception包含所有异常
    print('产生错误了')
   print(result)
'''
import time

#try   ....finally  和嵌套
try:
    f = open('test1.txt','r')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('关闭文件')


except Exception as result:
    print(result)
    print('出现问题')
'''finally:
    f.close()
    print('文件关闭')
'''






