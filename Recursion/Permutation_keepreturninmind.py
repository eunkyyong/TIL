# Combination with recursion
def dfs(level):
    if level == 3:
        print(*path)
        return

    for i in range(len(arr)):
        if arr[i] in path:
            continue

        path[level] = arr[i]
        print(f'{i} first / Lv: {level} / Before {path}')
        dfs(level+1)
        print(f'{i} second / Lv: {level} / Before {path}')
        path[level] = 0
        print(f'{i} third / Lv: {level} / Before {path}')

    return


arr = [i for i in range(1, 4)]
path = [0] * 3

dfs(0)