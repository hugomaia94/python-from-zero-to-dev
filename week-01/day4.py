'''
Exercício 1
Peça para o usuário digitar um número e mostre o dobro desse número.
Exemplo:
Digite um número: 5
O dobro é: 10


01
num = float (input('Digite um número para obter o dobro:'))
num = num * 2
print(num)



Exercício 2
Peça para o usuário digitar dois números e mostre a soma deles.
Exemplo:
Digite o primeiro número: 3
Digite o segundo número: 7
A soma é: 10


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print(f'A soma dos dois números é: {num1+num2}')

Exercício 3
Peça para o usuário digitar o nome e a idade. Depois mostre quantos anos a pessoa terá daqui a 10 anos.
Exemplo:
Nome: Ana
Idade: 20
Ana, daqui a 10 anos você terá 30 anos.

name = str(input('Digite seu nome: '))
age = int(input('Digite sua idade: '))
print(f'{name} daqui a 10 anos você terá {age+10} anos.')


Exercício 4
Peça a idade do usuário e mostre se ele é maior de idade.
Exemplo:
Digite sua idade: 18
Maior de idade: True

idade = int(input('Digite sua idade: '))
maior_de_idade = idade >= 17 
print(f'Maior de idade: {maior_de_idade}')


Exercício 5
Peça uma medida em metros e converta para centímetros.
Exemplo:
Digite metros: 2
Em centímetros: 200

medida = float(input('Digite uma medida em metros para converter em centímetros: '))
print(f'{medida} metros é: {medida*100} centímetros.')

'''