operacao = input('Digite dois valores inteiros separados por um operador +, -, * ou / \n')
if '+' in operacao:
  a, b = map(int, operacao.split('+'))
  calc = a + b
elif '-' in operacao:
  a, b = map(int, operacao.split('-')) 
  calc = a - b
elif '*' in operacao:
  a, b = map(int, operacao.split('*'))
  calc = a * b
elif '/' in operacao:
  a, b = map(int, operacao.split('/'))
  calc = a / b
print(f'O resutado da operação é {calc}')  
