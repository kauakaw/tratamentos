while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))

        conta = n1 / n2

    except ZeroDivisionError:
        print("Não é possivel dividir nada por zero! TENTE NOVEMENTE")
    except ValueError:
        print("Não é possivel dividir por letras ou números decimais! TENTE NOVAMENTE")
    else:
        print(f'{n1} dividido por {n2} é igual a  {round(conta, 2)}')
        break