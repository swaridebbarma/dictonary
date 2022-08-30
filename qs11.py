n = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
}
m=0
sm=0
thm=0
for i in (n):
    if n[i]>m:
        thm=sm
        sm=m
        m=n[i]   
    if n[i]<m and n[i]>sm:
        sm=n[i]
    if n[i]<sm and n[i]>thm:
        thm=n[i]
print(m,sm,thm)
