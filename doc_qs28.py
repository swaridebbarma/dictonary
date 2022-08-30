list = [1, 2, 3, 4]
new = current = {}
for i in list:
    current[i] = {}
    current = current[i]
print(new)
# 28 no

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)