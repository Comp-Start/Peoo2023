frase = list(input('Digite uma frase: \n').split())
for x in range(len(frase)):
  resposta = ' '.join(frase)
  del(frase[0])
  print(resposta)
