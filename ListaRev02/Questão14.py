frase = input('Digite uma frase: \n')
frase = list(frase[::-1].split())
for x in range(len(frase)):
  print(frase[len(frase) - 1 - x])

