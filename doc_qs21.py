a=[
    {"V":"S001"},
    {"V": "S002"}, 
    {"VI": "S001"},
    {"VI": "S005"}, 
    {"VII":"S005"}, 
    {"V":"S009"},
    {"VIII":"S007"}
]
b=[]
for i in a:
    for j in i:
        if i[j] not in b:
            # b.append(i)
            b.append(i[j]) 
            # m=sorted(b)         
print(b)


a=[
    {"V":"S001"},
    {"V": "S002"}, 
    {"VI": "S001"},
    {"VI": "S005"}, 
    {"VII":"S005"}, 
    {"V":"S009"},
    {"VIII":"S007"}
]
b=[]
for i in a:
    for j in i.values():
            b.append(j)
print(set(b))
for i in a:
    for j in i.values():
            b.append(j)
for i in a:
    for j in i.values():
            b.append(j)
for i in a:
    for j in i.values():
            b.append(j)
for i in a:
    for j in i.values():
            b.append(j)
print(b)