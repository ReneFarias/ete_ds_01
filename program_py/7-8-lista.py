lista_numeros = [1, 2, 3]
# aqui vemos como são criadas as listas, elas estão dentro de [], e separadas por , e esta em uma indice, o 1 é a indice 0, o 2 é indice 1, e assim por diante


print(lista_numeros[0])
# seleciona a indice 0, que é o valor 1
print(lista_numeros[1])
print(lista_numeros[2])

numeros = [1, 2, 3]
strings = ["João", "Maria", "Bruxa"]
decimais = [10.8, 15.2, 33.3]

print(numeros)
print(strings)
print(decimais)


lista_vazia = []
# cria uma lista vazia
lista_vazia.append("Olá")
# metodo append inclui valores na lista
# existe outros metodos como: insert, pop, sort, reverse, index, count, remove
lista_vazia.append("Mundo")

print(lista_vazia)

# mais exemplos de metodos abaixo
numerosMetodos = [10, 9, 8, 7, 6]

print( "total:", len(numerosMetodos) )
print( "menor valor:", min(numerosMetodos) )
print( "maior valor:", max(numerosMetodos) )