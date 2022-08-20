'''Exercício 10. Crie um programa que analisa se uma pessoa pode ou não tirar a carteira de motorista.
Se a pessoa tem 18 anos ou mais, o programa faz 3 perguntas (ela deve responder via teclado e uma de cada vez). As perguntas são:

Caso ela acerte 2 ou 3 perguntas, ela está apta para tirar a carteira (respostas corretas, em ordem: b, d, d). No final, seu programa deve informar se a pessoa está ou não apta para tirar a carteira de motorista.'''

print("Vamos saber se voce esta apto para tirar a carteira de motorista!")

idade = int(input("Quantos anos voce tem?\n"))
point = 0

if idade < 18:
    print("Voce nao pode fazer a carteira de motorista com essa idade!")

else:
    print("PRIMEIRA PERGUTA:")

    print("Ao prestar socorro à vítima de um acidente, NÃO se deve:")
    print("a) acionar imediatamente o Corpo de Bombeiros")
    print("b) dar água, comida ou qualquer substância para a vítima cheirar")
    print("c) conversar com a vítima para saber de suas condições gerais")
    print("d) deixar a vítima confortável até a chegada do socorro especializado")
    
    p1 = input()

    if p1 == 'b':
        point += 1

    print("SEGUNDA PERGUTA:")

    print("Ao se deparar com uma sinaleira na cor vermelha, você deve:")
    print("a) rir dela")
    print("b) passar mais rápido, pois é perigoso parar")
    print("c) dobrar a direita, pois vermelho indica direita")
    print("d) parar")

    p2 = input()

    if p2 == 'd':
        point += 1

    print("TERCEIRA PERGUTA:")

    print("Segundo a direção defensiva, quando você está em uma via e um pedestre vai atravessar você:")
    print("a) buzina muito forte para que o pedestre se assuste")
    print("b) atropela o pedestre, pois lugar de pedestre é na calçada")
    print("c) para e dá uma carona para o pedestre, pois é uma lei de trânsito")
    print("d) para e aguarda ele atravessar")

    p3 = input()

    if p3 == 'd':
        point += 1

if point < 2:
    print("Voce nao passou")

else:
    print("Voce passou!")