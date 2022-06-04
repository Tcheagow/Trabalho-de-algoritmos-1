#Código feito por Thiago Aparecido
import os #importanto a biblioteca os para ter acesso ao método que limpa o terminal

# função que irá apenas adicionar valores nos arrays principais
def AddingValuesInArrays(coordAbcissas, coordOrdenadas):
    #pedindo para o usuário digitar as coordenadas conforme proposto no trabalho
    print('Digite as coordenadas conforme pedido no trabalho')
    
    #lendo a entrada
    coords = input().split()

    #Adicionando os arrays com as coord nos arrays principais
    coordAbcissas.append([int(coords[0]), int(coords[2])])
    coordOrdenadas.append([int(coords[1]), int(coords[3])])

# função que irá criar o retângulo maior
def createNewRectangle(coordAbcissas, coordOrdenadas):
    #var auxiliar
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

    #limpando todos os valores dentro dos arrays principais
    coordAbcissas.clear()
    coordOrdenadas.clear()

    #adcionando novos valores nos arrays principais
    coordAbcissas.append([retang[0], retang[2]])
    coordOrdenadas.append([retang[1], retang[3]])

# main function (apenas para manter uma organização)
def main():
    #variavel para incrementar
    i = 0
    #arrays principais
    coordAbscissas = []
    coordOrdenadas = []

    while i < 100:
        #verificando o que o user deseja fazer
        print('Deseja incluir um novo retângulo? 1- Sim; 2- Não')
        opcao = input()

        if opcao == '1':
            #adicionando valores nos arrays
            AddingValuesInArrays(coordAbscissas, coordOrdenadas)

            #incrementando a váriavel i
            i += 1

            #verifica se o número de ratangulos é maior que 1. Caso seja, cria o menor retângulo que contenha os outros
            if len(coordOrdenadas) > 1:
                createNewRectangle(coordAbscissas, coordOrdenadas) 
        elif opcao == '2':
            break
        else: 
            #limpando o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Digite um valor válido')
    
    # verificando tamanho do etor principal para saber o que imprimir
    if len(coordAbscissas) == 0:
        print("Você não digitou nenhum retângulo")
    else:
        #printando o que foi proposto no trabalho conforme pedido no pdf
        print(1)
        print(f'({coordAbscissas[0][0]},{coordOrdenadas[0][0]}), ({coordAbscissas[0][1]},{coordOrdenadas[0][1]})')

#chamando a main function
main()