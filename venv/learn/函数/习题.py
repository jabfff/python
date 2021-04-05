def line():
    print('--'*3)

#line()



def n_line(a):
    for i in range(a):
        line()

#n_line(2)




def Sum3Num(x,y,z):
    result = x + y + z
    return result

def average3Number(x,y,z):
    sumResult = Sum3Num(x,y,z)
    aveResult = sumResult/3.0
    return aveResult

#g = Sum3Num(1,2,4)
#print(g)
G = average3Number(2,4,6)
print(G)