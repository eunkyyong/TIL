T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


# 선생님 코드
# def f(pat, txt, M, N):
# 	for i in range(N-M+1): # text에서 비교 시작
# 		for j in range(M):  # 불일치면 다음 시작위치로
# 			if txt[i+j] != pat[j]:
# 				break
# 		else:  # 패턴 매칭에 성공하면
# 			return 1
# # 모든 위치에서 비교가 끝난 경우
# 	return 0   # for 문 - 완전 검색 결과 확인할 때 !
#
# T = int(input())
# for tc in range(1, T+1):
# 	pat = input()
# 	txt = input()
# 	M = len(pat)
# 	N = len(txt)
#
# 	ans = f(pat, txt, M, N)
# 	print(f'#{tc} {ans}')