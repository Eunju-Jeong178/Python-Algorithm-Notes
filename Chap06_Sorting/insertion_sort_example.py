import time

array = [7,5,9,0,3,1,6,2,4,8]

start_time = time.time() # 시작 시간 측정

# 삽입정렬(Insertion Sort algorithm)
for i in range(1, len(array)): # 두 번째 칸(인덱스 1)부터 시작
  for j in range(i,0,-1): # 비교 시작하는 수의 왼쪽에 있는 수들 하나씩 반복 비교
    if array[j] < array[j-1]: # 왼쪽 데이터보다 작으면
      array[j],array[j-1] = array[j-1],array[j] # swap
    else: # 자기보다 큰 데이터를 만나면 그 위치에서 멈춤
      break # 더이상 비교하지 않고 멈춤 (왼쪽은 모두 정렬되어 있다고 가정하기 때문)
      # break를 쓰면 반복문 전체를 빠져나옴
      # continue를 쓰면 해당 조건만 건너뜀

  
end_time = time.time() # 종료 시간 측정
print("삽입 정렬 성능 측정:",end_time - start_time)
print(array)