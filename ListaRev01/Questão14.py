print('Digite três valores:')
a = int(input())
b = int(input())
c = int(input())

formaTriangulo = False
if abs(b - c) < a < b + c:
  formaTriangulo = True
elif abs(a - c) < b < a + c:
  formaTriangulo = True
elif abs(a - b) < c < a + b:
  formaTriangulo = True

if formaTriangulo == True:
  if a == b == c:
    print('Esses valores formam um triângulo equilátero')
  elif a == b or a == c or b == c:
    print('Esses valores formam um triângulo isósceles')
  else:
    print('Esses valores formam um triângulo escaleno')
else:
  print('Esses valores não formam um triângulo')
