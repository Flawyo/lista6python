'''
Autor: Flávio Rodrigo
Data: 21/08/2018

'''
lista = list()
for n in range (5):
    numero=int(input('Digite o {} número: '.format(n+1)))
    lista.append(numero)

maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)

print('O maior número digitado foi o {} que está na posição {}.'.format(maior,pos_max))
print('O menor número digitado foi o {} que está na posição {}.'.format(menor,pos_min))
