frase = input('Digite uma frase: \n')
a = 0
e = 0
i = 0
o = 0
u = 0
for x in frase.upper():
  if x == 'A':
    a+=1
  elif x == 'E':
    e+=1
  elif x == 'I':
    i+= 1
  elif x == 'O':
    o+=1
  elif x == 'U':
    u+=1
print(f'A - {a}') 
print(f'E - {e}')
print(f'I - {i}')
print(f'O - {o}')
print(f'U - {u}')
