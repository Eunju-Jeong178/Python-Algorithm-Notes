# 문제) 손님에게 거슬러 줘야 하는 동전의 최소 개수를 구하라.

# 가장 큰 화폐 단위부터 거슬러줌
# Time Complexity = O(K)

# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
# 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.
# 따라서 가장 큰 화폐단위부터 거슬러주면 항상 최적의 해를 보장할 수 있다. 

n = 1260  # change
count = 0  # initialization

# Check in order of large coin units (greedy)
list = [500, 100, 50, 10]  # K (the number of coin)

for coin in list:
    count = count + n // coin  # count += count + n
    n = n % coin  # n %= coin

print(count)