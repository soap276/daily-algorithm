N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

# answer = []
visited =[[0]* N for _ in range(N)]
stack = []
cnt =1
answer = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            stack.append((i, j))
            visited[i][j] = cnt
            num = 0
            while stack:
                num +=1
                x, y = stack.pop(0)

                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x+dx, y+dy

                    if 0<=nx<N and 0<=ny<N:
                        if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                            ii, jj = nx, ny
                            visited[ii][jj] = cnt
                            stack.append((ii, jj))

            answer.append(num)
            cnt += 1
cnt -= 1
print(cnt)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
