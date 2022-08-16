# version 1) 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result *= i
    
  return result

# version 2) 재귀적으로 구현한 n!
# 반복적으로 구현하는 것보다 더 간단하다. 
# 수학의 점화식을 그대로 표현
def factorial_recursive(n):
  if n<=1: # n이 1이하인 경우 1을 반환
    return 1 # 결과값으로 1을 내뱉고 종료

  # n! = n*(n-1)! 을 그대로 코드로 작성하기
  return n*factorial_iterative(n-1)


# 각각의 방식으로 구현한 n! 출력 (n = 5)
print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))