notaPrimeiroBimestre = int(input('Digite a nota do primeiro bimestre da disciplina:\n'))
notaSegundoBimestre = int(input('Digite a nota do segundo bimestre da disciplina:\n'))
peso1 = 2
peso2 = 3
mediaParcial = ((notaPrimeiroBimestre * peso1) + (notaSegundoBimestre * peso2)) / (peso1 + peso2)
if int(mediaParcial) == mediaParcial:
    mediaParcial = int(mediaParcial) 
print(f'Média parcial = {mediaParcial}')