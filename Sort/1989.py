T = int(input())
for tc in range(1, T+1):
    item = input().strip() # input받을 때 뒤에 space strip.......
    if item[::] == item[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
