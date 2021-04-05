"""列表"""
"""
mylist = ['a' , 'b' , 'c' , 'a' , 'b']


print(mylist.index('a',1,4))   #找到指定的元素，并返回下标( 范围 1<= x  <4)


print(mylist.count('c'))   #统计某个元素


print(mylist)
mylist.reverse     #反转
print(mylist)
mylist.sort（）     #排序
mylist.sort(reverse=True)  #降序

"""


#################################################
###嵌套



#schoolNmae = [[],[],[]]    #又3个元素为空的列表，每个元素都是空列表

#schoolNmae = [['北京大学' ,'清华大学'] , ['南开大学' , '天津大学' , '天津师范大学' ] , ['山东大学']]


import random


offices = [[] , [] , []]
names = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print('办公室%d的人数为：%d'%(i,len(office)))
    i += 1
    for name in office:
        print('%s'%name , end='\t')
    print('\n')
    print('-' * 20)

