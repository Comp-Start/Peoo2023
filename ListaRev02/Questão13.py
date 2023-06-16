#Jeito Fácil 

#frase = input('Digite uma frase: \n')
#print(frase[::-1])

#Jeito usando estruturas de repetição

frase = list(input('Digite uma frase: \n'))
for y in range(len(frase)):
  frase.insert(y, frase[len(frase)- 1])
  del(frase[len(frase) - 1])
resposta = ''.join(frase)   
print(resposta)
  
