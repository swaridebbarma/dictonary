# def test(dictt):
#     result = {key: [idx for idx in val if not idx % 2]  
#           for key, val in dictt.items()}   
#     return result    

# students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
# print("\nOriginal Dictionary:")
# print(students)
# print("Filter even numbers from said dictionary values:")
# print(test(students))

# students = {'V' : [1, 3, 5], 'VI' : [1, 5], 'VII' : [2, 7, 9]} 
# print("\nOriginal Dictionary:")
# print(students)
# print("Filter even numbers from said dictionary values:")
# print(test(students))




dic= {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]}
new_dic={}
for i in dic:
    b=[]
    for j in dic[i]:
        if j%2==0:
            b.append(j)
        new_dic[i]=b
print(new_dic)
# 51 no


dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
b={}
for i in dic:
    c=[]
    for j in dic[i]:
        if j%2==0:
            c.append(j)
        b[i]=c
print(b)
