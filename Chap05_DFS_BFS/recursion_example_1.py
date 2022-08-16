def recursive_function(i):
  # 10번 째 출력했을 때 종료되도록 종료 조건 명시
  if i == 10:
    return # 종료
    
  print(i,'번 째 재귀함수에서',i+1,'번 째 재귀함수를 호출합니다.')
  recursive_function(i+1) # 자기 자신 호출
  #print(i,'번 째 재귀함수를 종료합니다.')

recursive_function(1)

'''
재귀 함수 구조

def recursive_function():
  종료 조건

  반복할 것
  recursive_function() #자기 자신 호출

recursive_function() # 실행
'''