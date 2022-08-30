# def sum_math_v_vi_average(list_of_dicts):
#     for d in list_of_dicts:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return list_of_dicts 
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(sum_math_v_vi_average(student_details))


a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for i,j in a.items():
    print(j[4])
for i,j in a.items():
    print(i,"has value",j)
# 37 no


