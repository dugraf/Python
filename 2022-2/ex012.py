#Exercício 2. Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.

print("Digite 2 numeros inteiros, por favor!")

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

if a < b:
    print("O numero", b, "eh maior que o ", a)

else:
    print("O numero ", a, "eh maior que o ", b)
