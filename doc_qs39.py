marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print("Original Dictionary:")
print(marks)
r={}
for (key, value) in marks.items():
    if value >= 170:
        r[key] = marks[key]
print(r)
# 39 no