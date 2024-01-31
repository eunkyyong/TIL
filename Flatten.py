import sys
sys.stdin = open("C:\cek\PycharmProjects\pythonProject\Today-I-Learned\input2.txt","r")

def myMax():
    Max = height[0]
    MaxP = 0
    for i in range(100):
        if Max <= height[i]:
            Max = height[i]  # 값을 바꾸는게 아니라 index값 바꿔야함
            MaxP = i
    return MaxP

def myMin():
    Min = height[0]
    MinP = 0
    for j in range(100):
        if Min >= height[j]:
            Min = height[j]
            MinP = j # 인덱스 알아야 원래 있었던 자리 알 수 있음
    return MinP

def dump(height):
    for z in range(N):
        # 입력값을 확인하자. 의도한 대로 돌아가고 있는 지.
        MaxP = myMax()
        MinP = myMin()
        # 위에서 Max-1하면 이거 반영된 채로 Min구하므로 안됨
        # loop 끝나고 평탄화.
        height[MaxP] -= 1
        height[MinP] += 1
        # 한번씩 더!! 해야 함.왜??
        # 덤프를 1번 하는 건 : 최대, 최소 한번씩 구하는 것.
        # 이 문제에서는 덤프를 하고난 다음, 최대-최소 를 답으로 구해야 함.
        # 한번 더 돌려야 함.
        differ = height[MaxP]-height[MinP]
        if differ <= 1:
            break
# 함수를 따로빼기 myMin, myMax # dump모두 진행한 후, 그 때의 최대최솟값의 차를 구해야함!!
    MaxP = myMax()
    MinP = myMin()
    differ = height[MaxP] - height[MinP]
    return differ
    # print(height[MaxP], height[MinP])
T = 10
for i in range(10):
    N = int(input()) # dump_ch
    height = list(map(int, input().split()))
    a = dump(height)
    print(f'#{i+1} {a}')
