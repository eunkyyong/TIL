def fun2(x):
    x *= 2
    print('func2=>', x)

def fun1(x):
    if x==5:
        return
    x += 1
    print('func1 =>', x)
    fun1(x)

for i in range(1, 5):
    print('main=>', i)
    fun1(i)

