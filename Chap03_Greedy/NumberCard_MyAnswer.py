n,m = map(int,input().split()) # 행,열

array = [0]*m
row = [0]*m
min_list = []
# 2차원 배열 입력받기
for i in range(n):
  array[i] = list(map(int,input().split()))

# n개의 행 중에서 가장 작은 수 찾기
# 그렇게 찾은 n개의 숫자 중에서 가장 큰 수 찾기, 그 행은 몇 번째?
# 출력
min_list = []

for i in range(n):
  row = array[i]
  row.sort()
  min_list.append(row[0])
  
  
min_list.sort() # 오름차순으로 정렬
print(min_list[n-1]) # 가장 큰 수 출력

# 이렇게 2차원 배열 다 받아온 다음에 한 행씩 접근하는 건 비효율적..