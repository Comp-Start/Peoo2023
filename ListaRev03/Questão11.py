def Senha(texto):
  texto = texto.split()
  senha = ''
  for x in texto:
    senha+= str(len(x))
  return senha  

texto = input()
print(f'Senha = {Senha(texto)}')
