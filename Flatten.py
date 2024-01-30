import sys
sys.stdin = open("/Users/eunkyyong/Desktop/practice/review/Today-I-Learned/input2.txt","r")

def dump(height):
    for z in range(N):
        # 입력값을 확인하자. 의도한 대로 돌아가고 있는 지.
        Max = height[0]
        MaxP = 0
        for i in range(100):
            if Max <= height[i]:
                Max = height[i] # 값을 바꾸는게 아니라 index값 바꿔야함
                MaxP = i
        Min = height[0]
        MinP = 0
        for j in range(100):      
            if Min >= height[j]:
                Min = height[j]
                MinP = j # 인덱스 알아야 원래 있었던 자리 알 수 있음
        # 위에서 Max-1하면 이거 반영된 채로 Min구하므로 안됨
        # loop 끝나고 평탄화.
        height[MaxP] -= 1
        height[MinP] += 1
        # 한번씩 덜 해야 함.왜??
        differ = height[MaxP]-height[MinP]
        if differ <= 1:
            break
    return differ
    # print(height[MaxP], height[MinP])
T = 10
for i in range(10):
    N = int(input()) # dump_ch
    height = list(map(int, input().split()))
    a = dump(height)
    print(f'#{i+1} {a}')
    # print(N)
    # print(a)