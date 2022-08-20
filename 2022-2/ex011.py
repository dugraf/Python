#Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar. 

number = int(input("Digite um numero inteiro, por favor: "))

if number % 2 == 0:
    print("Este numero eh par!")

else:
    print("Este numero eh impar!")