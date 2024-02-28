# def KFC(x):
#     x += 1
#     KFC(x)
#
# x = 0
# KFC(x)

# def KFC(x):
#     if x == 6:
#         return
#     print(x, end = ' ')
#     KFC(x+1)
#     print(x, end=' ')
#
# KFC(0)
#
# def KFC(x):
#     if x == 2:
#         return
#     KFC(x+1)
#     KFC(x+1)
#     print(x)
# KFC(0)

# def KFC(x):
#     if x == 3:   # level
#         return
#
#     for i in range(4):   # branch
#         KFC(x+1)
# KFC(0)

def run(level):
    if level == 3:
        return
    for i in range(2):
        KFC(level+1)
run(0)