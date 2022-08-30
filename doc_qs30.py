a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
for key,values in list(a.items()):
    # print(key,values,list)
    word=""
for i in (key):
    for j in i:
        if j!=" ":
            word+=j
a[word]=a.pop(key)
print(a)
# for i in a.keys():
#     for k in a.values():
#         word=""
#         for j in i:
#             if j!=" ":
#                 word=word+j
# print(word)
# print(a,i)

    # print(i)