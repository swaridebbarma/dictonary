# a= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# b={k:v for k,v in sorted(a.items(),key=lambda v:v[1])}
# print(b)
# # 5 no

# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=list(dic.keys())
# b=list(dic.values())
# print(a)
# print(b)
# a.reverse()
# b.reverse()
# print(a)
# print(b)
# a.sort()
# b.sort()
# print(a)
# print(b)
# print(dict(zip(a,b)))


# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=list(dic.keys())
# b=list(dic.values())
# i=len(a)-1
# i=len(b)-1
# c=[]
# d=[]
# while i>=0:
#   c.append(a[i])
#   d.append(b[i])
#   i=i-1
# print(c)
# print(d)
# c.sort(reverse=True)
# # c.sort()
# print(c)
# d.sort()
# print(dict(zip(c,d)))


# # i=len(a)-1
# c=[]
# d=[]
# while i>=0:
#   c.append(a[i])
#   i-=1
# print(c)
# print(dict(zip(c,d)))


# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=list(dic.keys())
# b=list(dic.values())
# print(a)
# print(b)
# i=len(b)-1
# i=len(a)-1
# c=[]
# d=[]
# while i>=0:
#   c.append(a[i])
#   d.append(b[i])
#   i-=1
# print(c)
# print(d)
# print(dict(zip(c,d)))
# for i in range(len(b)):
#   for j in range(len(b)):
#     if b[i]<b[j]:
#       c=b[i]
#       b[i]=b[j]
#       b[j]=c
# #       d=a[i]
# #       a[i]=a[j]
# #       a[j]=d
# # print(b)
# # print(a




# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=list(dic.keys())
# b=list(dic.values())
# # print(a)
# # print(b)
# for i in range(len(b)):
#   for j in range(len(b)):
#     if b[i]<b[j]:
#       c=b[i]
#       b[i]=b[j]
#       b[j]=c
#       d=a[i]
#       a[i]=a[j]
#       a[j]=d
# print(b)
# print(a)
# i=len(b)-1
# i=len(a)-1
# c=[]
# d=[]
# while i>=0:
#   c.append(a[i])
#   d.append(b[i])
#   i-=1
# # print(c)
# # print(d)
# m={}
# for i in range(len(c)):
#     m[c[i]]=d[i]
# print(m)
# r=list(m.keys())
# r.reverse()
# # print(r)
# a=sorted(m.values())
# # print(a)
# l={}
# for i in range(len(r)):
#     l[r[i]]=(a[i])
# print(l)
    




"""a=list(dic.keys())
b=list(dic.values())
print(a)
print(b)
for i in range(len(b)):
  for j in range(len(b)):
    if b[i]<b[j]:
      c=b[i]
      b[i]=b[j]
      b[j]=c
      d=a[i]
      a[i]=a[j]
      a[j]=d
print(b)
print(a)
i=len(b)-1
i=len(a)-1
c=[]
d=[]
while i>=0:
  c.append(a[i])
  d.append(b[i])
  i-=1
print(c)
print(d)
print(dict(zip(c,d)))"""
# print(b)
# print(a)
# b.reverse()
# a.reverse()
# # print(b)
# # print(a)
# print(dict(zip(b,a)))

# e={}
# for k in range(len(b)):
#   e[k]=b[k]
# print(e)




# a=[2,1,5,6]
# b=[4,6,8,3]
# c={}
# for i in range(len(a)):
#     c[a[i]]=b[i]
# print(c)
    