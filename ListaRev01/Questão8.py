Maior valor = 10
Menor valor = 1
A soma do segundo maior valor com o segundo menor = 5
''
n1 = int(input('Digite quatro valores inteiros \n'))
n2 = int(input())
n3 = int(input())
n4 = int(input())

lista = [n1, n2, n3, n4]
lista.sort(reverse = True)

print(f'Maior valor = {lista[0]}')
print(f'Menor valor = {lista[3]}')
print(f'A soma do segundo maior valor com o segundo menor = {lista[1] + lista[2]}')
