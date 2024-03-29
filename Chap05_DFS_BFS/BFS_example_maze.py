from collections import deque

# N,M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque() 
  queue.append((x,y)) # queue에 현위치 넣어둠  <-- BFS 필수
  # 참고로, queue = deque((x,y)) 로 한번에 할 수도 있음

  # 큐가 빌 때까지 반복
  while queue:
    x,y = queue.popleft() # queue에서 하나씩 꺼냄  <-- BFS 필수

    # 현위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i] # next x
      ny = y + dy[i] # next y
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단거리 기록  <-- BFS 필수
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1 # 방문처리  <-- BFS 필수
        queue.append((nx,ny)) # 큐에 삽입 <-- BFS 필수
  # 가장 오른쪽 아래까지(출구위치)까지의 최단 거리 반환
  return graph[n-1][m-1]

  # BFS 수행한 결과 출력
  print(bfs(0,0))