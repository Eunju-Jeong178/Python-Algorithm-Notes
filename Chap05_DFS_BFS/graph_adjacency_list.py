# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]
# 행1: 노드 0과 연결 
# 행2: 노드 1과 연결
# 행3: 노드 2와 연결

'''
#참고
#n*m 크기의 2차원 리스트 초기화
array = [[0]*m for _ in range(n)]
'''

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0,5))

print(graph)