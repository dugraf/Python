'''Exercício 8. Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:

Digite 1 para somar dois valores
Digite 2 para subtrair dois valores
Digite 3 para multiplicar dois valores
Digite 4 para dividir dois valores
Digite 5 para realizar uma potência entre dois valores
Digite 6 para realizar uma radiciação entre dois valores
Digite qualquer outro número para sair
De acordo com a opção informada pelo usuário, solicite os valores necessários para o usuário e imprima na tela o resultado da operação realizada.'''

print("1 para somar")
print("2 para subtrair")
print("3 para multiplicar")
print("4 para dividir")
print("5 para potencia")
print("6 para radiciacao")
print("Qualquer outro numero para sair")

opera = int(input("Digite: "))

if opera > 0 and opera < 7:

    print("Agora escolha os numeros da operacao:")

    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))

    if opera == 1:
        opera = n1 + n2
        print(opera)

    elif opera == 2:
        opera = n1 - n2
        print(opera)

    elif opera == 3:
        opera = n1 * n2
        print(opera)

    elif opera == 4:
        opera = n1 / n2
        print(opera)

    elif opera == 5:
        opera = n1 ** n2
        print(opera)

    elif opera == 6:
        opera = n1 ** (1 / n2)
        print(opera)

else:
    print("Obrigado!")