# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.

# Original dictionary of lists:

# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# Split said dictionary of lists into list of dictionaries:

# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
 
# a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# b=list(a.keys())
# c=list(a.values())
# print(b)
# print(c)
# y=[]
# x={}
# z=[]
# for i in range(len(c)):
#     for j in range(len(c[i])):
#         z.append(c[i][j])
# print(z)
# l=0
# for k in range(len(b)):
#     x[b[k]]=z[l]
# print(x)

two_digit=input("enter two digit no")
first_digit=two_digit[0]
second_digit=two_digit[1]
print(first_digit)
print(second_digit)
result=int(first_digit)+int(second_digit)
print(result)