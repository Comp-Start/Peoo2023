def Referencia(nome):
  nome = list(nome.split())
  referencia = nome[len(nome) - 1]+','
  del(nome[len(nome) - 1])
  string = ''
  for x in nome:
    if x != 'de':
      string+=' ' + x[0] + '.'
  referencia += string
  return referencia

nome = input()
print(Referencia(nome))
    
