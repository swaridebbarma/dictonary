a =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
}
c=0
for i in a:
    for j in a[i]: 
        c+=1        
print(c)