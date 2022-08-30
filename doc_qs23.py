# Python program to demonstrate
# finding 3 highest values in a Dictionary
from heapq import nlargest
 
# Initial Dictionary
my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}

 
 
# print("Initial Dictionary:")
# print(my_dict, "\n")
 
ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
 
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
 
for val in ThreeHighest:
    print(val, ":", my_dict.get(val))
    
n= {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
m=0
sm=0
thm=0
k_m=0
k_sm=0
k_thm=0
for i in n:
    if n[i]>m:
        m=n[i]
        k_m=i
for j in n:
    if n[j]>sm and n[j]<m:
        sm=n[j]
        k_sm=j
for k in n:
    if n[k]>thm and n[k]<sm:
        thm=n[k]
        k_thm=k
print(k_m,":",m)
print(k_sm,":",sm)
print(k_thm,":",thm)
# 23 no





