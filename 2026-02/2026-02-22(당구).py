import math

# 두 점 사이의 거리 계산
def calcul_distance(x, y):
    dx = y[0] - x[0]
    dy = y[1] - x[1]
    return math.sqrt(dx**2 + dy**2)

# 두 점 사이의 각도 계산
def calcul_angel(x, y):
    # math.atan2 함수는 두 점 사이의 y좌표 차이와 x좌표 차이를 이용하여
    # 각도를 라디안 단위로 반환합니다. (y[1] - x[1]): y좌표 차이, (y[0] - x[0]): x좌표 차이
    return math.atan2(y[1]-x[1], y[0]-x[0])

# 목표구에서 각 홀까지의 각도 계산
def calcul_dis_angs(target, holes):
    # 목표구에서 각 홀까지의 거리 계산
    dis_to_holes = [calcul_distance(target, hole) for hole in holes]
    # 목표구에서 각 홀까지의 각도 계산
    angels_to_holes = [calcul_angel(target, hole) for hole in holes]
    return dis_to_holes, angels_to_holes

# 가장 가까운 홀을 찾는 함수
def best_hole(dis_to_holes, angels_to_holes):
    # 가장 짧은 거리의 홀의 인덱스
    best_hole_idx = dis_to_holes.index(min(dis_to_holes))
    # 가장 가까운 홀의 인덱스와 각도 반환
    return best_hole_idx, angels_to_holes[best_hole_idx]

# 내 공의 위치(임의의 위치로 설정됨)
myball = [127, 63.5]
# 목표구의 위치(임의의 위치로 설정됨)
target = [150, 90]
# myball = balls[0]
# target = balls[target_idx]  # 선/후공 규칙에 맞춰 선택


# 홀의 위치 (전체 테이블상의 위치를 약간 이동시켜 조정함)
# holes = [[0 , 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
# 홀 잡아당기기
r = 5.73 # 공의 직격
rr = 5.73 / 2
const = 0.3 # 상수 값
k = r * const # 공의 크기와 상수를 곱하여 오프셋을 계산
holes = [[0+k , 0+k],  # 왼쪽 아래 홀
         [127, 0+k/2], # 가운데 아래 홀
         [254-k, 0+k], # 오른쪽 아래 홀
         [0+k, 127-k], # 왼쪽 위 홀
         [127, 127-k/2], # 가운데 위 홀
         [254-k, 127-k]  # 오른쪽 위 홀
         ]

# 목표구에서 각 홀까지의 거리와 각도 계산
dis_to_holes, angels_to_holes = calcul_dis_angs(target, holes)

# 가장 가까운 홀을 선택 (가장 짧은 거리를 가지는 홀)
best_idx, ang_th = best_hole(dis_to_holes, angels_to_holes)


# ✅ 고스트볼(접점) = 목표구에서 "홀 반대방향으로 직경(=2R)" 이동
d = dis_to_holes[best_idx]
if d == 0:
    ghost = target[:]  # 예외
else:
    ux = (holes[best_idx][0] - target[0]) / d
    uy = (holes[best_idx][1] - target[1]) / d
    ghost = [
        target[0] - ux * r,
        target[1] - uy * r
    ]

# 내 공 -> 고스트볼 각도(라디안)
ang_wg = calcul_angel(myball, ghost)

# 일타싸피 각도(0도=위, 90도=오른쪽)로 변환
deg = math.degrees(ang_wg)   # 수학: 0도=오른쪽
# angle = 90 - deg
angle = (90 - deg) % 360
if angle < 0:
    angle += 360

# power
dist_wg = calcul_distance(myball, ghost)
power = max(25, min(100, (dist_wg + d) * 0.35))

# # 공의 반지름을 고려해 목표구의 접점까지의 각도를 계산
# # offset은 목표구와 홀 사이의 각도에 추가될 각도
# offset = math.atan2(r/2, dis_to_holes[best_hole_idx])

# # 목표구와 홀 사이의 각도에 오프셋을 추가하여 최종 목표 각도를 계산
# target_angel = best_hole_angle + offset

# # 내 공을 맞출 접점의 위치
# final_pos =[
#     target[0] - math.cos(target_angel) * (r/2),
#     target[1] - math.cos(target_angel) * (r/2)
# ]
# # 내 공과 목표구의 접점 사이의 각도를 계산
# final_angel = math.degrees(calcul_angel(myball, final_pos))
# # 타격력 (임의로 설정된 값)
# power = 100
