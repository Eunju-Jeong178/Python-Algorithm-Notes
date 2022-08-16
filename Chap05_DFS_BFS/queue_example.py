from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

'''
Queue(큐)를 구현할 때 list 사용하면 시간복잡도가 커진다.
(name_of_list.append(), name_of_list.pop)
(https://frhyme.github.io/python-lib/python_deque_is_faster_than_lst/)
'''

# 삽입(5) 삽입(2) 삽입(3) 삽입(7) 삭제() 삽입(4) 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력

queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력