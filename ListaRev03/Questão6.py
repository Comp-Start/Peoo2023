def Frete(massa, distancia):
  frete = 0.01 * massa * distancia
  return frete

massa, distancia = map(int, input().split())
print(f'Frete = {Frete(massa, distancia)}')
