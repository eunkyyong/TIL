def hexTodec(s):
    result = 0
    for c in s:
        if c.isdigit():
            result = result * 16 + int(c)
        else:
            # ASCII CODE
            result = result * 16 + ord(c) - ord('A') + 10
            # ord('A') = 10
    return result

def decTohex(intV):
    s = ''
    while intV > 0:
        r = intV % 16
        if r <10:
            s = str(r) + s
        else: # 10을 뻬서 고민.
            s = chr((r-10)+ord('A')) + s
        intV //= 16
    return s

def hexTobin(s):
    value = hexTodec(s)
    binS = decTobin(value)
    return binS

def binTodec(s):
    result = 0
    for c in s:
        result = result*2 + int(c)
    return result

def decTobin(intV):
    s = ''
    while intV > 0:
        s = str(intV%2) + s
        intV //= 2
    return s

def hexToBin(hexS):
    mapping = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
               '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
               'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    # key없으면 RuntimeError
    hexS= ''
    for c in hexS:
        hexS += mapping[c]
    return hexS


s = '11001'
print(bintodec(s))      # 25
print(dectobin(25))     # 11001
print(hextodec(s))      # 69633
print(hextodec('A0'))   # 160
print(dectohex(160))

hexS = 'AA0'
print(hexToBin(hexS))
print(hexToBin('2FA3'))