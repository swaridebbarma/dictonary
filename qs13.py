n = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
}
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
print(key_m)
print(key_sm)
print(key_tm)
