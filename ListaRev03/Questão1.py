def Menor(x, y):
  menor = min(x, y)
  return menor

a, b = map(int, input().split())
print(f'Menor = {Menor(a, b)}')
