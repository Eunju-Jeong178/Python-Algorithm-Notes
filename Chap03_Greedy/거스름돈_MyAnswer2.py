# Greedy
# 문제) 손님에게 거슬러 줘야 하는 동전의 최소 개수를 구하라.
# 가장 큰 화폐 단위부터 거슬러줌

num_coin = 0
price = 6210
print("물건가격은", price, "입니다.")
paid = int(input("점원에게 돈을 내십시오:"))
change = paid - price

print("거스름돈은", change, "입니다.")

coin_list = [500, 100, 50, 10]

for coin in coin_list:
    num_coin += change // coin
    change %= coin

print("거스름돈의 총 동전 개수는", num_coin, "개 입니다.")