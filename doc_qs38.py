dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
print("Original Dictionary:")
print(dict1)
print("New Dictionary after dropping empty items:")
dict2 = {}
for i,j in dict1.items():
    # print(j)
    if j is not None:
        dict2[i] = dict1[i]
print(dict2)
# 38 no