import itertools 
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
    
    
d ={'1':['a','b'], '2':['c','d']}
a,b = d.values()
for i in a:
    for j in b:
        print(i+j)
# 22 no
