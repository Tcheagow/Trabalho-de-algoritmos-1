import os #importanto a biblioteca os para ter acesso ao método que limpa o terminal

# função que irá apenas adicionar valores nos arryays principais
def AddingValuesInArrays(coordAbcissas, coordOrdenadas):
    #lendo a entrada
    coords = input().split()

    #Adicionando os arrays com as coord em outros arrays
    coordAbcissas.append([int(coords[0]), int(coords[2])])
    coordOrdenadas.append([int(coords[1]), int(coords[3])])

# função que irá verificar a possibilidade de sobreposição
def CheckOverlap(coordAbcissas, coordOrdenadas):
    retang = []

    #verificando qual a menor abcissa
    if coordAbcissas[0][0] <= coordAbcissas[1][0]:
        retang.append(coordAbcissas[0][0])
    else:
        retang.append(coordAbcissas[1][0])

    #verificando qual a maior ordenada 
    if coordOrdenadas[0][0] >= coordOrdenadas[1][0]:
        retang.append(coordOrdenadas[0][0])
    else:
        retang.append(coordOrdenadas[1][0])

    #verificando qual a maior abcissa
    if coordAbcissas[0][1] >= coordAbcissas[1][1]:
        retang.append(coordAbcissas[0][1])
    else:
        retang.append(coordAbcissas[1][1])
    
    #verificando qual a menor ordenada 
    if coordOrdenadas[0][1] <= coordOrdenadas[1][1]:
        retang.append(coordOrdenadas[0][1])
    else:
        retang.append(coordOrdenadas[1][1])

    coordAbcissas.clear()
    coordOrdenadas.clear()

    coordAbcissas.append([retang[0], retang[2]])
    coordOrdenadas.append([retang[1], retang[3]])


# main function (apenas para manter uma organização)
def main():
    i = 0
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
                CheckOverlap(coordAbscissas, coordOrdenadas) 
        elif opcao == '2':
            break
        else: 
            #limpando o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Digite um valor válido')
    print(1)
    print(f'({coordAbscissas[0][0]},{coordOrdenadas[0][0]}), ({coordAbscissas[0][1]},{coordOrdenadas[0][1]})')
#chamando a main function
main()