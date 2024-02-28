# 빠른 순서대로 정렬하기
person = [10, 15, 30, 50]
n = len(person)
person.sort()
sum = 0
left_person = n-1

for turn in range(n):
    time = person[turn]  # 오름차순 정렬한 lst
    # 누적합 = 남은 사람 * 시간
    sum += left_person * time
    left_person -= 1
print(sum)
