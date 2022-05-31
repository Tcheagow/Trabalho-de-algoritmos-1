import os #importanto a biblioteca os para ter acesso ao método que limpa o terminal

# função que irá apenas adicionar valores nos arryays principais
def AddingValuesInArrays(coordAbcissas, coordOrdenadas):
    #lendo a entrada
    coords = input().split()

    #Adicionando os arrays com as coord em outros arrays
    #Verificando qual é o maior x, pois irá me ajudar na função CheckOverlap()
    if int(coords[0]) <= int(coords[2]):
        coordAbcissas.append([int(coords[0]), int(coords[2])])
    else:
        coordAbcissas.append([int(coords[2]), int(coords[0])])
        
    #Verificando qual é o maior y, pois irá me ajudar na função CheckOverlap()
    if int(coords[1]) <= int(coords[3]):
        coordOrdenadas.append([int(coords[1]), int(coords[3])])
    else:
        coordOrdenadas.append([int(coords[3]), int(coords[1])])

# função que irá verificar a possibilidade de sobreposição
def CheckOverlap(coordAbcissas, coordOrdenadas, retangulos):
    posicao = 0 #var para auxiliar

    for j in range(1, len(coordAbcissas)):
        for k in range(2):
            if coordAbcissas[posicao][0] <= coordAbcissas[j][k] <= coordAbcissas[posicao][1] and coordOrdenadas[posicao][0] <= coordOrdenadas[j][k] <= coordOrdenadas[posicao][1]:
                print('ae krl')
        posicao += 1
        
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
            #limpando o terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Digite um valor válido')

#chamando a main function
main()