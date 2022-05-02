n,m = map(int, input().split()) # 공백으로 구분하여 입력받기 (행, 열)

result = 0 # 당연히 넘을만한 작은 수

for i in range(n):
  data = list(map(int, input.split())) # 한 행씩 받아오기
  min_value = min(data) # 현재 행에서 '가장 작은 값' 찾기
  result = max(result, min_value)  
  # idea) 반복되는 동안 '가장 작은 값'들 중에서 가장 큰 값 찾기

print(result)

'''
min_value = min(data) 는 다음과 같이 구현가능

min_value = 1001 # 넘을리 없는 큰 수
for a in data: # data 에서 하나씩 꺼내서
  min_value = min(min_value, a) # 가장 작은 값 찾기

'''