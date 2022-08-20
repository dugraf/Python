#Exercício 10. Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

letra = input("Digite uma letra:")

if letra in ('a', 'e', 'i', 'o', 'u'):
    print(letra, "eh uma vogal!")

elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print(letra, "eh uma consoante!")

else:
    print(letra, "nao eh uma consoante nem uma vogal!")