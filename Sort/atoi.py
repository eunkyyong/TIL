def atoi(s):  # '123' => 123
    r = 0
    for c in s:
        r = r*10 + (ord(c) - ord('0'))
    return r
t = atoi('123')
print(t, type(t))

def itoa(number):   # 321 => '321'
    result = ''
    while number > 0:
        c = chr(ord('0') + number % 10)
        result = c + result
        number //= 10
    return result

t = itoa(321)
print(t, type(t))
