n,k = map(int,input().split())

result = 0 # 시행 횟수

while True:
  if (n%k)!=0: # 나누어 떨어지지 않을 때
    if n == 1:
      break
    n -= 1
    result += 1
    
  else: # 나누어 떨어질 때
    if n == 1:
      break
    n = n//k
    result += 1
    
print(result) 