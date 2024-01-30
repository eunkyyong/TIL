import sys
sys.stdin = open("C:\cek\PycharmProjects\pythonProject\Today-I-Learned\input2.txt","r")

def dump(height):
    for z in range(N):
        # 입력값을 확인하자. 의도한 대로 돌아가고 있는 지.
        Max = height[0]
        MaxP = 0
        for i in range(100):
            if Max <= height[i]:
                Max = height[i] # 값을 바꾸는게 아니라 index값 바꿔야함
                MaxP = i
        # height 숫자 변경해야 함.
        # print(Max)
        Min = height[0]
        MinP = 0
        for j in range(100):
            if Min >= height[j]:
                Min = height[j]
                MinP = j
        height[MaxP] = height[MaxP] - 1
        height[MinP] = height[MinP]+1
        # 1회에 Max, Min구하고 cnt 변경 => N회 반복

    differ = height[MaxP]-height[MinP]
    return differ

T = 10
for i in range(10):
    N = int(input()) # dump_ch
    height = list(map(int, input().split()))
    a = dump(height)
    print(f'#{i+1} {a}')
    # print(N)
    # print(a)