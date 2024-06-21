import random

def get_escolha():
    return random.choice(["pedra", "papel", "tesoura"])

def vencedor(usuario, bot):
    if usuario == bot:
        return "Empate!"
    elif (usuario == "pedra" and bot == "tesoura") or (usuario == "papel" and bot == "pedra") or (usuario == "tesoura" and bot == "papel"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
usuario_escolha = get_escolha()
bot_escolha = get_escolha()

print("Você escolheu:",usuario_escolha)
print("O computador escolheu:",bot_escolha)

print(vencedor(usuario_escolha, bot_escolha))

print("Obrigado por jogar!")
