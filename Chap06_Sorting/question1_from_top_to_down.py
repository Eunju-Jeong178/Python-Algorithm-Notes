n = int(input())

data = []
# 엔터로 구분된 여러개의 숫자 입력값을 리스트로 받기
for i in range(n):
  data.append(int(input()))


data.sort()
data.reverse()

'''
data = sorted(data, reverse = True)
'''

# 정렬이 수행된 결과 출력
for i in range(len(data)):
  print(data[i], end= ' ')

'''
for i in data:
  print(i, end=' ')
'''