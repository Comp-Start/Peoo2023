baseRect = int(input('Digite a base e a altura do retângulo\n'))
alturaRect = int(input())

areaRect = baseRect * alturaRect
perimetroRect = baseRect * 2 + alturaRect * 2
diagonalRect = (baseRect**2 + alturaRect**2) ** (1/2)

print(f'Área = {areaRect:.2f} - Perímetro = {perimetroRect:.2f} - Diagonal = {diagonalRect:.2f}')