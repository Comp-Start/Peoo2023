print('Digite quatro valores inteiros')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
numbers = [n1, n2, n3, n4]

media = sum(numbers) / len(numbers)
print(f'Média = {media}')

menores = []
maiores = []

for x in numbers:
  if x < media:
    menores.append(x)
  else:
    maiores.append(x)

print('Números menores que a média')

for i in menores:
  print(i)

print('Números maiores ou iguais a média')
for y in maiores:
  print(y)
