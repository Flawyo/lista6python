'''
Autor: Flávio Rodrigo
Data: 21/08/2018

'''

lista = list()

while True:
    num = int(input('Digite um número: '))
    if num in lista:
        continue  
    lista.append(num)
    resp = input('Deseja continuar? (s/n)')
    if resp == 'n':
        break

o = sorted(lista)

print (o)
