from Comodo import Comodo
from Retangulo import Retangulo

print("*********Bem vindo*********"
      "\nEste programa foi feito para calcular quantos pisos seriam necessários para um comodo")

print("Utilize o ponto ( . ) no lugar da virgula, por exemplo 139.92 ")
piso_compri = (float(input("Por favor, digite o comprimento do seu piso em cm: ")))
piso_largu = (float(input("Por favor, digite o largura do seu piso em cm: ")))

piso = Retangulo(piso_compri, piso_largu)

comodo_compri = (float(input("Por favor, digite o comprimento do seu comodo em metros: ")))
comodo_largu = (float(input("Por favor, digite o largura do seu comodo em metros: ")))

comodo = Comodo(comodo_compri, comodo_largu)

comodo_m2 = comodo.calcula_m2()
piso_cm2 = piso.calcular_cm2()

primeiro_calculo = round(comodo_m2) * 10000
calculo_final = (primeiro_calculo / piso_cm2)

print("Você precisará de {} pisos para o seu comodo".format(round(calculo_final)))