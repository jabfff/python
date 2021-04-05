

products = [['iphone' , 6888] ,
            ['MacPro' , 14800] ,
            ['小米6' , '2499'] ,
            ['Coffee' , 31] ,
            ['Book' , 60] ,
            ['Nike' , 699]]

print('-' * 6 + '商品列表' + '-' * 6)
for i in products:
    x = products.index(i)
    print('%s  %s   %s '%(x,i[0],i[1]) , )


shoppingcar = []
while True:
    buy = input('请选择你需要的商品序号！！！输入q结束')
    if buy != 'q':
        shoppingcar.append(products[int(buy)])
        print('您的购物车里有%d件商品，具体如下：'%len(shoppingcar))
        print(shoppingcar)
        continue
    else:
        print('您购买了如下商品')
        print('-' * 6 + '购买列表' + '-' * 6)
        print('序号   名称    单价  ')
        price = 0
        for i1 in shoppingcar:
            x1 = shoppingcar.index(i1)
            price = price + int(i1[1])
            print('%s  %s   %s ' % (x1, i1[0], i1[1]), )
        break

print('#'*10)
print('一共花费%s元'%(price))
print('购物结束，再见！！')
9,9\]9+]]]22a3xx455tt