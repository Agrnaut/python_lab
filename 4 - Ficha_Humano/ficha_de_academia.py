from Pessoa import Pessoa

def valida_idade():
    nova_idade = int(input("Por favor, informe sua nova idade:"))
    if(nova_idade < idade):
        print("Não válido")
    elif(idade < 21 and nova_idade >= 21):
        crescimento = 21 - idade
        nova_altura = altura + round((crescimento * 0.005), 2)
        humano.crescer(nova_altura)
        humano.envelhecer(nova_idade)
    elif(idade < 21 and nova_idade < 21):
        crescimento = (nova_idade - idade)
        nova_altura = altura + round((crescimento * 0.005), 2)
        humano.crescer(nova_altura)
        humano.envelhecer(nova_idade)
    else:
        humano.envelhecer(nova_idade)
def altera_ficha():
    valor = ((int(input("Qual informação você gostaria de alterar na sua ficha?\n [1]Idade  [2]Peso  [3]Altura"))))
    if (valor == 1):
        valida_idade()
    elif(valor == 2):
        humano.engordar(int(input("Por favor, informe seu novo peso:")))
    else:
        humano.crescer(float(input("Por favor, informe sua nova altura:")))

def menu():
    opcao = int(input("O que você gostaria de fazer:\n [1]Mostrar ficha  [2]Alterar Ficha  [3]Encerrar Cadastro:\n[Opção]:"))
    if(opcao == 1):
        return 1
    elif(opcao == 2):
        return 2
    else:
        return 3


print("Bem vindo a academia Pythallets"
      "\nFavor preencher a ficha de acordo:")

fim_de_loop = False

nome = input("Nome:")
idade = int(input("idade:"))
peso = float(input("peso:"))
altura = float(input("altura:"))
humano = Pessoa(nome, idade, peso, altura)

while (not fim_de_loop):

    pergunta = menu()
    if(pergunta == 1):
        print(f"Nome: {humano.mostra_pessoa[0]}\n"
              f"Idade: {humano.mostra_pessoa[1]}\n"
              f"Peso: {humano.mostra_pessoa[2]}\n"
               f"Altura: {humano.mostra_pessoa[3]}")

    elif(pergunta == 2):
        altera_ficha()

    else:
        print("Obrigado por escolher nosso serviço:")
        break




# print(humano.mostra_pessoa)
#
#
#
# nova_idade = int(input("Digite sua atual idade:"))
#
#
#
# print(humano.mostra_pessoa)

