import discord
import random
import string
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Respostas de "bom dia", "boa noite" e cumprimentos
respostas_bom_dia = [
    "bom dia s2",
    "bd",
    "dom bia",
    "bundinha",
    "quer café?",
    "clbc",
    "caboca",
    "xiu",
    "bom dia <3"
]

respostas_boa_noite = [
    "b noite",
    "boa noite s2",
    "noite boa :)",
    "clbc",
    "caboca",
    "xiu",
    "noa boite 3>",
    "dorme bem bb"
]

respostas_oi = [
    "oi bb",
    "oie",
    "turu bom?",
    "olar",
    "comu vai",
    "xiu",
    "clbc",
    "suave truta?",
    "salve",
    "oiii"
]

respostas_nazu = [
    "clbc",
    "xiu",
    "oi lindu",
    "oi lindan",
    "caboca",
    "que foi",
    "fala",
    "oi porra",
    "fala caralho",
    "man",
    "enche o saco n",
    "o cacete oi",
    "fala cmg n random",
    "habla miga",
    "oin"
]

respostas_personalizadas = {
    "bom dia": respostas_bom_dia,
    "bomdia": respostas_bom_dia,
    "b dia": respostas_bom_dia,
    "dom bia": respostas_bom_dia,
    "bd": respostas_bom_dia,
    "b d": respostas_bom_dia,
    "boa noite": respostas_boa_noite,
    "boanoite": respostas_boa_noite,
    "bn": respostas_boa_noite,
    "b n": respostas_boa_noite,
    "b noite": respostas_boa_noite,
    "noa boite": respostas_boa_noite,
    "bonoite": respostas_boa_noite,
    "oi": respostas_oi,
    "ola": respostas_oi,
    "olar": respostas_oi,
    "ois": respostas_oi,
    "salve": respostas_oi
}

# Respostas espontâneas (sem "nazu")
respostas_espontaneas = {
    "quem": "te comeu",
    "cade": "no meu cu que n tá",
    "que horas são": "falta só um poquin pra daqui a pouco",
    "que horas sao": "mei dia pras nove",
    "que hora são": "sei nao",
    "que hora sao": "hora de papá",
    "que hora e": "sim",
    "que hora é": "eu acho que é essa hora aí",
    "que horas é": "tenho cara de relogio carai?",
    "que horas e": "é hora, definitivamente",
    "leitada?": "leite*"
}

# Respostas que exigem "nazu"
respostas_com_prefixo = {
    "vai se fuder": "amanha eu penso nisso",
    "quer café": "ja tomei leitada",
    "quer cafe": "quero n",
    "grossa": "vo te mostra oq é grosso",
    "tá aí": "depende de quem pergunta"
}

# Letras isoladas (a → b, y → z, etc)
respostas_alfabeto = {letra: chr(ord(letra) + 1) for letra in string.ascii_lowercase[:-1]}
respostas_alfabeto["y"] = "z, ganhei otario"

@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    conteudo = message.content.lower().strip()

    # Letras isoladas
    if conteudo in respostas_alfabeto and len(conteudo) == 1:
        await message.channel.send(respostas_alfabeto[conteudo])
        return

    # Espontâneas
    if conteudo in respostas_espontaneas:
        await message.channel.send(respostas_espontaneas[conteudo])
        return

    # Personalizadas com "nazu"
    if "nazu" in conteudo:
        for chave, respostas in respostas_personalizadas.items():
            if chave in conteudo:
                await message.channel.send(random.choice(respostas))
                return

        for chave, resposta in respostas_com_prefixo.items():
            if chave in conteudo:
                await message.channel.send(resposta)
                return

        # Se só tiver "nazu" sem nenhuma outra palavra-chave
        if conteudo.strip() == "nazu":
            await message.channel.send(random.choice(respostas_nazu))
            return

    await bot.process_commands(message)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)