class Viagem:
  def __init__(self):
    self.dist = 0
    self.horas = 0
    self.minutos = 0
  def calc_velMedia(self):
    return self.dist/((self.horas*60 + self.minutos)/60)
  
