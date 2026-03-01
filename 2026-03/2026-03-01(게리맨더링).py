N = int(input())
# N = 6
people = list(map(int, input().split()))
# people =[5, 2, 3, 4, 1, 2]
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(N):
    inp = list(map(int, input().split()))

    graph[i+1].extend(inp[1:])

# graph =[[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]
min =10000
arr=[]
for i in range(1, N+1):
    arr.append(i)
# arr = [1, 2, 3, 4, 5, 6]


# 부분집합들이 서로 연결되어 있는지 확인
def connect(node):
    
    if not node:
        return False
    
    start = node[0]
    q = []
    q.append(start)
    visited = [start]

    while q:
        cur = q.pop(0)
        for data in graph[cur]:
            if data in node and data not in visited:
                visited.append(data)
                q.append(data)

    if len(visited) == len(node):
        return True


# 부분집합 만들기
for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1<<j):
            subset.append(arr[j])

    A = subset
    B=[]
    for a in arr:
        if a not in A:
            B.append(a)

    if not A or not B:
        continue
    
    A_peo = 0
    B_peo = 0
    if connect(A) and connect(B):
        for k in A:
            A_peo += people[k-1]
        for kk in B:
            B_peo += people[kk-1]
        peo_min = abs(A_peo - B_peo)

        if min > peo_min:
            min = peo_min

if min == 10000:
    print(-1)
else:
    print(min)
