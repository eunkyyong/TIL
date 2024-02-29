import sys
sys.stdin = open("C:\cek\pycharm\TIL\Forexam\input (20).txt", "r")

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)