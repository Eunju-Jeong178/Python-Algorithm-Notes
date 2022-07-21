# Answer

# N,M을 공백을 구분하여 입력받기 
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)] # nxm 배열. 전체 맵과 크기가 같음

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x,y,direciton = map(int,input().split())
d[x][y]=1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int,input().split()))) # row 하나씩 입력받음
  # 기존에 map(int,input().split()) 에서 앞에 list만 추가한 것.

# 이런 문제 유형에서의 핵심 풀이 방식
# 북(0), 동(1), 남(2), 서(3) 방향 정의
dx = [-1,0,1,0] # python에서는 list에 ,(comma) 해줘야 한다. 
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1: # 북 --> 서
    direction = 3 # 서쪽은 -1이 아니라 3이다

# 시뮬레이션 시작
count = 1 # 시작할 때 이미 육지 하나를 밟고 있으니까 0이 아니라 1로 시작함
turn_time = 0

while True: # 무한 반복
  # 왼쪽으로 회전
  turn_left() # direction 1감소
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0: # 가보지 않았고, 육지인 경우
    d[nx][ny] = 1 # 이동.
    # 현 위치 변경
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나, 바다인 경우
  else:
    turn_time += 1
    
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
  if array[nx][ny] == 0: # 육지라면
    x = nx 
    y = ny
  # 뒤가 바다로 막혀있는 경우
  else:
    break
  turn_time = 0

# 정답 출력
print(count)
