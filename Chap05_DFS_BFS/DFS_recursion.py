'''
https://pythontutor.com/render.html#mode=display
에서 시각적으로 확인하기
'''

# DFS 메서드 정의
def dfs(graph, v, visited): 
  # 연결 리스트 형태의 그래프, 노드 번호, 방문 정보

  # 현재 노드를 방문 처리 (dfs 함수를 실행했을 때 실행하는 것, 즉 반복할 명령어)
  visited[v] = True # 노드 방문 처리
  print(v, end = ' ') # 출력

  # 현재 노드와 연결된 다른 노드(인접노드)를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]: # False 이면 실행. 즉, 방문하지 않은 인접노드
      dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형 (인접리스트) 으로 표현 (2차원 리스트)
# 일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다. 
graph = [
  [], # graph[index]와 노드 # 가 같도록 하기 위함 (index == #)
  [2,3,8], # graph[1] 노드 1과 인접한 노드들 (인접노드), 관행적으로 노드 번호가 낮은 것 부터 적는다.
  [1,7], # graph[2] 노드 2와 인접한 노드들 (인접노드)
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited) # 노드 1번부터 방문 시작
