def MenorInteiro(x):
  inteiro = round(x)
  if inteiro < x:
    inteiro +=1
  return inteiro

x = float(input())
print(f'O menor inteiro é {MenorInteiro(x)}')
  
