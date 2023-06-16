frase = input('Digite uma frase: \n').split()
senha = ''
for palavra in frase:
  senha += str(len(palavra))
print(senha)  
 
