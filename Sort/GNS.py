import sys
sys.stdin = open("C:\cek\pycharm\TIL\Sort\GNS_test_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    f'{input()}'
    # input 들어온 것을 뒤에 str만 쪼개자.
    strr = input().split()  # list로 나옴. ['SVN', 'FOR', 'ZRO', 'NIN', ...]
    N = len(strr)
    cnts = [0]*10  # 0-9 까지의 숫자
    gns = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    name = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    # 리스트 strr 내 요소들을 gns 딕셔너리 내 키와 일치한 값은 딕셔너리 값으로 치환해서 새로운 리스트 작성 가능??
    # print(strr[0]) SVN
    # print(*strr) # SVN FOR ZRO NIN FOR EGT EGT TWO
    for x in strr:
        pos = gns.get(x)
        cnts[pos] += 1
        # print(type(cnts)) list
        # print(type(pos)) int
    # cnt만큼 새로운 리스트에 배열
    lst = []
    for i in range(10):
        for j in range(cnts[i]):
            lst.append(name[i])
    print(f'#{tc}')
    print(*lst)

