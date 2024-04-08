print("conversão")

def converter_dolar_para_real(valor_dolar, cotacao_dolar ):
    valor_real = valor_dolar * cotacao_dolar
    return valor_real

cotacao = float(input("qual é a cotaçao do dolar em reais? R$ "))
valor_dolar = float(input("quanto em dolares voce deseja converter para reais? US$ "))

valor_convertido = converter_dolar_para_real(valor_dolar, cotacao_dolar )

print(f"o valor em reais é: R${valor_convertido:.2f}")
