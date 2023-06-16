def VolumeLitros(h, l, p):
  volumeMetroCubico = h * l * p
  volumeLitros = volumeMetroCubico * 1000
  return volumeLitros

h, l, p = map(float, input().split())
print(f'Volume em Litros = {VolumeLitros(h, l, p)}')
