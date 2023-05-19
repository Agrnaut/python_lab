from Quadrado import Quadrado

def quer_continuar():
    valor = ((int(input("Gostaria de voltar ao menu anterior?\n [1] Sim\n [2] Não\n"))))
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
          "\n[1] Mostrar o tamanho dos lados "
          "\n[2] Calcular a área do seu quadrado"
          "\n[3] Mudar o tamanho do lado do seu quadrado"
                          "\nOpção: ")))

    # fim_de_loop = quer_continuar()

    for escolha in range(3):
        if(pergunta == 1):
            print(f"O Lado do seu quadrado é {quadrado_exercicio.tamanho}")
            fim_de_loop = quer_continuar()
            break
        elif(pergunta == 2):
            print(quadrado_exercicio.calculo())
            fim_de_loop = quer_continuar()
            break
        elif(pergunta == 3):
            quadrado_exercicio.novo_tamanho(float(input("Digite um novo tamanho para os lados do seu quadrado: ")))
            fim_de_loop = quer_continuar()
            break
        else:
            print("Opção inválida")

