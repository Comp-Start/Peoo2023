def Diagonal(b, h):
  diagonal = (b**2 + h**2)**0.5
  return diagonal

b, h = map(int, input().split())
print(f'Diagonal = {Diagonal(b, h)}')
