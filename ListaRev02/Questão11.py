frase = input('Digite uma frase: \n')
sum = 0
for x in frase:
  try:
    int(x)
    isInteger = True
  except ValueError:
    isInteger = False
  if isInteger == True:
    sum+= int(x)
print(sum)    
