'''Exercício 8. Crie um programa que solicita, inicialmente, o saldo (em reais) de determinada conta corrente. Em seguida, apresente duas opções para o usuário escolher:

1. Realizar um saque

2. Realizar um depósito

Em ambos os casos (saque ou depósito), solicite o valor a ser utilizado na operação (valor a sacar ou valor a depositar). Sabendo que não é possível depositar mais do que R$300,00 de uma vez e que a conta não possui cheque especial, mostre na tela o resultado da operação realizada (sucesso ou insucesso) e o saldo final da conta após a operação.'''

saldo = float(input("Qual seu saldo?\n"))

print("1. Saque")
print("2. Deposito")

trans = int(input("Qual transacao sera feita? (1 ou 2)\n"))

if trans != 1 and trans != 2:
    print("Impossivel realizar essa operacao!")

else:
    vlr = float(input("Quanto? R$"))

    if trans == 1:
        total = saldo - vlr

        if vlr > saldo:
            print("Impossivel sacar um valor maior que o saldo!")

        else:
            print("Voce sacou R$", vlr, "agora tem R$", total)

    elif trans == 2:
        total = saldo + vlr

        if vlr > 300:
            print("Nao eh permitido depositar mais de R$300.00")

        else:
            print("Voce depositou R$", vlr, "agora tem R$", total)


