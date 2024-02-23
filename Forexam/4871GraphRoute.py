import sys
sys.stdin = open("C:\cek\pycharm\TIL\Forexam\sample_input (7).txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    state = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = list(map(int, input().split()))
        state[a][b] = 1
    S, G = map(int, input().split())


