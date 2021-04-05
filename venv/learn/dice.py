

"""
#字典访问

print(info['name'])
print(info['gender'])        #没有包含的直接访问会报错


print(info.get('gender'))     #使用GET方法在没有值的情况下默认返回 None

print(info.get('gender' , 'm'))    #没有找到的时候可以设定默认值


#增

info = {'name' : '周杰伦' , 'age' : '35'}

newID = input('请输入学号')
info['id'] = newID

print(info['id'])        #增加一对键值对
print(info)

#del info['name']       #删除一对键值对

#info.clear()            #将整个字典清空



#改
#info['age'] = 20
#print(info)



#查
for key,value in info.items():
    print('key=%s , value=%s'%(key,value))
"""


mylist = [['a' , '1'] ,
          ['b' , '2'] ,
          ['c' , '3'] ,
          ['d' , '4']]

for i,x in enumerate(mylist):
    for j,y in enumerate(x):
        print(j+1,y)