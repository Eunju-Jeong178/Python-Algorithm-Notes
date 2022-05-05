import time

# N을 입력받기
n = int(input())
plans = input().split()

start_time = time.time() # 시간측정 시작
x,y = 1,1

# L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1] # x,y를 따로 저장했기 때문
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_type)):
    if plan == move_type[i]:
      nx = x + dx[i] # x,y를 따로 저장했기 때문
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  # 위의 if문에 해당되지 않는 즉, 정사각형 안에 있을 경우 x,y에 반영
  x,y = nx, ny 
  
print(x,y)

end_time = time.time() # 시간측정 종료
print("time:",end_time - start_time) # 수행시간 출력