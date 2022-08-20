'''Inicialmente, solicite o nome dos 2 jogadores.
Em seguida, peça para o primeiro jogador digitar sua jogada (do tipo String).
Depois, peça para o segundo jogador digitar sua jogada (também do tipo String).
Ao final, imprima o nome do jogador vencedor, ou uma mensagem de erro caso algum dos dois não tenha digitado uma das String possíveis (“pedra”, “papel”, “tesoura”, “lagarto” ou “spock”). 

PAPEL > PEDRA E SPOCK
TESOURA > PAPEL E LAGARTO
PEDRA > LAGARTO E TESOURA
SPOCK > TESOURA E PEDRA
LAGARTO > SPOCK E PAPEL'''

jogador1 = input("Nome do jogador 1: ")
jogador2 = input("Nome do jogador 2: ")

jogada1 = input(jogador1 + ": pedra, papel, tesoura, lagarto ou spock?\n")
jogada2 = input(jogador2 + ": pedra, papel, tesoura, lagarto ou spock?\n")

if (jogada1 == 'papel' and jogada2 == 'pedra'):
    print(jogador1, "GANHOU!")
    print("PAPEL cobre a PEDRA")

elif (jogada1 == 'papel' and jogada2 == 'spock'):
    print(jogador1, "GANHOU!")
    print("PAPEL desaprova o SPOCK")

elif (jogada1 == 'tesoura' and jogada2 == 'papel'):
    print(jogador1, "GANHOU!")
    print("TESOURA corta o PAPEL")

elif (jogada1 == 'tesoura' and jogada2 == 'lagarto'):
    print(jogador1, "GANHOU!")
    print("TESOURA decapita o LAGARTO")

elif (jogada1 == 'pedra' and jogada2 == 'lagarto'):
    print(jogador1, "GANHOU!")
    print("PEDRA esmaga o LAGARTO")

elif (jogada1 == 'pedra' and jogada2 == 'tesoura'):
    print(jogador1, "GANHOU!")
    print("PEDRA destroi a TESOURA")

elif (jogada1 == 'spock' and jogada2 == 'tesoura'):
    print(jogador1, "GANHOU!")
    print("SPOCK quebra a TESOURA")

elif (jogada1 == 'spock' and jogada2 == 'pedra'):
    print(jogador1, "GANHOU!")
    print("SPOCK vaporiza a PEDRA")

elif (jogada1 == 'lagarto' and jogada2 == 'spock'):
    print(jogador1, "GANHOU!")
    print("LAGARTO envenena o SPOCK")

elif (jogada1 == 'lagarto' and jogada2 == 'papel'):
    print(jogador1, "GANHOU!")
    print("LAGARTO come o PAPEL")

#

if (jogada2 == 'papel' and jogada1 == 'pedra'):
    print(jogador2, "GANHOU!")
    print("PAPEL cobre a PEDRA")

elif (jogada2 == 'papel' and jogada1 == 'spock'):
    print(jogador2, "GANHOU!")
    print("PAPEL desaprova o SPOCK")

elif (jogada2 == 'tesoura' and jogada1 == 'papel'):
    print(jogador2, "GANHOU!")
    print("TESOURA corta o PAPEL")

elif (jogada2 == 'tesoura' and jogada1 == 'lagarto'):
    print(jogador2, "GANHOU!")
    print("TESOURA decapita o LAGARTO")

elif (jogada2 == 'pedra' and jogada1 == 'lagarto'):
    print(jogador2, "GANHOU!")
    print("PEDRA esmaga o LAGARTO")

elif (jogada2 == 'pedra' and jogada1 == 'tesoura'):
    print(jogador2, "GANHOU!")
    print("PEDRA destroi a TESOURA")

elif (jogada2 == 'spock' and jogada1 == 'tesoura'):
    print(jogador2, "GANHOU!")
    print("SPOCK quebra a TESOURA")

elif (jogada2 == 'spock' and jogada1 == 'pedra'):
    print(jogador2, "GANHOU!")
    print("SPOCK vaporiza a PEDRA")

elif (jogada2 == 'lagarto' and jogada1 == 'spock'):
    print(jogador2, "GANHOU!")
    print("LAGARTO envenena o SPOCK")

elif (jogada2 == 'lagarto' and jogada1 == 'papel'):
    print(jogador2, "GANHOU!")
    print("LAGARTO come o PAPEL")
