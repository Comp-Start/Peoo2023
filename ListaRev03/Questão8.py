def Soma(inicio, fim):
  sum = 0
  maior = inicio
  menor = fim
  if fim > inicio:
    maior = fim
    menor = inicio
  for x in range(menor, maior + 1):
    sum+=x
  return sum  

inicio, fim = map(int, input().split())
print(f'Soma = {Soma(inicio, fim)}')
