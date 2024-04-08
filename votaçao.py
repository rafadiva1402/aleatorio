print("votacao")

def calcular_percentual(valor, total):
    if total == 0:
        return 0
    else:
        return (valor / total) * 100

print("Por favor, informe a quantidade de votos para cada candidato: ")
votos_validos_a = int(input(" votos validos para o candidato A: "))
votos_validos_b = int(input(" votos validos para o candidato B: "))
votos_validos_c = int(input(" votos validos para o candidato C: "))
votos_nulos = int(input(" votos nulos: "))
votos_brancos = int(input(" votos em branco: "))

total_eleitores = votos_validos_a + votos_validos_b + votos_validos_c + votos_nulos + votos_brancos

percentual_validos = calcular_percentual(votos_validos_a + votos_validos_b + votos_validos_c, total_eleitores)
percentual_validos_a = calcular_percentual(votos_validos_a, total_eleitores)
percentual_validos_b = calcular_percentual(votos_validos_b, total_eleitores)
percentual_validos_c = calcular_percentual(votos_validos_c, total_eleitores)
percentual_nulos = calcular_percentual(votos_nulos, total_eleitores)
percentual_brancos = calcular_percentual(votos_brancos, total_eleitores)

print("\nResultados da Eleição: ")
print(f"numero total de eleitores: {total_eleitores}")
print(f"percentual de votos validos: {percentual_validos:.2f}%")
print(f"percentual de votos validos para candidatos A: {percentual_validos_a:.2f}%")
print(f"percentual de votos validos para candidatos B: {percentual_validos_b:.2f}%")
print(f"percentual de votos validos para candidatos C: {percentual_validos_c:.2f}%")
print(f"percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"percentual de votos brancos: {percentual_brancos:.2f}%")