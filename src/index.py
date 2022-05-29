# função que irá apenas adicionar valores nos arryays principais
from tabnanny import check


def AddingValuesInArrays(coordAbcissas, coordOrdenadas):
    #lendo a entrada
    coords = input().split()

    #adicionando os arrays com as coord em outros arrays
    coordAbcissas.append([int(coords[0]), int(coords[2])])
    coordOrdenadas.append([int(coords[1]), int(coords[3])])

# função que irá verificar a possibilidade de sobreposição
def CheckOverlap(coordAbcissas, coordOrdenadas, retangulos):
    print("oi")

# main function (apenas para manter uma organização)
def main():
    i = 0
    retangulos = []
    coordAbscissas = []
    coordOrdenadas = []

    while i < 100:
        print('Deseja incluir um novo retângulo? 1- Sim; 2- Não')
        opcao = input()

        if opcao == '1':
            #adicionando valores nos arrays
            AddingValuesInArrays(coordAbscissas, coordOrdenadas)

            #incrementando a váriavel i
            i += 1

            #verifica se o número de ratangulos é maior que 1. Caso seja, verifica sobreposição
            if len(coordOrdenadas) > 1:
                CheckOverlap(coordAbscissas, coordOrdenadas, retangulos)

        elif opcao == '2':
            break
        else: 
            print('Digite um valor válido')

#chamando a main function
main()