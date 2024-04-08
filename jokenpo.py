print("jokenpo")

from colorama import fore, style

 def verificar_vencedor(jogador1, jogador2 ):
     if jogador1 == jogador2:
         return fore.YELLOW + "empate" + style.RESET_ALL
     elif(jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "tesoura" and jogador2 == "papel") or \
         (jogador1 == "papel" and jogador2 == "pedra") :
         return fore.GREEN + "jogador 1 vence" + style.RESET_ALL
     else:
        return fore.BLUE + "jogador 2 vence" + style.RESET_ALL

def main():
    print(fore.CYAN+ "bem-vindo ao jogo jokenpo!" + style.RESET_ALL)

    while true:
        jogador1 = input("jogador1, escolha pedra,papel ou tesoura: ").capitalize()
        jogador2 = input("jogador2, escolha pedra,papel ou tesoura: ").capitalize()

        if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]
            print(fore.RED + "Opçao invalida. por favor, escolha apenas entre pedra, papel ou tesoura")
            continue




