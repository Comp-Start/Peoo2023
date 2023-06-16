def RemoverEspacos(texto):
  texto = texto.split()
  semEspacos = ' '.join(texto)
  return semEspacos

texto = input()
print(RemoverEspacos(texto))
