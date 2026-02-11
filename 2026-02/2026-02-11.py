# 중위 표기법 -> 후위 표기법으로 변경. stack 이용
# 후위 표기법의 수식을 stack을 이용하여 계산

stack = [0] * 10
top = -1

icp = {'(' : 3, '*':2, '/': 2, '+': 1, '-': 1}# 스택 밖에서의 우선순위
isp = {'(': 0, '*':2, '/': 2, '+': 1, '-': 1}# 스택 안에서의 우선선위
infix = '(6+5*(2-8)/2)' # 중위식 문자열
postfix = '' # 후위식 문자열

for token in infix:
    # 피연산자면 후위식에 추가
    if token not in '(*/+-)':
        postfix += token
    elif token == ')': # 닫는괄호면 여는 괄호는 만날때까지 pop
        while top > -1 and stack[top] != '(': # 언더플로우 확인
            top -= 1
            postfix += stack[top + 1]
        # while stack and stack[-1] != '(': # .append, .pop()을 활용할때
        #        postfix += stack.pop()
        if top != -1:
            top -= 1 # '(' 제거
    else: # '(*/+-' 인 경우
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token

        elif isp[stack[top]] >= icp[token]:
            while top > -1 and isp[stack[top]] >= icp[token]:
                top -= 1
                postfix += stack[top + 1]
            top += 1            # 스택의 마지막 연산자보다
            stack[top] = token  # 우선순위가 높아졌으므로 push

    # print(postfix, stack, top)
while top > -1: # 바깥쪽에 괄호가 없는 문자열일때
    top -= 1
    postfix += stack[top + 1]
print(postfix)


stack = []
for token in postfix:
    if token not in '*/+-': # 피연산자면 push
        stack.append(int(token)) # token은 문자열
    else: # 연산자면
        op2 = stack.pop() # 오른쪽 피연산자
        op1 = stack.pop() # 왼쪽 피연산자
        result = 0
        if token == '*':
            result = op1 * op2
        elif token == '/':
            result = op1 / op2
        elif token == '+':
            result = op1 + op2
        elif token == '-':
            result = op1 - op2
        stack.append(result)
# 스택에 연산결과 하나 남아있음
# 만약에 스택에 요소가 하나 이상이거나 값이 없으면 후위표기식 잘못된 것것answer = stack.pop()

print(answer)
print(f'{answer:.0f}')

## <강사님 코드>
# 중위 표기법 => 후위 표기법
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 밖에서 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 안에서 우선순위
# infix: 바꾸고 싶은 중위표기식
# n: 식의 길이
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
    stack = []

    # infix 에서 한글자씩 떼어와서 식을 만들자
    for i in range(n):
        # i번째 글자 확인
        # 연산자? 피연산자?
        if infix[i] not in '()+-*/':
            # i번 글자가 연산자가 아니였다. (숫자, 피연산자)
            # 결과로 출력(후위표기식에)
            postfix += infix[i]
        else:
            # i번 글자가 연산자였다.
            # i번 글자가 오른쪽 괄호 (닫는괄호)
            if infix[i] == ')':
                # '(' 여는 괄호가 나올 때까지 스택에서 연산자 계속 pop
                # () 안의 연산자가 먼저 연산되어야 하기 때문에
                # 꺼내서 쓴다. (식에 먼저 써줘야함)
                while stack:
                    # 연산자 꺼내기
                    op = stack.pop()
                    # 여는 괄호 만나면 중단
                    if op == '(':
                        break

                    # 후위표기식에 써주기
                    postfix += op
            else:
                # i번 글자가 닫는괄호가 아닌 연산자
                # i번 글자의 우선순위를 알아내서 (icp[infix[i]])
                # 스택의 꼭대기에 있는 연산자와 비교 (isp[stack[-1]])
                # icp[infix[i]]랑 isp[stack[-1]]이랑 비교

                # 1. 현재 i번 글자의 연산자의 우선순위 보다
                # 스택의 꼭대기에 있는 우선순위가 같거나 높다면
                # i번 글자보다 우선순위가 같거나 높은 애들은 스택에서 모두 꺼내 쓴다.
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop()

                # 2. 현재 i번 글자의 연산자의 우선순위가
                # 스택의 꼭대기에 있는 우선순위보다 높다면
                # 스택에 push
                stack.append(infix[i])
    # 스택에 연산자가 남아있다면 다 꺼내서 쓰면 된다.
    while stack:
        postfix += stack.pop()
    return postfix

