def maior(x, y, z):
  maior = x
  if y > maior:
    maior = y
  if z > maior:
    maior = z
  return maior

x = int(input('Digite um número:'))
y = int(input('Digite outro número:'))
z = int(input('Digite mais um número:'))

print(f'O maior número é {maior(x, y, z)}')
