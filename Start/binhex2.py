num = '10'
print(int(num))
print(int(num, 10))
print((num, 2))
print((num, 16))

num = 5
binV = bin(num)
hexV = hex(num)
print(num)
print(num, binV, type(binV))
print(num, hexV, type(hexV))