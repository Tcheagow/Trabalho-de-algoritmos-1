def AddingValuesInArrays(coordAbcissas, coordOrdenadas):
    #lendo a entrada
    coords = input().split()

    #adicionando os arrays com as coord em outros arrays
    coordAbcissas.append([int(coords[0]), int(coords[2])])
    coordOrdenadas.append([int(coords[1]), int(coords[3])])

# main function (apenas para manter uma organização)
def main():
    i = 0
    contRetangulos = 0 
    coordAbscissas = []
    coordOrdenadas = []

    while i < 100:
        try:
            #adicionando valores nos arrays
            AddingValuesInArrays(coordAbscissas, coordOrdenadas)

            #verificar se o número de ratangulos é maior que 1
            if contRetangulos > 1:
                pass
            else:
                pass
        except EOFError:
            break

#chamando a main function
main()