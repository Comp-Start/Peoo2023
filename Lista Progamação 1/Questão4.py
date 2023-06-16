class Entrada:
  def __init__(self):
    self.dia = ''
    self.horario = 0
  def valorEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia.capitalize() == 'Quarta':
      return 8
    if self.dia.capitalize() in val1:
      if self.horario >= 17:
        return 24
      else:
        return 16
    if self.dia.capitalize() in val2:
      if self.horario>=17:
        return 30
      else:
        return 20
  def valorMeiaEntrada(self):
    val1 = ['Segunda', 'Terça', 'Quinta']
    val2 = ['Sexta', 'Sábado', 'Domingo']
    if self.dia.capitalize() == 'Quarta':
      return 8
    if self.dia.capitalize() in val1:
      if self.horario >= 17:
        return 12
      else:
        return 8
    if self.dia.capitalize() in val2:
      if self.horario>=17:
        return 15
      else:
        return 10

entrada = Entrada()
entrada.dia = input('Qual o dia da semana? \n')
entrada.horario, aux= map(int, input('Digite o horário em que deseja ir (hh:mm): \n').split(':'))
print(f'Você pagará R${entrada.valorEntrada()} em uma entrada.')
print(f'Você pagará R${entrada.valorMeiaEntrada()} em uma meia-entrada.')
