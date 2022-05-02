# Greedy
# 문제) 손님에게 거슬러 줘야 하는 동전의 최소 개수를 구하라.
# 가장 큰 화폐 단위부터 거슬러줌

price = 6210
print("물건가격은", price, "입니다.")
paid = int(input("점원에게 돈을 내십시오:"))
change = paid - price

print("거스름돈은", change, "입니다.")

num500 = change // 500
change = change % 500

num100 = change // 100
change = change % 100

num50 = change // 50
change = change % 50

num10 = change // 10

total_change_num = num500 + num100 + num50 + num10

print("500원 동전은", num500, "개 입니다.")
print("100원 동전은", num100, "개 입니다.")
print("50원 동전은", num50, "개 입니다.")
print("10원 동전은", num10, "개 입니다.")
print()
print("거스름돈의 총 동전 개수는", total_change_num, "개 입니다.")