array = [('banana',2),('apple',5),('carrot',3)]

def setting(data):
  return data[1]
  # return data[1] # 이걸로 하면 알파벳 순으로 정렬

result = sorted(array, key=setting)
print(result)
