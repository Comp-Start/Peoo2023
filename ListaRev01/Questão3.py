n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

somaPares = 0
somaImpares = 0

lista = [n1, n2, n3, n4]

for x in lista:
  if x % 2 == 0:
    somaPares += x
  else:
    somaImpares += x
print(f'Soma dos pares = {somaPares}')
print(f'Soma dos ímpares = {somaImpares}')    
