'''Exercício 5. Solicite ao usuário que informe 3 valores inteiros. Depois disso, imprima uma das seguintes mensagens: TRIÂNGULO EQUILÁTERO, TRIÂNGULO ESCALENO, TRIÂNGULO ISÓSCELES ou NÃO FORMA UM TRIÂNGULO. 

Para a última mensagem, é importante notar que nem todo conjunto de 3 valores formam um triângulo, pois os valores devem obedecer à Condição de Existência de um Triângulo: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Ou seja:

( | b - c | < a < b + c) e ( | a - c | < b < a + c) e ( | a - b | < c < a + b)'''

a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: "))
c = int(input("Digite o lado c: "))

mod1 = b - c
mod2 = a - c
mod3 = a - b

if mod1 < 0:
    mod1 *= -1

if mod2 < 0:
    mod2 *= -1

if mod3 < 0:
    mod3 *= -1

if mod1 < a < b + c and mod2 < b < a + c and mod3 < c < a + b:
    if a == b and b == c:
        print("EQUILATERO")

    elif a != b and b != c and a != c:
        print("ESCALENO")

    else:
        print("ISOCELES")

else:
    print("NAO FORMA UM TRIANGULO!")