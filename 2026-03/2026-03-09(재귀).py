# 반복과 재귀
# 재귀함수 -> N중 for문에 가장 많이 이용
# 상태공간트리 가지의 수 = 재귀의 수

# 0~10을 출력
# 10에서 종료 (10보다 커지면 종료)
# 다음 재귀 호출 : num을 1씩 증가
def recur(num):
    if num > 3:
        return
    print(num, end = ' ')
    print()
    recur(num + 1)
    recur(num + 1)
    # print(num, end = ' ')

def recur2(num):
    if num > 3:
        return
    # print(num, end=' ')
    for i in range(1, 7):
        recur2(num+1)

recur(0)
recur2(0)

# 중복 순열
# [0, 1, 2] 3개의 카드가 존재 (2개를 뽑는 모든 경우)

# 기저조건: 2개의 카드를 모두 뽑았을 경우
# - 시작: 0개의 카드를 고른 상태부터 시작
# 다음 재귀 호출: 카드 3개 중 하나를 선택
path = []
def recur(cnt):
    if cnt == 2:
        print(path)
        return
    for i in range(3):
        path.append(i)
        recur(cnt+1)
        path.pop()

    # # 0을 선택
    # path.append(0)
    # recur(cnt+1)
    # path.pop()
    # # 1을 선택
    # path.append(1)
    # recur(cnt+1)
    # path.pop()
    # # 2를 선택
    # path.append(2)
    # recur(cnt+1)
    # path.pop()

recur(0)

# [심화] 경로를 전역변수 쓰지 않고 하는 방법
# - 경로를 누적하면서 파라미터로 전달한다.
def recur2(cnt, p):
    if cnt == 2:
        print(*p)
        return
    for i in range(3):
        recur2(cnt+1, p+[i])

recur2(0, [])



# 중복 제거된 순열
path = []
def recur(cnt):
    if cnt == 2:
        print(path)
        return
    for i in range(3):
        # 주의!!! in 은 O(N)이라서 너무 느리다 -> 시간초과 가능성 큼
        if i in path:
            continue

        path.append(i)
        recur(cnt+1)
        path.pop()
recur(0)

# -----중복없애기------

path = []
N = 3
visited = [0]*N # N개의 카드

def recur2(cnt):
    if cnt == 2:
        print(*path)
        return
    for i in range(3):
        if visited[i]: # 이미 i를 사용한적이 있다면
            continue

        visited[i] = 1 # 방문처리
        path.append(i)
        recur2(cnt + 1)
        path.pop()
        visited[i] = 0


recur2(0)


# 주사위 3개의 합 10이하인 경우의 수
# 주사위 3개 -> depth: 3
# branch 수 : 1~6 숫자 -> 6
path = []
result = 0
def recur(cnt):
    global result
    if cnt == 3:
        if sum(path) <= 10: # 경로의 합이 10 이하라면
            print(*path)
            result += 1
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt +1)
        path.pop()

# [업그레이드 버전]
path = []
result = 0
def recur(cnt, total):
    global result
    # 이미 10을 넘었으면 이 케이스는 더 볼 필요 없음
    if total > 10:
        return
    if cnt == 3:
        if total <= 10: # 경로의 합이 10 이하라면
            # print(*path)
            result += 1
        return

    for num in range(1, 7):
        # path.append(num)
        recur(cnt + 1, total+num)
        # path.pop()

recur(0, 0)





# 강사님 코드

# 0 1 2 3 4 5 5 4 3 2 1 0
def recur(num):
    # 1. 종료 조건
    if num > 5:
        return
    # 2. 재귀 호출
    # 종료조건에 점점 더 가까워지도록
    print(num, end = ' ')
    recur(num+1)
    print(num, end = ' ')

recur(0)


# [과제]1부터 6까지 사용하는 중복순열 [1, 1, 1] ~ [6, 6, 6]을 출력하는 코드를 재귀호출로 구현
path = []
def recur(cnt):
    if cnt == 3:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        recur(cnt + 1)
        path.pop()
recur(0)


# 심화버전
def recur2(cnt, path):
    if cnt == 3:
        print(path)
        return

    for i in range(1, 7):
        recur2(cnt+ 1, path+[i])

recur2(0, [])


# 중복되는 수가 없도록

arr = [1, 2, 3, 4, 5, 6]
N = 3
visited = [0] * (len(arr)+1)
path = []
def recur(cnt):
    if cnt == N:
        print(path)
        return

    for i in arr:
        if not visited[i]:
            path.append(i)
            visited[i] = 1
            recur(cnt + 1)
            path.pop()
            visited[i] = 0

