
n,m = map(int,input().split()) # 맵의 세로, 가로 크기 입력
a,b,d = map(int,input().split()) # 캐릭터가 서 있는 위치, 보는 방향

map_nxm = []
for i in range(n):
  # map_nxm[i-1] = list(input()) # 오답
   map_nxm.append(list(map(int,input().split()))) # nxm 2차원 배열 생성, list를 append함.

print(map_nxm)