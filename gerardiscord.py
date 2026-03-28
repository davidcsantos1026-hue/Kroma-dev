import discord
from discord import app_commands
from discord.ext import commands

# Configuração básica
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

class KromaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Isto sincroniza os comandos "/" com o Discord
        await self.tree.sync()
        print(f"✅ Slash Commands sincronizados!")

bot = KromaBot()

# --- DICIONÁRIO DE TEMAS ---
TEMAS = {
    "organizacao": {
        "cargos": [("Chefe", 0x9B59B6), ("🔰┆Admin", 0x2ECC71), ("Sub-chefe", 0x3498DB), ("Oficial", 0x2ECC71), ("Recruta", 0x2ECC71), ("Morador", 0x2ECC71), ("😈┆Organização", 0x2ECC71), ("🤝🏻Amigo", 0x2ECC71), ("🤝🏻Parceria 1", 0x2ECC71), ("🤝🏻Parceria 2", 0x2ECC71), ("🤝🏻Parceria 3", 0x2ECC71),("👤Civil", 0x2ECC71)],
        "categorias": {
            "CHEFES": ["💬┆chat-chefes", "📦┆bau-chefes"],
            "RECEPÇÃO": ["🛬┆entradas", "🛫┆saidas", "🚨┆regras"],
            "COMUNIDADE": ["💬┆chat", "📢┆comunicados", "⌛┆ausências", "📦┆bau-geral", "📍┆spots", "🎯┆meta-semanal", "📑┆informações", "🛠️┆craft-materiais", "👕┆roupa", "📱┆imagens", "🎬┆clips", "📸┆eventos", "🎥┆streamer"],
            "CALL": ["🔊┆Call 1", "🔊┆Call 2", "🔊┆Call 3", "🔊┆Convício", "💤┆AFK"],
            "PREÇÁRIO": ["💲┆civil", "💲┆parceria"],
            "ECONOMIA": ["🚚┆encomendas", "💸┆vendas"],
            "PARCERIAS": ["🤝🏻┆parceria-1", "🤝🏻┆parceria-2", "🤝🏻┆parceria-3"]
        }
    },
    "comunidade_fivem": {
        "cargos": [("Fundador", 0xFFD700), ("🎮 Player", 0x3498DB)],
        "categorias": {
            "STAFF": ["chat-staff-líder", "chat-staff", "chat-discord", "chat-dev", "chat-dev-car", "chat-designer", "comunicados", "anúncios", "informações", "comandos", "bugs", "ausências", "sugestões"],
            "RECEPÇÃO": ["entradas", "saidas", "verificação"],
            "INFORMAÇÕES": ["regras", "comunicados", "atualizações", "regras-atualizações", "status", "comunicados-sorteios", "sorteios", "top-semanal", "top-mensal", "punições", "spoiler", "votações", "boost-discord", "duvidas"],
            "COMUNIDADE": ["chat-geral", "pontos", "sugestões", "debate-sugestões", "anncios", "info-self", "eventos", "feedback-staff", "feedback-carros", "bugs", "cooldown", "anúncios-orgs", "votações-orgs"],
            "SUPORTE": ["Ticket", "sala de espera", "suporte-comunidade", "Suporte 1", "Supprte 2", "Suporte 3", "Suporte 4", "Suporte 5", "Reuniões", "Reuniões staff lider", "Reuniões discord", "Reuniões dev", "Reuniões designer", "Reuniões dev car", "Convívio 1", "Convívio 2", "Convívio 3"],
            "VIP": ["chat-vip-geral", "chat-vip-1", "chat-vip-2", "chat-vip-3", "chat-vip-4", "chat-vip-5", "anúncios-loja", "loja"],
            "STREAMERS": ["chat-streamers-geral", "chat-streamer-oficial", "chat-streamer-vip", "chat-streamer", "streamer-oficial", "streamer-vip", "streamer", "requesitos-streamer"],
            "FAQ'S": ["trabalho-legal-1", "trabalho-legal-2", "trabalho-legal-3", "trabalho-legal-4", "trabalho-legal-5"],
            "FAQ'S": ["trabalho-ilegal-1", "trabalho-ilegal-2", "trabalho-ilegal-3", "trabalho-ilegal-4", "trabalho-ilegal-5"],
            "FAQ'S": ["preçario", "bagageiras", "comandos", "limapr-cache", "lag-visual", "lategame"],
            "MÍDIA": ["imagens", "highlights", "clips", "redes-sociais"],
            "CANDIDATURAS": ["requesitos-staff", "candidatura-staff", "requesitos-dev", "candidatura-dev", "requesitos-design", "candidatura-design", "requesitos-screen-share", "candidatura-screen-share"],
            "PARCERIAS": ["parceria-1", "parceria-2", "parceria-3", "parceria-4", "parceria-5"],
            "GESTOR ORGANIZAÇÕES LEGAIS": ["chat", "comunicados", "anúncios", "pedir-tag", "rádios", "organização-legal-1", "organização-legal-2", "organização-legal-3", "organização-legal-4", "organização-legal-5"],
            "GESTOR ORGANIZAÇÕES ILEGAIS": ["chat", "comunicados", "anúncios", "pedir-tag", "rádios", "organização-ilegal-1", "organização-ilegal-2", "organização-ilegal-3", "oeganização-ilegal-4", "organização-ilegal-5", "organização-ilegal-6", "organização-ilegal-7", "oeganização-ilegal-8"]       
        }
    },
    "comunidade_streamers": {
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
