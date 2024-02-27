path = []
visited = [False] * 7

def KFC(x):
    if x == 3:
        print(path)
        return

    for i in range(1, 7):
        if visited[i]:
            continue  # 다시 위로 넘어가서 함수 진행?
        visited[i] = True  # 중복만 제거! 갔던 곳 또 안가서!
        path.append(i)
        KFC(x+1)
        path.pop()
        visited[i] = False

KFC(0)
