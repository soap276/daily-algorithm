# 분할 정복
# 해결할 문제를 여러 개의 작은 부분으로 나눔 -> 나눈 작은 문제를 각각 해결 -> 해결된 해답을 모음


# 2. 병합하는 과정 (이때, 정렬하면서 병합)
# 왼쪽, 오른쪽 리스트 중 작은 원소부터 정답 리스트에 추가하자
def merge(left, right):
    # 두 리스트를 합한 크기만큼 나온다
    result = [0] * (len(left)+len(right))
    l = r = 0 # 현재 바라보고 있는 인덱스

    # 두 리스트에서 비교할 대상이 남을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1
   # 남은 데이터들을 모두 result에 추가
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1
    return result

# 1. 분할하는 과정
# depth: 리스트의 길이가 1이 되면 끝
# branch: 왼쪽과 오른쪽으로 리스트를 분할 (2개)
def merge_sort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid] # 왼쪽 절반 리스트
    right = li[mid:] # 오른쪽 절반 리스트
    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merge_list = merge(left_list, right_list)
    return merge_list


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# 이진검색
arr = [7, 4, 2, 9, 11, 23, 19]
# 반드시 이진 검색은 정렬이 되어있어야 함
arr.sort()

def binary_search_while(target):
    left = 0 # 검색 시작점
    right = len(arr) - 1 # 검색 끝점

    while left <= right: # 교차가 되는 순간이 탐색 못하는 순간
        mid = (left+right) // 2
        # 정답을 찾으면 종료
        if arr[mid] == target:
            return mid
        # arr[mid]가 target보다 더 큰 경우 (target이 왼쪽에 위치)
        # - 왼쪽을 탐색
        if target < arr[mid]:
            right = mid-1
        # arr[mid]가 target보다 작은 경우 (target이 오른쪽에 위치)
        # 오른쪽을 탐색
        else:
            left = mid+1
    return -1

print(f'9 = {binary_search_while(9)}번째 위치')


# 강사님 코드
# 퀵 정렬
# A : 정렬할 배열
# l, r: 정렬배열의 시작 인덱스, 종료 인덱스
def quicksort(A, l, r):
    if l < r:
        # 기준원소를 정해서 기준원소(피벗)의 위치를 확정
        p = partition(A, l, r)
        # 기준원소(피벗)의 왼쪽을 다시 퀵정렬
        quicksort(A, l, p-1)
        # 기준원소(피벗)의 오른쪽을 다시 퀵정렬
        quicksort(A, p+1, r)


def partition(A, l, r):
    # l ~ r 이 부분을 파티셔닝
    # 기준원소(피벗)을 하나 정하자. => 가장 왼쪽에 있는 친구
    p = A[l]

    # p보다 작은애는 왼쪽으로
    # p보다 큰애는 오른쪽으로

    # 왼쪽에서 p보다 큰 애를 찾고 오른쪽에서 p보다 작은 애를 찾아
    # 자리를 서로 교환시키자

    # i는 왼쪽에서 시작해서 큰 애를 찾을때까리 오른쪽으로 간다
    i = l
    # j는 오른쪽에서 시작해서 작은애를 찾을때까지 왼쪽으로 간다
    j = r

    # i와 j가 교차하기 전까지 찾아라
    while i <= j:
        # i는 왼쪽에서 +1
        while i <= j and A[i] <= p:
            i += 1

        # j는 오른쪽에서 -1
        while i <= j and A[j] >= p:
            j -= 1

        # 위에있는 두개의 while 이 끝나고 나서
        # 여전히 i가 j보다 작으면
        # 잘못된 위치에 있는 원소를 찾은거다 => 자리교환
        if i < j:
            A[i], A[j] = A[j], A[i]

    # i와 j가 교차하면 반복 종료
    # 왼쪽 부분에는 p보다 작은애들이 모여있고 (정렬x)
    # 오른쪽 부분에는 p보다 큰 애들이 보여있는 (정렬X) 상태

    # 왼쪽 부분과 오른쪽 부분의 경계에 p를 꽂아주면 완료
    # i와 j가 교차하면 i는 큰 원소들의 인덱스, j는 작은 원소들의 인덱스
    # p는 누구랑 자리를 바꿔야 하나? p는 가장 왼쪽, 작은 부분에 속해있었으므로 j랑 바꿔야 한다
    A[l], A[j] = A[j], A[l]

    # 기준원소의 자리는 j로 확정 (FIX)
    return j


arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

# 정렬할 범위 지정
def merge_sort(start, end):
    if start == end-1:
        return start, end

    mid = (start + end) // 2
    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    merge(left_s, left_e, right_s, right_e)
    return start, end # 정렬할 범위 리턴턴

# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    l = left_s
    r = right_s
    N = right_e - left_s
    result = [0] * N
    # result 배열에 들어갈 원소의 다름 자리 (작은 순서)
    idx = 0
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    for i in range(N):
        arr[left_s + i] = result[i]






arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)


# 병합정렬 함수
# 정렬할 범위를 지정(인덱스)
# 시작(start) ~ 종료(end)
def merge_sort(start, end):
    # 1. 종료 조건
    # 원소가 하나 남았을때
    # 더이상 분할이 불가능함
    if start == end - 1:
        return start, end

    # 2. 재귀 호출
    # 두 부분으로 나누고
    # 합칠때 정렬이 이루어진다.
    # 두 두분으로 나누는 기준은 가운데
    mid = (start + end) // 2

    # 왼쪽부분 다시 분할후 정렬
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽부분 다시 분할후 정렬
    right_s, right_e = merge_sort(mid, end)

    # 합치면 된다.
    merge(left_s, left_e, right_s, right_e)
    # 정렬된 범위 리턴
    return start, end


# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    # 왼쪽부분의 가장 작은 원소가 있는 인덱스
    l = left_s
    # 오른쪽부분의 가장 작은 원소가 있는 인덱스
    r = right_s

    # 왼쪽 부분과 오른쪽 부분을 합친 결과의 길이 N
    N = right_e - left_s
    result = [0] * N

    # result배열에 들어갈 원소의 다음 자리(작은 순서)
    idx = 0

    # 병합시작 (병합을 하면서 정렬이 된다)

    # 왼쪽 부분과 오른쪽 부분이 둘다 남아 있는경우
    # 왼쪽 부분의 최소값 vs 오른쪽 부분의 최소값 비교
    # 둘중에 작은거 선택해서 result의 idx 위치에 넣기
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            # 왼쪽부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            # 오른쪽부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[r]
            r += 1
            idx += 1

    # 둘중 한 부분에만 원소가 남아있는 경우
    # 남아있는 원소 주루룩 추가

    # 오른쪽만 남은 경우
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 왼쪽만 남은 경우
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # result 안에는 left_s 에서 right_e 까지의 원소들이
    # 오름차순으로 정렬이 되어있고, 이 부분을 원본 arr 에 반영
    for i in range(N):
        arr[left_s + i] = result[i]

    print(result)


merge_sort(0, N)

print(arr)