recur(0)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 10000
    def ans(i, j, sum_data):
        global result
        sum_data += matrix[i][j]

        if sum_data > result:
            return

        if i == N-1 and j == N-1:
            result = min(result, sum_data)
            return

        for di, dj in [[1, 0], [0, 1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                ans(ni, nj, sum_data)

    ans(0, 0, 0)
    print(f'#{tc} {result}')



T = int(input())
for tc in range(1, T+1):
    # 구역의 개수
    # 0: 사무실
    # 1~N: 나머지 구역
    N = int(input())
    # E[i][j] : i번 구역에서 출발해서 j번 구역으로 갈 때 에너지 사용량
    # E[i][j]는 E[j][i]와 다를수도 있다.
    E = [list(map(int, input().split())) for _ in range(N)]

    # 최소 에너지 사용량
    min_e = float("inf")

    # 방문체크 배열 (이전에 방문한 구역은 다시 방문 X)
    visited = [0] * N
    # 첫번째 방은 사무실, 방문 체크 미리 해두자
    visited[0] = 1
    # now_room: 현재 위치한 방 번호
    # e: 현재 방번호까지 오는데 사용한 에너지량
    def patrol(now_room, e):
        global min_e

        # 0. 가지치기
        # 현재까지 구한 에너지의 합이 내가 알고있는 최소 에너지보다 크면?
        # 더이상 진행할 필요가 없다
        if e >= min_e:
            return

        # 1. 종료 조건
        if 0 not in visited:
            # 남은 방문할 구역이 없다면 종료
            # 끝에 첫번째 방으로 돌아오는 것까지 생각
            e += E[now_room][0]
            # 현재 완성한 경로의 에너지 사용량과 이전에 최소였던 에너지 중에서 최솟값
            min_e = min(e, min_e)
            return

        # 2. 재귀 호출
        # 내가 지금까지 선택하지 않은 구역중 하나 선택
        # 다음 단계로
        for next_room in range(N):
            # next_room : 이번에 방문할 방 번호
            if not visited[next_room]:
                # 방문하지 않았다면 이번에 방문
                visited[next_room] = 1
                # 다음에 방문할 방 번호 선택하러 재귀호출
                # 현재 방 번호를 알고 있어야 에너지 사용량을 계산
                e_sum = E[now_room][next_room]
                # e += e_sum
                # 주의 !!! 에너지 사용량 되돌리기
                patrol(next_room, e+e_sum)
                visited[next_room] = 0
    # 0번 (사무실) 에서 출발, 에너지 사용량 0부터 시작
    patrol(0, 0)

    print(f'{tc} {min_e}')



T = int(input())
for tc in range(1, T+1):

    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N)]

    # 최소 에너지 사용량
    min_e = float("inf")

    # 방문체크 배열 (이전에 방문한 구역은 다시 방문 X)
    visited = [0] * N
    # 첫번째 방은 사무실, 방문 체크 미리 해두자
    visited[0] = 1
    # now_room: 현재 위치한 방 번호
    # e: 현재 방번호까지 오는데 사용한 에너지량
    def patrol(now_room, e):
        global min_e

        # 0. 가지치기
        # 현재까지 구한 에너지의 합이 내가 알고있는 최소 에너지보다 크면?
        # 더이상 진행할 필요가 없다
        if e >= min_e:
            return

        # 1. 종료 조건
        if 0 not in visited:
            # 남은 방문할 구역이 없다면 종료
            # 끝에 첫번째 방으로 돌아오는 것까지 생각
            e += E[now_room][0]
            # 현재 완성한 경로의 에너지 사용량과 이전에 최소였던 에너지 중에서 최솟값
            min_e = min(e, min_e)
            return

        # 2. 재귀 호출
        # 내가 지금까지 선택하지 않은 구역중 하나 선택
        # 다음 단계로
        for next_room in range(N):
            # next_room : 이번에 방문할 방 번호
            if not visited[next_room]:
                # 방문하지 않았다면 이번에 방문
                visited[next_room] = 1
                # 다음에 방문할 방 번호 선택하러 재귀호출
                # 현재 방 번호를 알고 있어야 에너지 사용량을 계산
                e_sum = E[now_room][next_room]
                # e += e_sum
                # 주의 !!! 에너지 사용량 되돌리기
                patrol(next_room, e+e_sum)
                visited[next_room] = 0
    # 0번 (사무실) 에서 출발, 에너지 사용량 0부터 시작
    patrol(0, 0)

    print(f'{tc} {min_e}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 10000
    visited = [0] * N
    visited[0] = 1

    def room(now_room, e_sum):
        global result

        if e_sum > result:
            return

        if 0 not in visited:
            e_sum += matrix[now_room][0]
            result = min(result, e_sum)
            return

        for next_room in range(N):
            if not visited[next_room]:
                visited[next_room] = 1
                plus = matrix[now_room][next_room]
                room(next_room, e_sum + plus)
                visited[next_room] = 0

    room(0, 0)
    print(f'{tc} {result}')





T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()

    cnt = int(cnt)
    N = len(num)
    result = 0
    num = list(str(num))
    # print(num)
    check = set()
    def solve(k, num):
        global result

        # # 가지치기
        # if k번 교환해서 만든 숫자열을 이전에 만든적이 있다면:
        #     return
        state = (k, ''.join(num))
        if state in check:
            return
        check.add(state)

        # 종료
        if k == cnt:
            number = 0
            for i in range(N):
                number += (10**(N-i-1)) * int(num[i])
            result = max(result, number)
            return

        # 재귀호출(다음단계)
        # 자리를 교환해서 다음 단계(다음 교환횟수)
        # 앞쪽자리 인덱스 i : 0 ~ N-2
        # 뒤쪽자리 인덱스 j : i+1 ~ N-1
        for i in range(N-1):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                solve(k+1, num)
                num[i], num[j] = num[j], num[i]
        # i와 j를 정해서 자리바꾸기
        # 자리바꾼 다음에 다음 교환횟수로 => 재귀호출, 교환횟수 +1
        # i와 j를 바꿔서 원상복귀

    solve(0, num)
    print(f'#{tc} {result}')







