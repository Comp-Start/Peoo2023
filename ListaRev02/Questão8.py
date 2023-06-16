frase = list(input('Digite uma frase: \n').split())
for x in frase:
  print(x[len(x) - 1], end='')
