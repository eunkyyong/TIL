import sys
sys.stdin = open("C:\cek\PycharmProjects\pythonProject\Today-I-Learned\input.txt","r")

def Num(str):
    counts = [0] * 10
    for n in Ai:
        counts[n] += 1
    # print(counts)
    maxV = counts[0]  # 몇 번째 값인지 인덱스 바로 구할 수 있음
    maxP = 0  # 가장 많이 몇번 나왔는 지 구할 수 있음
    for i in range(10):
        if maxV <= counts[i]:
            maxV = counts[i]
            maxP = i
    return maxP, maxV

T = int(input())
for i in range(T):
    N = int(input())
    Ai = list(map(int, input())) #[4, 9, 6, 7, 9] # 하나씩 int로 바꿈
    a, b = Num(Ai) # 실행순서도 제대로 보자..
    print(f'#{i+1} {a} {b}') # 여기서 값 받아서 ..


