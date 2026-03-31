import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOCKEN = os.getenv("DISCORD_TOCKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class Kroma(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!", 
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        print("--- 📂 A carregar Cogs ---")

        if not os.path.exists('./cogs'):
            os.makedirs('./cogs')

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'✅ Carregado: {filename}')
                except Exception as e:
                    print(f'❌ Erro ao carregar {filename}: {e}')

        await self.tree.sync()
        print("--- ✨ Sincronização concluída ---")

bot = Kroma()

@bot.event
async def on_ready():
    print(f'🚀 Bot online como {bot.user}')
    print(f'📂 ID do Bot: {bot.user.id}')
    await bot.change_presence(activity=discord.Game(name="A gerir o seu servidor!"))

async def main():
    async with bot:
        if DISCORD_TOCKEN is None:
            print("❌ ERRO: O Token não foi encontrado no teu ficheiro .env!")
            return

        await bot.start(DISCORD_TOCKEN)

async def carregar_modulos():
    # Lista de ficheiros .py que queres carregar como extensões
    modulos = [
        'personalizacaoperfil',
        'permissoes_organizacao',
        'gerardiscord' # Adicionei este pois é o ficheiro principal que estivemos a falar
    ]

    for modulo in modulos:
        try:
            await bot.load_extension(modulo)
            print(f"✔️ Módulo '{modulo}' carregado com sucesso!")
        except Exception as e:
            print(f"❌ Falha ao carregar módulo '{modulo}': {e}")

@bot.event
async def on_ready():
    print(f'--- Bot Online ---')
    print(f'Nome: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'------------------')

async def iniciar():
    async with bot:
        await carregar_modulos()
        # SUBSTITUI PELO TEU TOKEN REAL
        await bot.start('TEU_TOKEN_AQUI_DENTRO_DAS_ASPAS')

if __name__ == "__main__":
    try:
        asyncio.run(iniciar())
    except KeyboardInterrupt:
        print("Bot desligado.")
