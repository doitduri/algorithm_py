def calc(a, b, op):
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    else:
        return int(a) * int(b)


N = int(input())
equation = input()

# max_value가 - 가장 큰 값으로 초기화되어야
max_value = -10 ** 10

if N > 1:
    queue = [[int(equation[0]), 0, 0], [calc(equation[0], equation[2], equation[1]), 2, 1]]
    qlen = 2
else:
    qlen = 0
    max_value = equation[0]
start = 0

while qlen > 0:
    cur, ind, ans = queue[start]
    start += 1
    qlen -= 1

    # 하나 한 거랑 두 개 한 거랑 넣기
    # ind 길이 체크 => 종료 조건
    if ind == N - 3:
        cur = calc(cur, equation[N - 1], equation[N - 2])
        # ind가 N-1에 도달할 때마다 cur값과 max_value를 비교
        if max_value < cur:
            max_value = cur
        continue
    if ind == N - 1:
        if max_value < cur:
            max_value = cur
        continue

    # 하나만 계산하거나
    queue.append([calc(cur, equation[ind + 2], equation[ind + 1]), ind + 2, ans])
    # 뒤에 두 개를 먼저 계산하거나
    queue.append(
        [calc(cur, calc(equation[ind + 2], equation[ind + 4], equation[ind + 3]), equation[ind + 1]), ind + 4, ans + 1])

    qlen += 2

print(max_value)