## 스택
- LIFO: 가장 마지막에 넣은 자료가 가장 먼저 나오는 것
- top: 스택 포인터, 스택에서 마지막 삽입된 원소의 위치

# push 연산
- append 메소드를 통해 리스트의 마지막에 데이터를 삽입
s = []
def my_push(item):
    s.append((item))

- 인덱스 연산을 활용한 구현
def my_push(item, size):
    global top
    top += 1
    if top == size:
        print('Overflow!')
    else:
        stack[top] = item

- 단순한 Push 연산
size = 10
stack = [0] * size
top = -1

my_push(10, size) # my_push 함수를 이용
top += 1
stack[top] = 20

- pop 연산
def my_pop():
    if len(s) == 0:
        print('Underflow!')
        return
    else:
        return s.pop() # 리스트 s의 마지막 원소 삭제

- 인덱스 연산을 이용한 pop 연산
def my_pop():
    global top
    if top == -1:
        print('Underflow')
        return 0
    else:
        top = -1
        return stack[top+1]
print(my_pop())

if top > -1: # pop()
    top -= 1
    print(stack[top+1])

- 간단한 스택
st = []
st.append(1) # push 1
st.append(2)
st.append(3)
print(st.pop())
print(st.pop())
print(st.pop())

- stack을 이용한 괄호 검사
# 괄호가 아니면 버림
# 여는 괄호 -> push
# 닫는 괄호 -> stack에 남은 여는 괄호가 있으면 pop
# 괄호 수식이 끝났는데 스택에 괄호가 남아있으면 오류
# 닫는 괄호인데 스택이 남아있지 않으면 오류
txt = input()
# 스택 생성
top = -1
stack = [0] * 100 # 입력최대 길이
ans = 'ok'
for x in txt:
    if x == '(':
        top += 1
        stack[top] = '('

    elif x == ')':
        if top == -1: # 여는 괄호가 없으면 오류
            print('ERROR')
            break # for x
        else: # 여는 괄호가 있으면 pop
            top -= 1
            # 괄호가 여러종류면 이 부분에서 비교
            # if stack[top+1] == '(' and ')':
            #     continue
            # elif stack[top+1] == '{' and x ==
if top != -1:
    ans = 'ERROR'

# 스택 초기화 (선언)
# 내가 빈리스트를 스택으로 사용하겠다.
stack = []

# 스택에 자료를 추가하는 방법
for i in range(10):
    stack.append(i)

print(stack)

# 스택에서 자료를 삭제하는 방법
# 자료를 삭제하면 ==> 가장 최근에 저장한 자료가 튀어나온다.
for i in range(10):
    element = stack.pop()
    print(element, end = ',')
print()

# 스택안에 몇개가 있는지 모른다.
# 근데 다 꺼내서 확인하고 싶다면 어떻게?
# 빈리스트는 False 로 취급된다는 걸 활용
while stack:
    element = stack.pop()
    print(element, end = ',')
print()
print(stack)

# top이라는 키워드와 (크기가 고정된)배열을 활용한 스택

# 스택 초기화(선언)
# top: 스택에 마지막으로 삽입된 자료의 위치(인덱스)를 나타냄
top = -1
# N: 스택의 크기
N = 10
# 리스트로 스택을 만들기
stack = [0] * N

# 스택에 자료 삽입하기
for i in range(1, 11):
    top += 1
    stack[top] = i
# 스택에 자료를 추가하기 전에 스택이 꽉 찼나 확인
if top < N-1:
    # 넣을 수 있다면 추가
    top += 1
    stack[top] = 11
else:
    # 스택에 더이상 원소를 넣을 수 없음
    print('overflow')

print(stack, top)

# 스택에서 자료 삭제
for i in range(10):
    element = stack[top]
    top -= 1
    print(element, end=',')
print()

print(stack[top], top)
# 뭔가 남아있어도 우리는 이 스택이 이제 비었다고 판단. 왜? top이 -1 이니까..
print(stack)

# 굳이 함수 쓰지 않고 리스트에 append 사용해서 스택 구현 가능

# 스택을 이용한 괄호 검사
