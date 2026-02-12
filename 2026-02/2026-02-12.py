
# < 강사님 코드 >
lst = [1, 2, 3, 4, 5]
N = 5

# 부분집합 구하기 (재귀함수)
# idx : 내가 현재 idx 번째 원소를 부분집합에 넣을지 말지 고민중..
# selected : 내가 고른 원소의 상태를 나타낸다
# selected[x] == 1: x번째 원소를 부분집합에 넣기로 했다.
# selected[y] == 0: y번째 원소를 부분집합에 넣지 않기로 했다.
def make_set(idx, selected):

    # 1. 종료 조건
    # 원소의 개수가 총 N개니까
    # 선택을 N번 했다면 종료
    if idx == N:
        # 부분집합 하나가 완성 되었다.
        for i in range(N):
            if selected[i]:
                print(lst[i], end = ' ')
        print()
        return

    # 2. 재귀 호출
    # idx번 원소를 부분집합에 넣기로 하고 idx+1번 원소를 고민하러
    selected[idx] = 1
    make_set(idx+1, selected)
    # idx번 원소를 부분집합에 넣지 않기로 하고 idx+1번 원소를 고민하러
    selected[idx] = 0
    make_set(idx+1, selected)

make_set(0, [0] * N)


# 활용 -> 부분집합의 합이 s이하인 부분집합만 구하세요 -> 합이 '이하'일때만 가지치기 가능
# 이상일때는 끝까지 다 해봐야함
S = 5
lst = [1, 2, 3, 4, 5]
N = 5

# 부분집합 구하기 (재귀함수)
# idx : 내가 현재 idx 번째 원소를 부분집합에 넣을지 말지 고민중..
# selected : 내가 고른 원소의 상태를 나타낸다
# selected[x] == 1: x번째 원소를 부분집합에 넣기로 했다.
# selected[y] == 0: y번째 원소를 부분집합에 넣지 않기로 했다.
# s : 지금까지 내가 만든 부분집합의 합
def make_set(idx, selected, s):

    # 0. 가지치기
    # 답이 될 가능성이 없으면 더이상 진행하지 않도록
    # 지금까지 내가 만든 부분집합의 합이 S보다 크면 진행 X
    if s > S:
        return

    # 1. 종료 조건
    # 원소의 개수가 총 N개니까
    # 선택을 N번 했다면 종료
    if idx == N:
        # 부분집합 하나가 완성 되었다.
        subset = []
        for i in range(N):
            if selected[i]:
                subset.append(lst[i])
        # if sum(subset) <= S:
            print(subset, sum(subset))
        return

    # 2. 재귀 호출
    # idx번 원소를 부분집합에 넣기로 하고 idx+1번 원소를 고민하러
    selected[idx] = 1
    make_set(idx+1, selected, s + lst[idx])
    # idx번 원소를 부분집합에 넣지 않기로 하고 idx+1번 원소를 고민하러
    selected[idx] = 0
    make_set(idx+1, selected, s + 0)

make_set(0, [0] * N, 0)


## 순열
# 3자리수 순열의 경우의 수 : 3x2x1 = 6가지
# 자리 주인을 정하는 방식의 순열
# 0번 자리에 올 원소 정하기
# 1번 자리에 올 원소 정하기
# ...
# N-1번 자리에 올 원소 정하기 (마지막은 알아서 정해짐)
lst = [1, 2, 3, 4, 5]
N = 5
# reslt = [?, ?, ?, ?, ?]
# idx : 순열의 idx번 자리에 올 원소를 선택하는 중이다.
# selected : 순열을 만들때 이전에 사용했던 원소를 체크 (중복 선택 방지)
# selected [x] == 1 : x번 원소는 이전에 사용했다.
# selected [y] == 0 : y번 원소는 이전에 사용안했다.
# result: 지금까지 만든 순열 ([], ())
def make_perm(idx, selected, result):
    # 1. 종료 조건
    # 0번자리부터 N-1번자리까지 다 주인 정했으면 종료 (N번자리는 없음)
    if idx == N:
        # 지금까지 만든 순열 출력
        print(result)
        return
    # 2. 재귀 호출
    # idx번 자리에 올 숫자가 누군지 하나 선택
    # 이전에 내가 고른적 없는 숫자만 선택가능
    for i in range(N):
        # N개의 원소 일일히 확인하며 이전에 사용한 원소면 넘어가
        # 이전에 사용한적 없는 원소면 idx자리에 놓고 idx+1번 단계로 진행
        if not selected[i]:
            # idx번 자리에 i번 원소를 놓고 진행
            selected[i] = 1
            # 순열 만들기
            result.append(lst[i])
            # i번 원소를 idx번 자리에 놓고 나머지 경우의 수 고려
            make_perm(idx+1, selected, result)
            # i번 원소는 다음 자리에서 또 쓸수 있도록 기록 제거
            selected[i] = 0
            result.pop()
