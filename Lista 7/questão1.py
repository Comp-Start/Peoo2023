def maior(x, y):
  maior = x
  if y > x:
    maior = y
  return maior

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

print(f'O maior é {maior(x, y)}')
