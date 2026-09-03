import random

def play():
    usuario = input("Faça sua escolha, meu nobre! 'pedra', 'papel' ou 'tesoura', e que os jogos comecem!\n")
    computador = random.choice(['pedra', 'papel', 'tesoura'])
    print("Seu oponente escolheu", (computador))

    if usuario == computador:
        return 'Foi empate, meu nobre!'
    
    # pedra > tesoura, tesoura > papel, papel > pedra
    if vencedor(usuario, computador):
        return 'Parabéns, meu nobre! Você ganhou!'
    
    return 'Vacilou, meu nobre, tente de novo!'
    
def vencedor(jogador, oponente):
    #return true se o jogador for o vencedor
    # pedra > tesoura, tesoura > papel, papel > pedra

    if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel') \
        or (jogador == 'papel' and oponente == 'pedra') :
        return True
    
print(play())