salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
# esse ELIF signifia OU ENTÃO; else if em outras linguagens; e esse AND é mais uma condicao, condicão E
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerent de projetos")