def MMC(x, y):
  maior = max(x, y)
  while maior % x != 0 or maior % y != 0: 
    maior += 1 
  return maior

x, y = map(int, input().split())
print(MMC(x, y))
