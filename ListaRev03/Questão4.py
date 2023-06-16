def VolumeEsfera(r):
  volume = 4/3 * 3.14 * r**3
  return volume

raio = int(input())
print(f'Volume = {VolumeEsfera(raio)}')
