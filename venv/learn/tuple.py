tup1 = (12,23,34)    #tuple不允许修改
tup2 = ('abe' , 'xyz')
tup = tup1 +tup2
print(tup)   #看起来增加了，实际市连接起来，放到一个新内存里面。

del tup1         #删除整个元组

