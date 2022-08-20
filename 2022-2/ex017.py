#Exercício 7. Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não.

from time import sleep

print("*************************************")
sleep(.5)
print("*QUER SABER QUAL NUMERO EH BISSEXTO?*")
sleep(.5)
print("*************************************")
sleep(.5)

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print(ano, "eh um ano bissexto!")

else:
    print(ano, "nao eh bissexto!")