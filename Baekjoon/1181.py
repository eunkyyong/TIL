N = int(input())
Len = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    length = len(word)
    Len[length].append(word)
for i in range(51):
    while Len[i]:
        lst = sorted(Len[i])
        result = list(dict.fromkeys(lst))
        for s in result:
            print(s)
        # print(result)
        break





