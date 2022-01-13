# coding: utf-8

inputs = input().rstrip().split()

n = int(inputs[0])
c_1 = int(inputs[1])
c_2 = int(inputs[2])

c = 0
pl = 0

for i in range(1, n+1):
    price = int(input().rstrip())

    if i >= n:
        pl += (price * c)
        break

    if c_2 > price and price > c_1:
        # 何もしない
        continue

    if price >= c_2:
        pl += (price * c)
        c = 0

    if c_1 >= price:
        pl -= price
        c += 1

print(pl)
    

# ・株価が c_1 円以下の場合、1 株買う
# ・株価が c_2 円以上の場合、持ち株「を」すべて売る
# ・株価が c_1 円、c_2 円の間の場合は、何もしない
# ・N 日目には、上記を行わず持ち株をすべて売る
