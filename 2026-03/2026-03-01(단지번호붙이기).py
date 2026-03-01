N = int(input())

matrix = [list(map(int, input())) for _ in range(N)] ## 입력 형식 항상 잘보기
visited = [[0]* N for _ in range(N)]
cnt = 1
answer = []
q=[]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            num = 0
            q.append((i, j))
            visited[i][j] = cnt 

            while q:
                num += 1
                ii, jj = q.pop(0)

                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ni, nj = ii+di, jj+dj

                    if 0<=ni<N and 0<=nj<N:
                        if matrix[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = cnt
                            mi, mj = ni, nj
                            q.append((mi, mj))

            cnt +=1
            answer.append(num)

cnt -= 1
print(cnt)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
