N, M, K = map(int, input().split())
if K>M:
  print("다시 입력하세요.")
  N,M,K = list(map(int, input().split()))

N_list = list(map(int, input().split()))
if len(N_list) != N:
  print("다시 입력하세요.")
  N_list = list(map(int, input().split()))

# 가장 큰 수가 무엇인지, 그리고 index가 몇 인지 알아야 함
# 받아온 자연수 리스트를 내림차순으로 정리
# 가장 큰 수와 그 다음으로 큰 수만 번갈아가면서 더하면 됨
N_list.sort(reverse=True) 
first_big = N_list[0]  
second_big = N_list[1]  

sum = 0

# 반복되는 계산:
# first_big을 K번 더하고, second_big을 1번 더함
# 종료조건:
# M 이 다 채워지면 종료

while True:

    for i in range(K):
        if M == 0:
            break
        sum += first_big
        M -= 1

    if M == 0:
        break
    sum += second_big
    M -= 1

print(sum)