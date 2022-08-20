'''Exercício 6. Crie um programa que simula um jogo de par ou ímpar entre 2 jogadores.
Sem programa deve solicitar o nome dos dois jogadores e a opção do primeiro jogador (par ou ímpar).
Em seguida, o programa deve solicitar um valor inteiro para cada jogador, referente ao valor que ele vai jogar.
No final, imprima quem ganhou o jogo.'''

from time import sleep


print("**********************")
sleep(.2)
print("*JOGO DO PAR OU IMPAR*")
sleep(.2)
print("**********************")
sleep(.2)

jogador1 = input("Nome do jogador 1: ")
jogador2 = input("Nome do jogador 2: ")

parOuImpar = input((jogador1 +", par ou impar?: "))

if parOuImpar != 'par' and parOuImpar != 'impar':
    print("Vamo se ajudar magrao!")

else:
    n1 = int(input(jogador1 +" digite um numero: "))
    n2 = int(input(jogador2 +" digite um numero: "))

    res = (n1 + n2) % 2

    if res == 0 and parOuImpar == 'par':
        print(jogador1, "GANHOU!")

    elif res == 0 and parOuImpar == 'impar':
        print(jogador2, "GANHOU!")

    elif res != 0 and parOuImpar == 'par':
        print(jogador2, "GANHOU!")

    elif res != 0 and parOuImpar == 'impar':
        print(jogador1, "GANHOU!")