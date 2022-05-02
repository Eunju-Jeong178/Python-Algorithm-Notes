n = int(input())
count = 0

for i in range(n+1): # 0~n
  for j in range(60): # 0~59
    for k in range(60): # 0~59
      # ver1) in
      if '3' in str(i)+str(j)+str(k): # 문자열로 찾기
        count += 1
      '''
      # ver2) find()
      time = str(i)+str(j)+str(k)
      if time.find('3') != (-1):
        count += 1
      '''

print(count)

# 하나씩 늘린다 --> for문
# 탐색 in 구문 사용

'''
<오답노트>

3이 있는지 찾을 때
in 을 쓸 생각을 못 함.

리스트 틀을 미리 만들어야 하나 생각했음. 그럴 것 없이 이어붙이면 됨.

시분초 야말로 3중 for문 
'''