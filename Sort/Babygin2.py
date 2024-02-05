# N = 3
# numbers = [0, 1, 2]
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             continue #(반복안하고 다시 위로 올라갈 때)
#         for k in range(3):
#             if k==i or k==j:
#                 continue
#             print(i, j, k) # i, j, k는 위치를 나타내는 인덱스.
#             # numbers[i], numbers[j], numbers[k]가 되어야 함
# # ---------------------------------------------------
# def babygin(counts):
#     n_tri = 0
#     n_run = 0
#     i = 0
#     while i<10: # 필요할 때만 증가
#         if counts[i] >= 3:
#             n_tri += 1
#             counts[i] -= 3
#         if i<=7 and counts[i] > 0 and counts[i+1] >0 and counts[i+2]>0:
#             n_run += 1
#             counts[i] -= 1
#             counts[i+1] -= 1
#             counts[i + 2] -= 1
#             continue
#
#         i += 1 # 위 조건 둘다 아닐때만 i 증가
#     print(n_tri, n_run)
#     return
# t = babygin([0, 0, 0, 0, 0, 0, 0, 2, 2, 2])
# t = babygin([0, 0, 0, 0, 0, 4, 1, 1, 0, 0])
# t = babygin([0, 0, 0, 0, 0, 0, 1, 1, 3, 1])
# ----------------------------------------------------------

def babygin(s_numbers): # str으로 받음
    counts = [0] *12 # (run 확인 시 오류남, 10 + 2)
    numbers = list(map(int, s_numbers))
    for n in numbers:
        counts[n] += 1
    # print(s_numbers, counts)

    n_tri = 0
    n_run = 0
    for i in range(12):
        while i<10:
            if counts[i] >= 3:
                n_tri += 1
                counts[i] -= 3
            if i<= 7 and counts[i]>0 and counts[i+1]>0 and counts[i+2]>0:
                n_run += 1
                counts[i] -= 1
                counts[i+1] -= 1
                counts[i+2] -= 1
                continue
            i += 1
    print(n_tri, n_run)
    return


t = babygin([0, 0, 0, 0, 0, 0, 0, 2, 2, 2])
t = babygin([0, 0, 0, 0, 0, 4, 1, 1, 0, 0])
t = babygin([0, 0, 0, 0, 0, 0, 1, 1, 3, 1])
# -------------------------------------------------------------
# def babygin(n_numbers): # int으로 받음
#     counts = [0] *12 (run 확인 시 오류남)
#     for _ in range(6):
#         d = n_numbers % 10
#         count[d] += 1
#         n_numbers //= 10
    # print(n_numbers, counts)
    # n_tri = 0
    # n_run = 0
    #
    # while i<10: # 필요할 때만 증가
    #     if counts[i] >= 3:
    #         n_tri += 1
    #         counts[i] -= 3
    #     if i<=7 and counts[i] > 0 and counts[i+1] >0 and counts[i+2]>0:
    #         n_run += 1
    #         counts[i] -= 1
    #         counts[i+1] -= 1
    #         counts[i + 2] -= 1
    #         continue
    #
    #     i += 1 # 위 조건 둘다 아닐때만 i 증가
    # print(n_tri, n_run)
    # return
