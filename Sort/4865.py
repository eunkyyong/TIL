T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = [0] * 100
    for c in str1:
        cnt[c] += 1
    print(cnt)
