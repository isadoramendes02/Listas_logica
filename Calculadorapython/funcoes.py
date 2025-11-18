def soma():
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    resultado = num1 + num2
    return resultado


def subtração():
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    resultado = num1 - num2
    return resultado


def multiplicação():
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    resultado = num1 * num2
    return resultado


def divisão():
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    if num2 == 0:
        return "Não pode realizar divisão por 0"
    else:
        resultado = num1 / num2
        return resultado