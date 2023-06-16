aux = ''
for x in range(1, 11):
  if x % 2 == 0:
    aux += ' ' + str(x)
  print(f'{x}{aux}')
  
