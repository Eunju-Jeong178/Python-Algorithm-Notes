# 성적이 낮은 순서로 학생 출력하기

num_student = int(input())

student_info = []

for i in range(num_student):
  input_data = input().split()
  student_info.append((input_data[0], int(input_data[1])))

def key_sort(data):
  return data[1]

result = sorted(student_info, key = key_sort)

for i in range(num_student):
  print(result[i][0], end= ' ')


