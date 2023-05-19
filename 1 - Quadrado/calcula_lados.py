from Quadrado import Quadrado

def quer_continuar(valor):
    if (valor == 1):
        return False
    else:
        return True

print("Bem vindo Aluno")

#quadrado_exercicio = input("digite o nome do seu quadrado: ").strip().upper()

quadrado_exercicio = Quadrado(float(input("Digite um tamanho para os lados do seu quadrado: ")))


fim_de_loop = False

while(not fim_de_loop):
    pergunta = int(input(("Você gostaria de "
          "\n[1] Mostrar o tamanho do lado e o calculo da área: "
          "\n[2] Mudar o tamanho do lado do seu quadrado:\n: ")))
    if (pergunta < 0 or pergunta > 2):
        print("opção inválida! Escolha outra\n")
        continue
    elif(pergunta == 1):
        quadrado_exercicio.mostra_e_calcula
        fim_de_loop = quer_continuar((int(input("Gostaria de voltar ao menu anterior?\n [1] Sim\n [2] Não\n"))))
    else:
        quadrado_exercicio.muda_tamanho_lado(float(input("Digite o novo lado do seu quadrado: ")))
        continue

