def iniciais(nome):
  palavras = nome.split()
  resultado = ''
  for palavra in palavras:
    resultado += palavra[0]
  return resultado

nome = input('Escreva seu nome completo: ')
print(f'As iniciais do seu nome são: {iniciais(nome)}')
  