infix = '(6+5*(2-8)/2)'
postfix = get_postfix(infix, len(infix))
print(postfix)


def get_result(postfix):
    # 후위표기식 계산 방법
    # 앞에서부터 쭉 한번만 보면 된다.
    # 숫자를 만나면 스택에 넣고
    # 연산자를 만나면 먼저 나온애 오른쪽, 나중에 나온애 왼쪽 두 개 꺼내서
    # 연산하고 그 결과 다시 스택에 넣기

    stack = []
    for c in postfix:
        # 글자 하나씩 떼어와서 c 라고 하면
        # c가 숫자? 연산자?
        if c not in '+-/*':
            stack.append(int(c))
        else: # 연산자면
            op2 = stack.pop()
            op1 = stack.pop()
            result = 0
            if c == '*':
                result = op1 * op2
            elif c == '/':
                result = op1 / op2  # 연산결과가 실수로 나옴. 문제에서 정수로만 연산하라고 하면 // 쓰거나 int 사용
            elif c == '+':
                result = op1 + op2
            elif c == '-':
                result = op1 - op2
            stack.append(result)

    # 모든 식을 다 확인했다면 스택에 숫자 1개 남아있음 -> 최종 연산 결과
    return stack.pop()

result = get_result(postfix)
print(result)

# 1. 벽인지 아닌지
# 2. 2차원 배열 범위를 벗어나는지
# 3. 이미 갔던 곳인지 아닌지

# dfs로 푸는 방법
# 재귀호출로 푸는 방법

T = int(input())
for tc in range(1, T + 1):
    # 미로의 크기 N
    N = int(input())

    # 미로의 정보
    # 1: 벽(이동불가), 2: 시작지점, 3: 출구지점
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작지점 찾기
    si, sj = 0, 0
    # 행 우선순회로 일단 2차원 배열 순회해서 시작지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    # 행번호, 열번호 입력으로 받음
    def dfs(si, sj):
        visited = [[0] * N for _ in range(N)]
        # visited[5][5] == 1 : 5행 5열 방문한 적 있음

        stack = []
        # 시작지점 방문 체크
        visited[si][sj] = 1

        # 현재 방문중인 위치 i, j
        i, j = si, sj

        while True:
            # 현재 있는 위치가 출구면 반복 중단
            if maze[i][j] == 3:
                # 출구 찾음. 정답 1
                return 1

            # 현재 위치에서 인접한 4방향 탐색
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # (i, j) 위치와 인접한 (ni, nj)위치가 이동 가능한가??
                # 2차원 배열 인덱스 범위 안
                # 방문한적 없어야 함
                # 벽이 아니어야 함
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:  # 조건 순서 지키기
                    # ni, nj 방문체크
                    visited[ni][nj] = 1
                    # 돌아올 위치 기억
                    stack.append((i, j))
                    # ni, nj 이동
                    i, j = ni, nj
                    break

            else:
                # 중간에 break 한적이 없다 => 갈곳을 발견하지 못했다. 이전 방문지점으로 돌아감
                if stack:
                    i, j = stack.pop()
                else:
                    # 스택 비었으면 갈수있는 곳 다 가본거
                    break
        # 반복문 다 돌았는데 return 1 못하면 출구를 찾지 못함
        return 0


    print(f'#{tc} {dfs(si, sj)}')

