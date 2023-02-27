# 9.13
from random import randint, choice

class Dados:

    def __init__(self, caras=6):
        self.caras= caras
    
    def tirar_dado(self):
        """Imprime un numero aleatorio entre 1 y el numero de caras del dado."""
        print(randint(1, self.caras))

dado_6 = Dados()

dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()
dado_6.tirar_dado()

dado_10 = Dados(10)

dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()
dado_10.tirar_dado()

dado_20 = Dados(20)

dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()
dado_20.tirar_dado()

# 9.14

lista_loteria =  [0,1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e']

boleto_premiado = []

for select in range(4):
    boleto_premiado.append(choice(lista_loteria))

print(f"El boleto premiado es: {boleto_premiado}")

# 9.15

mi_boleto = [0,3,4,'a']
boleto_premiado = []
count = 0
while True:
    
    for select in range(4):
        boleto_premiado.append(choice(lista_loteria))
    if boleto_premiado == mi_boleto:
        break
    boleto_premiado = []
    count += 1
print(count)
