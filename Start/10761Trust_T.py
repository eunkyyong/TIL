T = int(input())
for tc in range(1, T+1):
    lst = input().split()

    N = int(lst[0])
    pos = {'B': 1, 'O': 1}

    robot, x = lst[1], int(lst[2])
    pre_robot = robot
    pre_time = x
    pos[robot] = x
    total = x

    for i in range(3, len(lst), 2):
        robot, x = lst[i], int(lst[i+1])
        if pre_robot == robot:
            time = abs(x-pos[robot]) + 1  # 버튼 눌러야 하니까 +1
            pre_time += time

        else:
            # time = max(1, abs(x-pos[robot]) - pre_time + 1)
            time = abs(x-pos[robot])  # 이동 시간
            if time < pre_time:
                # O의 이동시간이 B가 간 시간보다 작았다. 내 차례오기 전에 이미 가있어서 버튼만 누르면 됨.
                time = 1
            else:
                # 더 걸리는 시간 구해야 함.
                time = time - pre_time + 1
            pre_time = time

        total += time
        pre_robot = robot
        pos[robot] = x
    print(f'{tc} {total}')