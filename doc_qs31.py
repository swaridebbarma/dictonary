n={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
m=0
sm=0
tm=0
key_m=0
key_sm=0
key_tm=0
for i in n:
    if n[i]>m:
        m=n[i]
        key_m=i
# print(m)
for j in n:
    if n[j]>sm and n[j]<m:
        sm=n[j]
        key_sm=j
# print(sm)
for k in n:
    if n[k]>tm and n[k]<sm:
        tm=n[k]
        key_tm=k
print(key_m,m)
print(key_sm,sm)
print(key_tm,tm)
# 31 no
