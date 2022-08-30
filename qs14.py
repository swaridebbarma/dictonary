# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# d=a.values()
# c=a.keys()
# print(c)
# print(d)
# d=[45,60,20,30,50]
# i=0
# while i < len(d):
#     b=i
#     j=i+1
#     while j< len(d):
#         if d[b]<d[j]:
#             b=j
#         j+=1
#     d[i],d[b]=d[b],d[i]
#     i+=1
# print(d)

a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
key=[]
value=[]
for i,j in a.items():
    key.append(i)
    value.append(j)
print(key)
print(value)
for x in value:
    for y in value:
        if x>y:
            temp=x
            x=y
            y=temp
print(y)
dict={}
for k in range(len(key)):
    dict[key[k]]=value[k]
print(dict)

# d={1:"rekha",2:"swari",3:"dhanika"}
# x=d.values()
# print(x)

# a={1:10,2:20,3:30}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(sum)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sortedbyval={k:v for k,v in sorted(a.items(),key=lambda v:v[1])}
# sortedbyval1={k:v for k,v in sorted(a.items(),key = lambda v:v[1],reverse=True)}
# print(sortedbyval)
# print(sortedbyval1)

