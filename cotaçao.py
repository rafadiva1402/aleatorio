print("cotaçao")

def converter_real_para_dolar(valor_real, cotaçao_dolar):
    valor_dolar = valor_real / cotaçao_dolar
    return valor_dolar

cotaçao_dolar = float(input("qual é a cotaçao atual do dolar em reais? R$ "))
valor_real = float(input("quantos reais voce deseja converter para dolares? R$ "))

valor_convertido = converter_real_para_dolar(valor_real, cotaçao_dolar)

print(f'o valor em dolares é: US$ {valor_convertido:.2f}')