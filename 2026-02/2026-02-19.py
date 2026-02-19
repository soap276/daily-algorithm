## 강사님 코드
# 트리만들기 1

# 마지막 노드 V, 간선의 개수 N
V, N = map(int, input().split())
# 트리의 정보가 한줄 입력으로 들어온다.
tree = list(map(int, input().split()))
# 5 4
# 1 2 1 3 3 4 3 5
# 1-2/1-3/3-4/3-5

# 부모 노드 번호를 인덱스로 저장하는 방법
cleft = [0] * (V + 1)
cright = [0] * (V + 1)
# cleft[4] = 4번 노드의 왼쪽 자식 번호
# cright[1] = 1번 노드의 오른쪽 자식 번호

# 한줄 입력을 간선 개수만큼 자른다.
for i in range(N):
    # 부모 번호
    p = tree[2 * i]
    # 자식번호
    c = tree[2 * i + 1]

    # p의 자식은 c번이다.
    # 이진트리에서 자식은 왼쪽? 오른쪽?
    # 먼저 왼쪽 자식이 있나 확인
    # p번노드의 왼쪽 자식이 없다면
    if cleft[p] == 0:
        # 왼쪽자식으로 c 넣기
        cleft[p] = c
    # p번 노드의 왼쪽 자식이 있었다면
    else:
        cright[p] = c

print(cleft)
print(cright)




# 마지막 노드 V, 간선의 개수 N
V, N = map(int, input().split())
# 트리의 정보가 한줄 입력으로 들어온다.
tree = list(map(int, input().split()))

# 자식 번호를 인덱스로 부모 번호를 저장
parent = [0] * (V+1)
# parent[2] = 2번 자식의 부모 노드 번호
# parent[4] = 4번 자식의 부모 노드 번호
# x번 노드의 부모 노드 번호를 알고싶어요 = parent[x]
for i in range(N):
    # 부모 번호
    p = tree[2 * i]
    # 자식번호
    c = tree[2 * i + 1]
    # c번 노드의 부모 노드 번호는 p번이다.
    parent[c] = p

print(parent)

# 5번 노드의 조상 노드 모두 찾고 싶음
child = 5

ancestor = []

while parent[child] != 0:
    # child의 부모 노드가 0이 아니다 -> child는 루트노드가 아니다
    # child의 부모 위로 한 칸 올라가 본다.
    child = parent[child]
    # 이 노드는 부모로드니까 조상 목록에 추가
    ancestor.append(child)
# 어느 순간 child의 부모 번호가 0번이 된다. == child는 루트 노드다
root = child
print(root, ancestor)

## 순회
# 트리의 각 노드를 중복되지 않게 전부 방문하는 것
# 전위순회 : 부모노드 방문 후 자식 노드를 좌, 우 순서로 방문 (현재노드 방문 처리 -> 현재노드의 왼쪽 서브트리 이동 -> 오른쪽 서브트리 이동)
# 중위 순회: 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순 (왼쪽 서브트리 -> 현재노드 -> 오른쪽 서브트리)
# 후위 순회: 자식 노드를 좌, 우 순서로 방문한 후 부모노드로 방문 (왼쪽 서브트리 -> 오른쪽 서브트리 -> 현재노드)


def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
    if T:   # 0이 아니면 (존재하는 정점이면)
        print(T)    # visit(T) T에서 할일 처리
        pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동

def in_order(T):
    if T:   # 0이 아니면 (존재하는 정점이면)
        in_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        print(T)  # visit(T) T에서 할일 처리
        in_order(right[T]) # 오른쪽 자식(서브트리)로 이동

def post_order(T):
    if T:   # 0이 아니면 (존재하는 정점이면)
        post_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        post_order(right[T]) # 오른쪽 자식(서브트리)로 이동
        print(T)  # visit(T) T에서 할일 처리


## 서브트리 문제
T = int(input())
for tc in range(1, T+1):
    # 간선의 개수 E개(노드의 개수는 E+1개), N은 시작 노드 번호
    E, N = map(int, input().split())

    cleft = [0] * (E+2)
    cright = [0] * (E+2)

    edges = list(map(int, input().split()))
    # 간선의 개수만큼 잘라냄
    for i in range(E):
        # 부모노드 번호 = 짝수
        p = edges[i*2]
        # 자식노드 번호 = 홀수
        c = edges[i*2+1]

        # p번 노드의 왼쪽자식이 없으면 왼쪽부터
        if cleft[p] == 0:
            cleft[p] = c
        # 있으면 오른쪽
        else:
            cright[p] = c

    # 문제에서 원하는 답 = N번 노드에서 순회 시작시 노드의 개수
    count = 0
    # t를 루트로 하는 서브트리 전위순회
    def preorder(t):
        global count
        # t번 노드가 존재하면
        if t != 0:
        # t번 처리
            count += 1
            # t번 왼쪽 서브트리 전위순회
            preorder(cleft[t])
            # t번 오른쪽 서브트이 전위순회
            preorder(cright[t])

    preorder(N)
    print(f'#{tc} {count}')


