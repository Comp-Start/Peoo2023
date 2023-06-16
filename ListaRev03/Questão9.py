def Vogais(texto):
  vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
  vogaisTexto = ''
  for x in texto:
    if x in vogais:
      vogaisTexto += x
  return vogaisTexto    

texto = input()
print(f'Vogais = {Vogais(texto)}')
