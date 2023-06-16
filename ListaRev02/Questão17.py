frase = input('Digite uma frase: \n').split()
vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for palavra in frase:
  qtd = 0
  for caractere in palavra:
    if caractere in vogais:
      qtd+=1
  for x in range(qtd):
    print(palavra, end=' ')
  
