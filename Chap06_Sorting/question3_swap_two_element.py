n,k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


A = sorted(A)
B = sorted(B, reverse = True)
'''
A.sort()
B.sort(reverse=True)
'''

for i in range(k):
  if A[i] < B[i]:
    A[i],B[i] = B[i],A[i]
  else:
    break # for 반복문 탈출

print(sum(A))