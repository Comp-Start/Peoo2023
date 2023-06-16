count = 0
qtd = 0
for x in range(1, 31):
  if qtd == 3:
    print(count, end=' ')
    count = 0
    qtd = 0
  print(x, end=' ')
  count+=x
  qtd +=1 
print(count)
