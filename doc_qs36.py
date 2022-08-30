x= {'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
for k,v in x.items():
    if k in y and x[k]==y[k]:
        print(k,":",v, "is present in both x and y")
# 36 no

a= {'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
for i,j in a.items():
    for i,j in b.items():
        if a[i]==b[i]:
            print(i,":",j, "is present in both a and b")