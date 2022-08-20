'''Exercício 9. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.'''

print("Vamos verificar se a nota precisara de Grau C")

gA = float(input("Nota do Grau A: "))
gB = float(input("Nota do Grau B: "))

nFinal = (gA * 0.33) + (gB * 0.66)

print("Sua nota ficou %.1f" % nFinal)

if nFinal <= 6:
    print("Voce precisara fazer o Grau C!")

else:
    print("Voce nao precisara fazer o Grau C!")