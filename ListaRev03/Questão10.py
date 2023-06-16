def Palavra(texto, pos):
  palavras = []
  palavra = ''
  for x in texto:
    if x == ' ':
      palavras.append(palavra)
      palavra = ''
    else:
      palavra += x
  palavras.append(palavra)    
  return palavras[pos] 
  

texto = input()
pos = int(input())
print(Palavra(texto, pos))


  
