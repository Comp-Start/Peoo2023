def aprovado(nota1, nota2):
  media = (nota1+nota2)/2
  resultado = ''
  if media >= 60:
    resultado = 'Aprovado'
  else:
    resultado = 'Reprovado'
    
nota1 = int(input('Digita a nota 1: '))
nota2 = int(input('Digite a nota 2: '))

print(aprovado(nota1, nota2))
