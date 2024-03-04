path = []

# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
# KFC(0)

# 중복순열
def run(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        run(x+1)

        path.pop()

    return  # 이걸 몰랐습니다!!! 이거 안써도 되는데.. 꼭 써야 하는 줄 알았

run(0)