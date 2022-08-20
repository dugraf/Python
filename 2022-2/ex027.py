'''Exercício 7. Solicite que o usuário informe uma data, solicitando de forma separada o ano, o mês e o dia (nesta ordem), todos valores inteiros.
O ano pode ser qualquer valor entre 0 e 2022.
O mês deve ser um valor entre 1 (inclusive) e 12 (inclusive).
O dia deve estar de acordo com o mês informado e, ainda, com o ano (bissexto ou não). Acesse ESTE LINK para ver como calcular se um ano é ou não bissexto.'''

print("Informe uma data, por favor!")

ano = int(input("Ano: "))
bi = ano % 4
mes = int(input("Mes: "))
dia = int(input("Dia: "))

if (ano < 0 or ano > 2022 or mes <= 0 or mes > 12 or dia < 1 or dia > 31):
    print("Desculpe, data invalida!")

else:
    if (mes == 2 and bi == 0 and dia == 29):
        print("Essa data eh valida!")

    elif (mes == 2 and bi != 0 and dia == 29):
        print("Desculpe, sem dia 29 nessa data!")
    
    else:
        print("Essa data eh maravilhosa!")