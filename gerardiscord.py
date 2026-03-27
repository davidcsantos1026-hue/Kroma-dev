import discord
from discord import app_commands
from discord.ext import commands

# Configuração básica
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Isto sincroniza os comandos "/" com o Discord
        await self.tree.sync()
        print(f"✅ Slash Commands sincronizados!")

bot = MyBot()

# --- DICIONÁRIO DE TEMAS ---
TEMAS = {
    "organizacao": {
        "cargos": [("Chefe", 0x9B59B6), ("Admin", 0x2ECC71), ("Sub-chefe", 0x3498DB), ("Oficial", 0x2ECC71), ("Recruta", 0x2ECC71), ("Morador", 0x2ECC71), ("Organização", 0x2ECC71), ("Amigo", 0x2ECC71), ("Parceria 1", 0x2ECC71), ("Parceria 2", 0x2ECC71), ("Parceria 3", 0x2ECC71),("Civil", 0x2ECC71)],
        "categorias": {
            "RECEPÇÃO": ["🛬┆entradas", "🛫┆saidas", "🚨┆regras"],
            "COMUNIDADE": ["💬┆chat", "📢┆comunicados", "⌛┆ausências", "📦┆bau-geral", "📍┆spots", "🎯┆meta-semanal", "📑┆informações", "🛠️┆craft-materiais", "👕┆roupa", "📱┆imagens", "🎬┆clips", "📸┆eventos"],
            "CALL": ["🔊┆Call 1", "🔊┆Call 2", "🔊┆Call 3", "🔊┆Convício", "💤┆AFK"],
            "PREÇÁRIO": ["💲┆civil", "💲┆parceria"],
            "ECONOMIA": ["🚚┆encomendas", "💸┆vendas"],
            "PARCERIAS": ["🤝🏻┆parceria_1", "🤝🏻┆parceria_2", "🤝🏻┆parceria_3"]
        }
    },
    "comunidade_creador_conteudo": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Comunidade_fivem": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Clã": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Comunidade_estudo": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Agencia_design": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Servidor_vendas": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Desenvolvedor": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Desporto": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    },
    "Torneio": {
        "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
            "🎮 JOGOS": ["🕹️-procurar-grupo"]
        }
    }
}

@bot.event
async def on_ready():
    print(f'🚀 Bot online como {bot.user}')

# COMANDO SLASH: /gerar
@bot.tree.command(name="gerar", description="Cria a estrutura do servidor (Apenas para o Dono)")
@app_commands.describe(tema="Escolhe o tema do servidor (ex: organizacao, Comunidade_creador_conteudo, Comunidade_fivem, Clã, Comunidade_estudo, Agencia_design, Servidor_vendas, Desenvolvedor, Desporto, Torneio)")
async def gerar(interaction: discord.Interaction, tema: str):
    tema = tema.lower()
    guild = interaction.guild

    # VERIFICAÇÃO: Apenas o Fundador (Owner) do servidor pode usar
    if interaction.user.id != guild.owner_id:
        await interaction.response.send_message("❌ Erro: Apenas o **Fundador** do servidor pode usar este comando!", ephemeral=True)
        return

    if tema not in TEMAS:
        await interaction.response.send_message(f"❌ Tema inválido! Escolhe: `trade` ou `gaming`.", ephemeral=True)
        return

    # Responder imediatamente para evitar erro de timeout do Discord
    await interaction.response.send_message(f"🏗️ A iniciar construção do tema **{tema.upper()}**...", ephemeral=True)

    config = TEMAS[tema]

    # 1. CRIAR CARGOS
    for nome_cargo, cor in config["cargos"]:
        if not discord.utils.get(guild.roles, name=nome_cargo):
            await guild.create_role(name=nome_cargo, color=discord.Color(cor), hoist=True)

    # 2. CRIAR CATEGORIAS E CANAIS
    for cat_nome, canais in config["categorias"].items():
        categoria = await guild.create_category(cat_nome)
        for canal_nome in canais:
            if "🔈" in canal_nome:
                await guild.create_voice_channel(canal_nome, category=categoria)
            else:
                await guild.create_text_channel(canal_nome, category=categoria)

    await interaction.followup.send(f"✅ Estrutura **{tema.upper()}** concluída com sucesso!")

# Substitui pelo teu Token real
bot.run('TOCKEN DISCORD')
