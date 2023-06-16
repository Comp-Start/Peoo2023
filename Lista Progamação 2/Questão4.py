class Entrada:
  def __init__(self, dia, horario):
    self.set_dia(dia)
    self.set_horario(horario)
  def set_dia(self, v):
    self.__dia = v
  def set_horario(self, v):
    if v >= 0: self.__horario = v
  def get_dia(self):
    return self.__dia
  def get_horario(self):
    return self.__horario
  def valorEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia.capitalize() == 'Quarta':
      return 8
    if self.__dia.capitalize() in val1:
      if self.__horario >= 17:
        return 24
      else:
        return 16
    if self.__dia.capitalize() in val2:
      if self.__horario>=17:
        return 30
      else:
        return 20
  def valorMeiaEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.__dia.capitalize() == 'Quarta':
      return 8
    if self.__dia.capitalize() in val1:
      if self.__horario >= 17:
        return 12
      else:
        return 8
    if self.__dia.capitalize() in val2:
      if self.__horario>=17:
        return 15
      else:
        return 10
class UI:
  @staticmethod
  class main():
    dia = input('Qual o dia da semana? \n')
    horario, aux = map(int, input('Digite o horário em que deseja ir (hh:mm): \n').split(':'))
    entrada = Entrada(dia, horario)

    print(f'Você pagará R${entrada.valorEntrada()} em uma entrada.')
    print(f'Você pagará R${entrada.valorMeiaEntrada()} em uma meia-entrada.')
UI.main()    
  
