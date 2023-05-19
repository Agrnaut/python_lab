from Estoque import Feira
from Estoque import Solicitante

print("Bem vindo a Feira-Livre")

solicitante = Solicitante(input("Digite seu nome:"))


arquivo = open("Frutas.txt", "r")
estoque = []

for fruta in arquivo:

    fruta = fruta.strip().upper()
    # print(fruta)
    estoque.append(fruta)
arquivo.close()
estoque_final = Feira(estoque)
x = len(estoque)
# x = 33

for i in range(x):
    print ("{} [{}]".format(estoque_final[i],i))

fruta_escolhida = int(input("Escolha um numero de acordo a fruta:"))
for escolha in estoque_final:
    if fruta_escolhida >= x or fruta_escolhida < 0:
        print("opção inválida")
        break
    else:
        print(f"Obrigado por escolher nosso serviço, {solicitante.nome} solicitou a fruta {estoque_final[fruta_escolhida]}")
        break

