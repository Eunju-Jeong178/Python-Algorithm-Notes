import time

n = int(input())
plan = list(input().split())

start_time = time.time() # 시간측정 시작

position = [1,1]

for i in range(len(plan)):
  if plan[i] == 'L':
    if (position[1]-1) == 0:  # 정사각형 벗어남
      continue # pass 로 해도 되기는 됨: 왜?
    else:
      position[1] -= 1
  elif plan[i] == 'R':
    if (position[1]+1) == (n+1):  # 정사각형 벗어남
      continue
    else:
      position[1] += 1
  elif plan[i] == 'U':
    if (position[0]-1) == 0:  # 정사각형 벗어남
      continue
    else:
      position[0] -= 1
  elif plan[i] == 'D':
    if (position[0]+1) == (n+1):  # 정사각형 벗어남
      continue
    else:
      position[0] += 1

print(position[0], position[1])

end_time = time.time() # 시간측정 종료
print("time:",end_time - start_time) # 수행시간 출력