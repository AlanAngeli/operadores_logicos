""""
Operadores lógicos

and, or, not, in, e not in


"""

#comparacao1 and comparacao2 - (Verdadeiro e Falso) = False

#comparacao1 or comparacao2  - Verdadeiro ou Verdadeiro

#Exemplo de not:

a = 2
b = 3

if not b > a:
    print("B é maior que A")
else:
    print("A é maior que B")

#Exemplo de in:

nome = input("Digite seu nome: ")
if "a" in nome:
    print("Existe a letra A no seu nome")
elif "A" in nome:
    print("Existe a letra A no seu nome")
else:
    print("Seu nome não tem a letra A")

#Exemplo de not in

nome = input("Digite seu nome: ")
if "o" not in nome:
    print("Não tem letra O no seu nome")
else:
    print("Seu nome tem a letra O")


