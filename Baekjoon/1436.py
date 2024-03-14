N = int(input())
lst = list(str(N//280))  # sixth_to_seventh
# lst 뒤로 append 하기
fst_fifth = N%280
if 0<= fst_fifth < 114:  # 0~5 _ _ _ _
    if fst_fifth%19 != 0:
        lst.append(str(fst_fifth//19))  # 5 _ _ _ _ 10e5숫자str 집어넣기
        if 0<=fst_fifth%19<7:  # _ 6 6 6 fst_fourth
            t = str(fst_fifth%19-1)
            lst.append(t)
            for _ in range(3):
                lst.append(str(6))

        elif 7<= fst_fifth%19 < 17:  # 666_ fst_fourth
            for _ in range(3):
                lst.append(str(6))
            t = str(fst_fifth % 19-7)
            lst.append(t)

        elif 17<= fst_fifth%19 < 19:  # _666 (7~9) fst_fourth
            t = str(fst_fifth % 19 - 10)
            lst.append(t)
            for _ in range(3):
                lst.append(str(6))
    else:  # 19의 배수
        lst.append(str(fst_fifth // 19-1))
        t = str(fst_fifth % 19+9)
        lst.append(t)
        for _ in range(3):
            lst.append(str(6))


elif 114<= fst_fifth < 224:  # 6 _ _ _ _
    if fst_fifth % 19 != 0:
        lst.append(str(6))
        if 114<=fst_fifth<121:  # _ 6 6 6 fst_to_fourth
            lst.append(str(fst_fifth%19-1))
            for _ in range(3):
                lst.append(str(6))

        elif 121<= fst_fifth < 190: # 6 6 __
            for _ in range(2):
                lst.append(str(6))
            if 7<= fst_fifth%19<16:
                lst.append(str(0))
                lst.append(str(fst_fifth-120))
            else:
                lst.append(str(fst_fifth - 120-1))


        elif 106 <= fst_fifth%19 < 109:  # (7~9) 6 6 6
            lst.append(str(fst_fifth-220))
            for _ in range(3):
                lst.append(str(6))

    else:  # 19의 배수
        # lst.append(str(fst_fifth // 19-1))
        for _ in range(3):
            lst.append(str(6))
        lst.append(str(fst_fifth//19-4))
        t = str(fst_fifth % 19+9)
        lst.append(t)



elif 224 <= fst_fifth < 280:
    lst.append(str((fst_fifth-223)%19+5))  # 7~9 _ _ _ _ 10e5숫자str 집어넣기
    if 0 <= (fst_fifth-223)%19 < 6:  # _ 6 6 6 fst_fourth
        t = str(fst_fifth % 19)
        lst.append(t)
        for _ in range(3):
            lst.append(str(6))

    elif 6 <= (fst_fifth-223)%19 < 16:  # 666_ fst_fourth
        for _ in range(3):
            lst.append(str(6))
        t = str((fst_fifth-223)%19 - 6)
        lst.append(t)

    elif 16 <= (fst_fifth-223)%19 < 19:  # _666 (7~9) fst_fourth
        t = str((fst_fifth-223)%19 - 9)
        lst.append(t)
        for _ in range(3):
            lst.append(str(6))
result = "".join(lst)
print(int(result))
# print(*lst)


# _666
# 666_ 2C1
#
# __666
# _666_
# 666__ 3C1
#
# 0 _ 6 6 6 : 2*10 - 1 = 19
#     _ 666: 0~5 6개
#     666_ : 0~9 10개
#     _666 : 7~9 3개
# 1 _ _ _ _ : 19
#     1_666: 0~5 6개
#     1666_: 0~9 10개
#     1_666: 7~9 3개
# 2 _ _ _ _ : 19
# 3 ----: 19
# 4 ----: 19
# 5 ----: 19 / 114
# 6 ----:
#     6_666: 0~5 : 6개 / 120개
#     666__: 66666 100개 / 187
#     6_666:7~9: 3개  // 9+100 = 109 114+109 = 223
# 223 + 57 = 280
# 6자리 수만 2520, 5+6자리 수: 2800
# _ _ _ _ _ _ : 0 _ _ _ _ _, 1 _ _ _ _ _
#             _ 6 6 6 _ _ :
#             _ _ 6 6 6 _ :
#             _ _ _ 6 6 6 : 6자리 수만 -> 9 * 280 = 2520
# 7자리 수만
# 9 * 2800 = 22,680
# N <= 10,000
# _ _ (_ _ _ _ _ : 280)
# N % 280 = 10e7, 6의 자리 숫자
# N // 280 =