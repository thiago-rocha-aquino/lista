#Desenvolver um programa em Python que leia 10 nomes,
# idade e altura armazenando-os numa Lista, No final
# mostre o nome a idade e a altura das pessoas: com maior idade: com menor altura;
pessoas = []
for i in range(3):
    print(f"Pessoa {i + 1}")
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    altura = float(input("digite sua altura: "))
    pessoas.append({"nome": nome, "idade": idade, "altura": altura})
pessoa_maior = max(pessoas, key=lambda pessoa: pessoa['idade'])
pessoa_menor = min(pessoas, key=lambda pessoa: pessoa['altura'])
print("pessoa com maior idade:")
print(f"Nome: {pessoa_maior['nome']}, Idade: {pessoa_maior['idade']}, Altura: {pessoa_maior['altura']}")
print("pessoa com menor altura:")
print(f"Nome: {pessoa_menor['nome']}, Idade: {pessoa_menor['idade']}, Altura: {pessoa_menor['altura']}")


