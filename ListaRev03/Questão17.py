def VelocidadeMedia(distancia, tempo):
  h, m, s = map(int, tempo.split(':'))
  m = (m*60 + s)/60
  h = (h*60 + m)/60
  vel = str(distancia / h) + ' Km/h'
  return vel

distancia = int(input())
tempo = input()

print(VelocidadeMedia(distancia, tempo))  
  
