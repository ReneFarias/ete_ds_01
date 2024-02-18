# condicionais torna o script mais dinamico, deixa o fluxo do programa dinamico
idade = int( input("Irnforme a sua idade: ") )

if idade >= 18:
# if = SE a idade é maior ou igual a 18, se sim executa o prox comando, se nn ele passa para o proximo
    print("PERMITIDO!")
else:
# else = SE NÃO então aqui executa o comando a seguir
    print("BLOQUEADO!")