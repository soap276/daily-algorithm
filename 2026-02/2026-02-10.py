# 피보나치 수를 구하는 재귀함수
def fibo(n):
    if n<2: # F0 = 1, F1 = 1
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 재귀함수의 기본형
def f(i, N):
    if i == N: # 중단조건
        return
    else: # 재귀호출
        f(i+1, N)

def f(i, N): # arr[i]에 접근하는 재귀함수
    if i == N: # 모든 원소에 접근했으면
        return
    else:
        print(A[i])
        f(i+1, N) # 다음 원소 A[i+1]로 이동

A = [1, 2, 3]
f(0, 3)

# 배열 원소 검색
# 배열에 v가 있으면 1, 없으면 0 리턴
# v = 5 인 경우, arr 에는 5가 없으므로 마지막 단계까지 호출하고 0 리턴
def f(i, N, V):
    if i ==N:  #V를 못찾은 경우
        return 0
    elif A[i] == V:
        return 1
    else:
        return f(i+1, N, V)

N = 3
A = [3, 7, 6]
V = 2

ans = f(0, N, V)
print(ans)


## 메모이제이션
# 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록하여
# 전체적인 실행 속도를 빠르게 하는 기술

def fibo1(n):
    global cnt
    cnt += 1
    if n>=2 and memo[n] == 0: # memo[n]이 0이 아니면 -> 이미 계산된 값, 바로반환
        memo[n] = fibo1(n-1) + fibo1(n-2) # 처음 계산하는 값이면 재귀 호출
    return memo[n]

n = 10
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
cnt = 0
print(fibo1(10), cnt)

## DP: 동적계획법
# 크기가 작은 부분문제를 먼저 해결한 뒤
# 그 결과를 바탕으로 더 큰 부분문제를 차례대로 해결해나가는 알고리즘
# 동일한 하위 문제가 여러 번 반복되어 나타나는 중복 부분 문제여야 함
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

## DFS
# 깊이 우선 탐색


# 2차원 배열을 순회하는 재귀함수 만들기

N = 5

arr = [[N*j+i for i in range(1, N+1)] for j in range(N)]
# 시작 i = 0, j = 0
# 종료 i=4, j=4
# 시작 => 종료로 가기위해 i와 j가 어떻게 변하는가.. (행우선순회)
# 0, 0 => 0, 1 => 0, 2 .. => 1, 0 => 1, 1 => ...
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

# 바로 위의 for 문과 똑같은 배열을 출력하는 2차원 재귀함수 만들기
def myprint(i, j):
    # 1. 종료 조건 (현재 단계가 어떤 조건에 도달하면 재귀 호출을 멈추도록)
    if i >= N:
        return

    # 2. 재귀 호출 (현재 단계에서 필요한 작업을 하고 다음단계로)
    # 단, 다음단계로 가면 갈수록 종료조건에 가까워 져야 한다.

    print(arr[i][j], end =' ')
    j += 1
    if j == N:
        i += 1
        j = 0
        print()
    myprint(i, j)

print('================')

myprint(0, 0)



# 인접 행렬
# A = 0, B = 1,,,, G = 6
# 정점의 개수는 N = 7 개

# adj_matrix = []
# 1번 정점과 2번 정점이 인접 (다른 정점을 거치지 않고 바로 연결)
# adj_matrix[1][2] = 1
# adj_matrix[2][1] = 0 (유향 그래프인 경우 역방향 x)
# 3번 정점과 4번 정점이 인접하지 않음
# adj_matrix[3][4] = 0
adj_matrix = [[0, 1, 1, 0, 0, 0, 0], # A
              [1, 0, 0, 1, 1, 0, 0], # B
              [1, 0, 0, 0, 1, 0, 0], # C
              [0, 1, 0, 0, 0, 1, 0], # D
              [0, 1, 1, 0, 0, 1, 0], # E
              [0, 0, 0, 1, 1, 0, 1], # F
              [0, 0, 0, 0, 0, 1, 0]] # G

# 인접 행렬로 그래프를 나타낸 상태에서 깊이 우선 탐색
# s : 탐색을 시작하는 정점 번호
# v : 정점의 개수
def dfs(s, V):
    # dfs: 깊이우선탐색
    # 그래프의 모든 정점을 빠짐없이 한번씩 모두 탐색
    # 내가 이전에 방문 했는지 안했는지 여부를 확인
    visited = [0] * V
    # visited[5] == 1 => 5번 정점을 방문한적이 있다.
    # visited[6] == 0 => 6번 정점을 방문한적이 없다

    # 돌아올 길을 저장(기억)할 스택
    stack = []

    # 시작정점 s를 방문했다 처리
    visited[s] = 1
    print(s)

    # 현재 내가 방문하고 있는 정점 번호 v
    v = s

    # 그래프 탐색 시작
    while True:
        # 현재 내가 있는 정점 번호는 v
        # v와 인접한 정점(w)이 있나 없나 확인 => 있다면 이전에 방문 했나 안했나 확인
        # 방문 가능하면 방문한다.

        for w in range(V):
            # v와 w가 인접하고 w를 이전에 방문한적이 없으면 방문한다.
            if adj_matrix[v][w] and not visited[w]:
                # w는 갈 수 있다.
                # 방문처리, w 정점에서 필요한 작업을 한다.
                # w에서 더이상 갈 길이 없으면 v로 돌아와야 하니
                # v를 스택에 저장
                stack.append(v)
                # w를 방문했다고 처리
                visited[w] = 1
                # w 정점에서 할일
                print(w)
                # w로 이동해서 위에서 했던 탐색을 반복
                v = w
                # 바뀐 v에서 새로운 탐색을 해야 하기 때문에 break
                break
        else:
            # 반복 중에 break 한적이 없다 => 이동가능한 다른 정점이 없다.
            # 이전 길로 돌아가기 (스택에서 돌아갈 정점번호 꺼내기)
            if stack:
                # 스택에서 돌아갈 곳 꺼내서 현재 위치로 바꾸기
                stack.pop()
            else:
                # 스택이 비었다면 돌아갈곳이 없다. => 모든 정점 탐색 완료
                break # for while

# 0번 정점에서 시작하고 정점의 개수는 7개
dfs(0, 7)



## 과제 그래프 경로 문제
T = int(input())
for tc in range(1, T+1):
    # V, E = 정점의 개수, 간선의 개수
    V, E = map(int, input().split())
    
    # 인접 행렬
    # adj_m[1][2] == 1 => 1번에서 2번가는길 o
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    
    # 그래프 정보 입력
    # 출발-도착 정점 쌍(간선) 정보가 E개 입력으로 들어온다.
    for i in range(E):
        s, e = map(int, input().split())
        adj_m[s][e] = 1
        # adj_m[e][s] = 1 요건 안됨 (무향 그래프에서 사용)
    
    # 테스트케이스 입력 마지막에 출발 정점 번호, 목표 정점 번호
    S, G = map(int, input().split())
    
    # S에서 출발하는 DFS 탐색, 탐색중 G를 만나면 탐색 종료
    
    # 처음엔 도착 불가능이라고 가정, dfs 탐색 중 G를 만나면 1로
    answer = 0
    
    ### DFS
    
    print(f'#{tc} {answer}')

