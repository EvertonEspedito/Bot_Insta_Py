from time import sleep
from instabot import Bot

# Crie uma instância do bot
bot = Bot()

# Faça login na sua conta do Instagram
bot.login(username=input("Digite o seu Nome de Usuario: "), password=input("Digite Sua Senha: ")+"\n")

# Peça o username do concorrente
concorrente_username = input("Digite o username do concorrente: ")

# Obtenha os seguidores do concorrente
seguidores = bot.get_user_followers(concorrente_username)

# Itere sobre os seguidores e curta as 2 últimas fotos de cada um
for seguidor in seguidores:
    # Obtenha as 2 últimas fotos do seguidor
    fotos = bot.get_user_medias(seguidor, filtration=None)
    for foto in fotos[:2]:  # Pegue apenas as 2 últimas fotos
        # Curta a foto
        bot.like(foto)
        print(f"Fotografia curtida para {seguidor}")
        # Intervalo para não sobrecarregar o servidor do Instagram e evitar bloqueios
        sleep(10)  # Intervalo de 10 segundos entre cada curtida

# Logout do bot
bot.logout()
