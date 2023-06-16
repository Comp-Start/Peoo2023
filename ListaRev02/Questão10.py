frase = input('Digite uma frase: \n')
for x in range(len(frase)):
  substring = frase.replace(frase[0], '')
  frase = substring + frase[0]
  print(frase)
