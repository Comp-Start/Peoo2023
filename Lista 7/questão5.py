def formatar_nome(nome):
  nomes = nome.split()
  listaNomes = []
  for x in nomes:
    listaNomes.append(x.capitalize())
  resultado = str(listaNomes[0])
  for x in range(1, len(listaNomes)):
    resultado += ' '
    resultado += listaNomes[x]
  return resultado
                 
nome = input('Digite seu nome:')
                 
print(f'Aqui está seu nome formatado: {formatar_nome(nome)}')                 
