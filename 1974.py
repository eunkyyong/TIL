def sub_check():
    for s_row in range(0, 9, 3):
        for s_col in range(0, 9, 3):
            cnt = [0]*10
            for dr in range(3):
                for dc in range(3):
                    number = ARR[s_row+dr][s_col+dc]
                    if cnt[number]:
                        return False

    return True
# 이런식으로 쭉 하자.

