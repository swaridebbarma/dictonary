a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
cp={}
for i in a:
    if i['item'] in cp.keys():
        cp[i['item']]+=i['amount']
    else:
        cp[i['item']]=i['amount']  
    
print(cp)   
# 24 no