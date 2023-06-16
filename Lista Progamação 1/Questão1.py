import math
class Circulo:
  def __init__(self):
    self.raio = 0
  def calc_Area(self):
    return math.pi * self.raio**2
  def calc_Circ(self):
    return 2 * math.pi * self.raio
 
x = Circulo()
print("Digite o raio do círculo:")
x.raio = float(input())

print(f"Area = {x.calc_Area()} \nCircunferência = {x.calc_Circ()}")
