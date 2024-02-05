# a = 'aa'
# b = 'ab'
# print(a>b) # False

a = 'aa'
b = 'a'
print(a>b) # True

# import sys
#
# a = ''
# b = 'h'
#
# print(sys.getsizeof(a))  # 49 byte
# print(sys.getsizeof(b))  # 50 byte
#
# def itoa(a):
#     s = ''
#     while a > 0:
#         s = chr(a%10+ord('0')) + s
#         a //= 10
#         return s
# ans = itoa(123)
# print(ans)
#         # ord() : ASCII code
#         # char(3 + ord('0')) = ??
#
# # ------------------------------------
# # 문자열을 아스키 함수로 바꿔주는 함수 - IM 에 이 문제 나온 적 없음!!
# a = ord('1')
# print(a)
# # ASCII -> 0: 48, @: 64
# # a = ord('f') - ord('a') + ord('A')
# # print(chr(a))
# # --------------------------------------
# s = "abcdef test"
# # new_s = s[::-1]
#
# result = ''
# for idx in range(len(s)-1, -1, -1):
#     c = s[idx]
#     result = result + c
# print(result)
# s = 'a' + 'b'
# s = 'b' + 'a'


# N = len(s)
# l_s = list(s)
# for i in range(N//2):
#     l_s[i], l_s[N-1-i] = l_s[N-1-i], l_s[i] # 문자열은 안에서 바꾸는 거 안됨.
# t = ''.join(l_s)  # 합칠 때 ''를 기준으로 묶어줘
# print(t)
#
# print(s.reverse())  #Error. reverse()는 method이므로 string에는 없고 list에는 있다.
#
# l_s = list(s)
# print(l_s.reverse())  # method를 쓰면 자기 자신을 바꾼다. return 값이 없다!!!
# print(''.join(l_S))  # 이렇게 하면 잘 나온다!

