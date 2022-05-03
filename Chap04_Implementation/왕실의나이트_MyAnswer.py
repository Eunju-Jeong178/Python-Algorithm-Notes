import time

# 현재 나이트의 위치 입력받기
position = input() # input().split() 하면 안 됨. position[0] = a1 이렇게 하나로 인식함

start_time = time.time() # 시간측정 시작

# 현재 위치인 row, col 정의
row = int(position[1])

if position[0] == 'a':
  col = 1
elif position[0] == 'b':
  col = 2
elif position[0] == 'c':
  col = 3
elif position[0] == 'd':
  col = 4
elif position[0] == 'e':
  col = 5
elif position[0] == 'f':
  col = 6
elif position[0] == 'g':
  col = 7
elif position[0] == 'h':
  col = 8
'''
위의 조건문은 아래의 한 줄로 대체 가능 : ord('a') --> 정수 97 반환

col = int(ord(position[0]) - ord('a')) + 1 # a,b...,h 모두 정수 1 차이
'''

# 나이트가 이동할 수 있는 8가지 방향 정의 [step_row, step_col]
steps = [
  [-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]
]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
'''
반복문 idea)
수평 두 칸, 수직 한 칸 또는 수직 두 칸, 수평 한 칸 중에서 하나라도 8x8 칸에서 벗어나면
count 하지 않음. 
즉, 모두 성립해야만 count 함 --> and 를 써서 모두 성립하는 경우만 count += 1을 하자.
'''
count = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  if next_row >=1 and next_row <=8 and next_col >=1 and next_col <= 8:
    count += 1

print(count)

end_time = time.time() # 시간측정 종료
print("time:",end_time - start_time) # 수행시간 출력