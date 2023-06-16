def AreaCirculo(raio):
  area = (3.14 * raio)**2
  return area

raio = int(input('Digite o raio do círculo: \n'))
print(f'Área = {AreaCirculo(raio)}')
