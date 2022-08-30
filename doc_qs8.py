a= {1: 9, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(i):
  if i in a:
      print('Key is present in the dictionary:',i)
  else:
      print('Key is not present in the dictionary:',i)
is_key_present(5)
is_key_present(9)
# 8 no