# 그래프를 표현하는 2가지 방법 중 하나 
# (인접행렬 Adjacency Matrix / 인접 리스트 Adjacency List)

INF = 999999999 # 무한의 비용 선언. 서로 연결되지 않았을 때. 987654321 로 하기도 한다.

# 2차원 리스트를 이용해 인접행렬 표현
graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)