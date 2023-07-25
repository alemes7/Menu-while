
print("Menu")
print(" ")
print("1-Número primo")
print("2-Número decrescente")
print("3-Mediana de 3 números")
print("4-Sair")
a = input("Digite a função que deseja:")
s = 1

while s==1:
    Primo = "1"
    Decrescente = "2"
    Mediana = "3"

    sim = "y"
    não = "n"


    if a == Primo:
        print("Você escolheu número primo.")
        b = float(input("Digite o valor que deseja para realizar a operação:"))
        if b%2 == 0 and b!=2 or b%3==0 and b!=3 or b%5==0 and b!=5 or b%7==0 and b!=7:
            print("O número não é primo.")
        elif b==1:
            print("O número não é primo.")
        else:
            print("O número é primo.")

        if s == 1:
            print("Escola uma opção:")
            print("Logica - L")
            print("Refazer - R")
            print("Voltar - V")
            print("Sair - S")
        
    Logica = "L"
    Refazer = "R"
    Voltar = "V"
    Sair = "S"

    t=(input(""))
    if t == Logica:
        s = 1
        print("Função indisponivel")
        
    else:
        print(" ")
        print("Código invalido")
        print(" ")

        z=(input(""))

        if z == sim:
            s = 0
        elif z == não:
            S = 1
        else:
            print(" ")
            print("Código invalido")
            print(" ")
        
    if a == Decrescente:
        print("Você escolheu número decrescente.")
        print(" ")
        x=int(input("Insira um valor para decrescente:"))

        while x >= 0:
            print(x)
            x = x -1

    if a == Mediana:
        F = int(input("Informe o 1° valor de sua mediana: ")) 
        D = int(input("Informe o 2° valor de sua mediana: ")) 
        C = int(input("Informe o 3° valor de sua mediana: "))

        if F > D and F > C:
            MAX1 = F
            if D > C:
                print(f"A mediana é: {D}")
            else:
                print(f"A mediana é: {C}")
        if D > F and D > C:
            MAX1 = D
            if F > C:
                print(f"A mediana é: {F}")
            else:
                print(f"A mediana é: {C}")
        if C > F and C > D:
            MAX1 = C 
            if F > D:
                print(f"A mediana é: {F}")
            else:
                print(f"A mediana é: {D}")


