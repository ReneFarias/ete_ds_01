notas = []

contador = 1

while contador <= 5:
    # WHILE = ENQUANTO o contador for menor ou igual a 5 ele executa o codigo a seguuir:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1

    print( "quantidade de notas", len(notas) )