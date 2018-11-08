def selectionSort(vetor):

    print(vetor)

    i = 0
    while i < len(vetor) - 1:

        menor = i
        j = i + 1

        while j < len(vetor):
            if vetor[j] < vetor[menor]:
                menor = j
            j+=1

        if menor != i:
            temp = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = temp

        i+=1
        print(vetor)

    print(vetor)

lista = [7,4,2,9,18,1]
v = selectionSort(lista)

def bubble_sort(vetor):

    print(vetor)

    ordenado = False
    while ordenado != True:

        ordenado = True
        j = 0
        while j < len(vetor)-1:
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp

                ordenado = False
            j += 1

        print(vetor)

    print(vetor)

lista = [7,4,2,9,18,1]
v = bubble_sort(lista)
