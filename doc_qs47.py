# def test(dictionary):
#     for key in dictionary:
#         dictionary[key].clear()
#     return dictionary

# dictionary = { 
#                'C1' : [10,20,30], 
#                'C2' : [20,30,40],
#                'C3' : [12,34]
#              }
# print("\nOriginal Dictionary:")
# print(dictionary)
# print("\nClear the list values in the said dictionary:")
# print(test(dictionary))


a= { 
    'C1' : [10,20,30], 
    'C2' : [20,30,40],
    'C3' : [12,34]
}
print(a)
for k in a:
    a[k].clear()
print(a)
# 47 no