# 0번 자리부터 정하기 시작
# 아직 아무것도 고르지 않은 상태
# 순열은 미완성 상태
make_perm(0, [0] * N, [])

## 순열2
lst = [1, 2, 3, 4, 5]
N = 5
# idx : idx번 원소의 자리를 교환하겠다

def make_perm(idx):

    # 1. 종료 조건
    if idx == N:
        print(lst)
        return
    # 2. 재귀 호출
    # idx번 원소와 다른 위치에 있는 원소를 하나 정하고
    # 자리를 바꾼다. 다른 위치(j)의 조건 idx보다 작으면 안된다. (같으면 그 자리 그대로 있는 경우)
    for j in range(idx, N):
        # idx번 원소와 j번 원소 자리를 바꾸겠다.
        lst[idx], lst[j] = lst[j], lst[idx]
        make_perm(idx+1)
        # 자리 바꿨던 일을 없던일로 하고 다른애랑 바꿔야 한다.
        lst[idx], lst[j] = lst[j], lst[idx]

make_perm(0)

## 백트레킹
# 미로찾기 알고리즘
# 스택을 이용하여 지나온 경로를 역으로 되돌아 감

def maze_backtracking(maze, start, end):
    N = len(maze)
    M = len(maze[0])

    # 방문 체크 배열
    visited = [[False] * M for _ in range(N)]

    # 경로 저장 스택
    stack = []

    # 시작 위치 push
    stack.append(start)
    visited[start[0]][start[1]] = True

    while stack:
        # 현재 위치 = 스택 맨 위
        x, y = stack[-1]

        # 도착하면 경로 반환
        if (x, y) == end:
            return stack

        moved = False # 이번 턴에 이동했는지 체크

        # 4방향 탐색
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x+dx
            ny = y + dy
            # 범위 안, 벽 아님, 방문 안 함 -> 이동
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and maze[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

                    moved = True
                    break

        # 갈 곳 없으면(이번턴에 이동하지 않았다면) -> 뒤로이동 (백트레킹)
        if not moved:
            stack.pop()

    # 경로 못 찾으면
    return None

maze = [
 [0,1,1,1],
 [0,0,0,1],
 [1,1,0,1],
 [1,0,0,0]
]

path = maze_backtracking(maze, (0,0), (3,3))

if path:
    print("경로:", path)
else:
    print("경로 없음")



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N      # 열 사용 체크
    min_sum = 1000000

    def backtrack(row, total):
        global min_sum

        # 가지치기: 중간합이 이미 최소합 이상이면 중단
        if total >= min_sum:
            return

        # 종료 조건: 모든 행을 다 선택했으면 최소값 갱신
        if row == N:
            min_sum = min(min_sum, total)
            return

        # 현재 행에서 선택할 열 탐색
        for col in range(N):
            # 이전에 사용한 적 없는 열이면 방문
            if not selected[col]:
                # 방문체크
                selected[col] = 1
                # 다음 행으로 가서 또 열 선택
                backtrack(row + 1, total + arr[row][col])
                # 다른 행의 열이 들어올 수 있도록 열 선택한 기록 제거
                selected[col] = 0

    backtrack(0, 0)

    print(f"#{tc} {min_sum}")
