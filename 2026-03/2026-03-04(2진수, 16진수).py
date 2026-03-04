## 1
decimal = 149

# 십진수를 이진수로 바꾼 결과
binary = 0

# 2로 나눈 몫이 2보다 작아질 때까지 계속 나눈다
# 나머지를 거꾸로 읽으면 이진수 완성

# 중간 나눗셈에서 나머지를 기억할 배열
arr = []

while decimal != 0:
    arr.append(decimal%2)
    # 다음에 나눌 숫자는 2로 나눈 몫
    decimal //= 2

arr.reverse()
print(*arr)

## 2

# 비트연산자
def bit_print(dec):
    # dec을 2진수로 만든 결과
    output = ""

    for i in range(7, -1, -1):
        if dec & (1 << i):
            output += "1"
        else:
            output += "0"
    return output

print(bit_print(149))

## 3

bit = "00000010001101"

# 이진수를 7칸씩 쪼개서 쪼갠 것들 각각 십진수로 바꾸기
N = len(bit)

# 길이가 14
# 0~6
# 7~13
for i in range(0, N, 7):
    # i번 비트에서 7칸 잘라서 십진수로 만들고 출력
    decimal = 0
    ith_bin = bit[i:i+7]
    # ex) bin = 0000001
    # decimal += bin[6] * 2**0
    # decimal += bin[5] * 2**1
    # decimal += bin[4] * 2**2
    # ..
    # decimal += bin[0] * 2**6
    for j in range(6, -1, -1):
        decimal += int(ith_bin[j]) * (2**(6-j))
    print(decimal, ",")



## 4

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "E": "1110",
    "F": "1111"
}

hex = "47FE"

result = ""
for i in range(4):
    result += hex_to_bin[hex[i]]

print(result)


result2 = ""
for c in hex:
    # c를 숫자로 바꾸고
    dec = int(c, 16)

    result_bin = ""

    # 2진수 * 4
    for i in range(3, -1, -1):
        result_bin += "1" if dec & (1<<i) else "0"

    result2 += result_bin
print(result2)



T = int(input())

for tc in range(1, T+1):
    N, hex= input().split()
    N = int(N)
    print(hex)

    result2 = ""
    for c in hex:
        # c를 숫자로 바꾸고
        dec = int(c, 16)

        result_bin = ""

        # 2진수 * 4
        for i in range(3, -1, -1):
            result_bin += "1" if dec & (1 << i) else "0"

        result2 += result_bin
    print(f'#{tc} {result2}')


    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    result = ""
    for i in range(len(hex)):
        result += hex_to_bin[hex[i]]

    print(f'#{tc} {result}')




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()

    # 몇번 회전할건지, 한 변에 몇 개의 원소가 있는지
    rota = N // 4
    # 회전 별로 나올 수 있는 수들 넣을 리스트 생성
    result = []

    for _ in range(rota):

        for i in range(0, N, rota):
            # 리스트 슬라이스 진행
            piece = num[i:i+rota]
            # 16진수 10진수로 변환
            val = int(piece, 16)
            # 중복이 아닌 것만 result에 넣기
            if val not in result:
                result.append(val)

        # 맨 앞의 원소 리스트 맨 뒤로 넣기 -> 회전
        num = num[1:] + num[0]
        # data = num.pop(0)
        # num.append(data)
    # 내림차순 정렬
    result.sort(reverse=True)
    # print(result)
    print(f'#{tc} {result[K-1]}')
