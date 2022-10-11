import time

array = [7,5,9,0,3,1,6,2,4,8] # N개

start_time = time.time() # 시간측정 시작

for i in range(len(array)): # N번 수행 (index 0부터 N-1까지)
  min_index = i # 가장 작은 원소의 인덱스
  
  # i번째 인덱스와 하나하나 비교하여 가장 작은 수의 인덱스 찾기
  for j in range(i+1, len(array)): # (index i+1부터 N-1까지)
    if array[min_index] > array[j]: # 오름차순 정렬
    # if array[min_index] < array[j]: # 이렇게하면 내림차순 정렬
      min_index = j
  array[i],array[min_index] = array[min_index],array[i] # swap 파이썬은 이게 가능

end_time = time.time() # 시간측정 종료
print("선택정렬 성능측정(sec):",end_time - start_time) # 수행시간 출력
print(array)