""""#函数定义
def printinfo():
    print('-----------------')
    print('******人生苦短，我用PYthon******')
    print('-----------------')

#函数调用
printinfo()
"""


#带参数的函数
#带返回值

"""
def add2Num(a,b):
    #c = a + b      ####带参数
    #print(c)       ####带参数

    return a + b    ####带返回值


#add2Num(11,22)
result = add2Num(11,22)
print(result)
"""

#返回多个函数
def divid(a,b):
    shang = a // b
    yushu = a % b
    return shang,yushu          #多个返回值用 , 分割

sh,yu = divid(5,2)
print('商： %d , 余数： %d'%(sh,yu))