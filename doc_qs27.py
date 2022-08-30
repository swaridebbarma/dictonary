a= [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
c=0
for j,v in a.items():
    if j["id"]==v:
        c=c+v
print(c)