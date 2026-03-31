import discord
from discord import app_commands
from discord.ext import commands
import asyncio

# --- DICIONÁRIO DE TEMAS ---
TEMAS = {
    "organizacao": {
        "cargos": [
            ("Chefe", 0x9B59B6),
            ("🔰┆Admin", 0x2ECC71),
            ("Sub-chefe", 0x3498DB),
            ("Oficial", 0x2ECC71),
            ("Recruta", 0x2ECC71),
            ("Morador", 0x2ECC71),
            ("😈┆Organização", 0x2ECC71),
            ("🤝🏻Amigo", 0x2ECC71),
            ("🤝🏻Parceria 1", 0x2ECC71),
            ("🤝🏻Parceria 2", 0x2ECC71),
            ("🤝🏻Parceria 3", 0x2ECC71),
            ("👤Civil", 0x2ECC71),
        ],
        "categorias": {
            "CHEFES": [
                "💬┆chat-chefes", 
                "📦┆bau-chefes"
            ],
            "RECEPÇÃO": [
                "🛬┆entradas", 
                "🛫┆saidas", 
                "🚨┆regras"
            ],
            "COMUNIDADE": [
                "💬┆chat",
                "📢┆comunicados",
                "⌛┆ausências",
                "📦┆bau-geral",
                "📍┆spots",
                "🎯┆meta-semanal",
                "📑┆informações",
                "🛠️┆craft-materiais",
                "👕┆roupa",
                "📱┆imagens",
                "🎬┆clips",
                "📸┆eventos",
                "🎥┆streamer",
            ],
            "CALL": [
                "🔊┆Call 1", 
                "🔊┆Call 2", 
                "🔊┆Call 3", 
                "🔊┆Convício", 
                "💤┆AFK"
            ],
            "PREÇÁRIO": [
                "💲┆civil", 
                "💲┆parceria"
            ],
            "ECONOMIA": [
                "🚚┆encomendas", 
                "💸┆vendas"
            ],
            "PARCERIAS": [
                "🤝🏻┆parceria-1", 
                "🤝🏻┆parceria-2", 
                "🤝🏻┆parceria-3"
            ],
        },
    },
    "comunidade_fivem": {
        "cargos": [
            ("👑┆Fundador", 0xFFD700),
            ("🔰┆Staff líder", 0x3498DB),
            ("🔰┆Suporte", 0xFFD700),
            ("🔰┆Moderador", 0x3498DB),
            ("🔰┆Estagiário", 0xFFD700),
            ("🔰┆Staff", 0x3498DB),
            ("</>┆Developer", 0x3498DB),
            ("✏️┆Designer", 0x3498DB),
            ("💻┆Screen share", 0x3498DB),
            ("⚙️┆Dev car", 0x3498DB),
            ("📋┆Gestor de organizações legais", 0x3498DB),
            ("📋┆Gestor de organizações ilegais", 0x3498DB),
            ("📋┆Gestor de ticket", 0x3498DB),
            ("📋┆Gestor de creadores de conteúdo", 0x3498DB),
            ("📋┆Gestor de tags", 0x3498DB),
            ("📋┆Gestor de eventos", 0x3498DB),
            ("📋┆Gestor de VIP", 0x3498DB),
            ("💎┆vip 1", 0xFFD700),
            ("💎┆vip 2", 0x3498DB),
            ("💎┆vip 3", 0xFFD700),
            ("💎┆vip 4", 0x3498DB),
            ("💎┆vip 5", 0xFFD700),
            ("🎥┆Streamer Oficial", 0x3498DB),
            ("🎥┆Streamer Vip", 0xFFD700),
            ("🎥┆Streamer", 0x3498DB),
            ("💼┆Chefe de organização legal 1", 0x3498DB),
            ("💼┆Organização legal 1", 0x3498DB),
            ("💼┆Chefe de organização legal 2", 0x3498DB),
            ("💼┆Organização legal 2", 0x3498DB),
            ("💼┆Chefe de organização legal 3", 0x3498DB),
            ("💼┆Organização legal 3", 0x3498DB),
            ("💼┆Chefe de organização legal 4", 0x3498DB),
            ("💼┆Organização legal 4", 0x3498DB),
            ("💼┆Chefe de organização legal 5", 0x3498DB),
            ("💼┆Organização legal 5", 0x3498DB),
            ("💀┆Chefe de organização ilegal 1", 0x3498DB),
            ("💀┆Organização ilegal 1", 0x3498DB),
            ("💀┆Chefe de organização ilegal 2", 0x3498DB),
            ("💀┆Organização ilegal 2", 0x3498DB),
            ("💀┆Chefe de organização ilegal 3", 0x3498DB),
            ("💀┆Organização ilegal 3", 0x3498DB),
            ("💀┆Chefe de organização ilegal 4", 0x3498DB),
            ("💀┆Organização ilegal 4", 0x3498DB),
            ("💀┆Chefe de organização ilegal 5", 0x3498DB),
            ("💀┆Organização ilegal 5", 0x3498DB),
            ("💀┆Chefe de organização ilegal 6", 0x3498DB),
            ("💀┆Organização ilegal 6", 0x3498DB),
            ("💀┆Chefe de organização ilegal 7", 0x3498DB),
            ("💀┆Organização ilegal 7", 0x3498DB),
            ("💀┆Chefe de organização ilegal 8", 0x3498DB),
            ("💀┆Organização ilegal 8", 0x3498DB),
            ("🚫┆White list block", 0x3498DB),
            ("✅┆Verificado", 0xFFD700),
            ("👤┆Civil", 0x3498DB),
        ],
        "categorias": {
            "STAFF": [
                "💬┆chat-staff-líder",
                "💬┆chat-staff",
                "💬┆chat-discord-developer",
                "💬┆chat-dev",
                "💬┆chat-dev-car",
                "💬┆chat-designer",
                "📢┆comunicados",
                "📢┆anúncios",
                "📌┆informações",
                "⌨️┆comandos",
                "❌┆bugs",
                "⌛┆ausências",
                "📫┆sugestões",
            ],
            "RECEPÇÃO": [
                "🛬 ┆entradas", 
                "🛫┆saidas", 
                "✅┆verificação"
            ],
            "INFORMAÇÕES": [
                "🚨┆regras",
                "📢┆comunicados",
                "📣┆atualizações",
                "📢┆regras-atualizações",
                "📊┆status",
                "📢┆comunicados-sorteios",
                "🎉┆sorteios",
                "🏆┆top-semanal",
                "🏆┆top-mensal",
                "⛔┆punições",
                "👀┆spoiler",
                "📊┆votações",
                "🚀┆boost-discord",
                "❓┆dúvidas",
            ],
            "COMUNIDADE": [
                "💬┆chat-geral",
                "🔵┆pontos",
                "📫┆sugestões",
                "🗪┆debate-sugestões",
                "📢┆anúncios",
                "ℹ️┆info-self",
                "🎊┆eventos",
                "📩┆feedback-staff",
                "📩┆feedback-carros",
                "❌┆bugs",
                "⌛┆cooldown",
                "📢┆anúncios-orgs",
                "📊┆votações-orgs",
            ],
            "SUPORTE": [
                "🎟️┆ticket",
                "⏳┆sala de espera",
                "🌐┆suporte-comunidade",
                "📞┆Suporte 1",
                "📞┆Supprte 2",
                "📞┆Suporte 3",
                "📞┆Suporte 4",
                "📞┆Suporte 5",
                "🔊┆Reuniões",
                "🔊┆Reuniões staff lider",
                "🔊┆Reuniões discord developer",
                "🔊┆Reuniões dev",
                "🔊┆Reuniões designer",
                "🔊┆Reuniões dev car",
                "🔊┆Convívio 1",
                "🔊┆Convívio 2",
                "🔊┆Convívio 3",
            ],
            "VIP": [
                "💬┆chat-vip-geral",
                "💬┆chat-vip-1",
                "💬┆chat-vip-2",
                "💬┆chat-vip-3",
                "💬┆chat-vip-4",
                "💬┆chat-vip-5",
                "📢┆anúncios-loja",
                "🛒┆loja",
            ],
            "STREAMERS": [
                "💬┆chat-streamers-geral",
                "💬┆chat-streamer-oficial",
                "💬┆chat-streamer-vip",
                "💬┆chat-streamer",
                "📜┆requesitos-streamer",
                "🎥┆streamer-oficial",
                "🎥┆streamer-vip",
                "🎥┆streamer",
            ],
            "FAQ'S": [
                "💼┆trabalho-legal-1",
                "💼┆trabalho-legal-2",
                "💼┆trabalho-legal-3",
                "💼┆trabalho-legal-4",
                "💼┆trabalho-legal-5",
            ],
            "FAQ'S": [
                "💀┆trabalho-ilegal-1",
                "💀┆trabalho-ilegal-2",
                "💀┆trabalho-ilegal-3",
                "💀┆trabalho-ilegal-4",
                "💀┆trabalho-ilegal-5",
            ],
            "FAQ'S": [
                "💲┆preçario",
                "🚗┆bagageiras",
                "⌨️┆comandos",
                "🗑️┆limpar-cache",
                "👁️┆lag-visual",
                "🎮┆lategame",
            ],
            "MÍDIA": [
                "📸┆imagens",
                "🎞️┆highlights",
                "🎬┆clips",
                "📱┆redes-sociais",
                "📣┆Divulgação",
            ],
            "CANDIDATURAS": [
                "📜┆requesitos-staff",
                "📝┆candidatura-staff",
                "📜┆requesitos-dev",
                "📝┆candidatura-dev",
                "📜┆requesitos-designer",
                "📝┆candidatura-designer",
                "📜┆requesitos-screen-share",
                "📝┆candidatura-screen-share",
                "📜┆requesitos-dev-car",
                "📝┆candidatura-dev-car",
                "📜┆requesitos-discord-developer",
                "📝┆candidatura-discord-developer",
            ],
            "PARCERIAS": [
                "🤝🏻┆parceria-1",
                "🤝🏻┆parceria-2",
                "🤝🏻┆parceria-3",
                "🤝🏻┆parceria-4",
                "🤝🏻┆parceria-5",
            ],
            "GESTOR ORGANIZAÇÕES LEGAIS": [
                "💬┆chat",
                "📢┆comunicados",
                "📢┆anúncios",
                "🔖┆pedir-tag",
                "📻┆rádios",
                "💼┆organização-legal-1",
                "💼┆organização-legal-2",
                "💼┆organização-legal-3",
                "💼┆organização-legal-4",
                "💼┆organização-legal-5",
            ],
            "GESTOR ORGANIZAÇÕES ILEGAIS": [
                "💬┆chat",
                "📢┆comunicados",
                "📢┆anúncios",
                "🔖┆pedir-tag",
                "📻┆rádios",
                "💀┆organização-ilegal-1",
                "💀┆organização-ilegal-2",
                "💀┆organização-ilegal-3",
                "💀┆oeganização-ilegal-4",
                "💀┆organização-ilegal-5",
                "💀┆organização-ilegal-6",
                "💀┆organização-ilegal-7",
                "💀┆oeganização-ilegal-8",
            ],
        },
    },
    "comunidade_divulgacao": {
        "cargos": [
            ("👑┆Fundador", 0xFFD700),
            ("🔰┆Staff líder", 0x3498DB),
            ("🔰┆Staff", 0x3498DB),
            ("🎥┆Streamer", 0x3498DB),
            ("🌐┆Comunidade discord", 0x3498DB),
            ("🎥┆Creador de conteúdo", 0x3498DB),
            ("📷┆Social poster", 0x3498DB),
            ("🎬┆Clip creator", 0x3498DB),
            ("┆Membro", 0x3498DB),
        ],
    },
        "categorias": {
            "RECEPÇÃO": [
                "🛬┆entrada", 
                "🛬┆saida", 
                "🚨┆regras", 
                "✅┆verificação"
            ],
            "COMUNIDADE": [
                "💬┆chat-geral",
                "📢┆comunicados",
                "📢┆anúncios",
                "ℹ️┆infomação",
            ],
            "SUPORTE": [
                "🎟️┆ticket",
                "⏳┆salda de espera",
                "📞┆Suporte 1",
                "📞┆Suporte 2",
                "📞┆Suporte 3",
                "📞┆Suporte 4",
                "📞┆Suporte 5",
                "🔊┆Convívio 1",
                "🔊┆Convívio 2",
                "🔊┆Convívio 3",
                "❓┆dúvidas",
            ],
            "PATROCINIOS": [
                "📢┆comunidados", 
                "📢┆anúncios", 
                "🛒┆loja"
            ],
            "DISCORD PATROCIONADO": [
                "🤝🏻┆discord-patrocionado-1",
                "🤝🏻┆discord-patrocionado-2",
                "🤝🏻┆discord-patrocionado-3",
                "🤝🏻┆discord-patrocionado-4",
                "🤝🏻┆discord-patrocionado-5",
            ],
            "STREAMERS PATROCIONADOS": [
                "🤝🏻┆streamers-patrocionado-1",
                "🤝🏻┆streamers-patrocionado-2",
                "🤝🏻┆streamers-patrocionado-3",
                "🤝🏻┆streamers-patrocionado-4",
                "🤝🏻┆streamers-patrocionado-5",
            ],
            "CREADOR DE CONTEÚDO PATROCIONADO": [
                "🤝🏻┆creador-de-conteúdo-patrocionado-1",
                "🤝🏻┆creador-de-conteúdo-patrocionado-2",
                "🤝🏻┆creador-de-conteúdo-patrocionado-3",
                "🤝🏻┆creador-de-conteúdo-patrocionado-4",
                "🤝🏻┆creador-de-conteúdo-patrocionado-5",
            ],
            "SOCIAL POSTER PATROCIONADO": [
                "🤝🏻┆social-poster-patrocionado-1",
                "🤝🏻┆social-poster-patrocionado-2",
                "🤝🏻┆social-poster-patrocionado-3",
                "🤝🏻┆social-poster-patrocionado-4",
                "🤝🏻┆social-poster-patrocionado-5",
            ],
            "CLIP CREATOR PATROCIONADO": [
                "🤝🏻┆clip-creator-patrocionado-1",
                "🤝🏻┆clip-creator-patrocionado-2",
                "🤝🏻┆clip-creator-patrocionado-3",
                "🤝🏻┆clip-creator-patrocionado-4",
                "🤝🏻┆clip-creator-patrocionado-5",
            ],
            "DIVULGAÇÃO": [
                "🌐┆discord",
                "🎥┆streamers",
                "📺┆creadores-de-conteúdo",
                "📰┆ocial-poster",
                "🎬┆clip-creators",
            ],
        },
        "grupo_de_amigos": {
            "cargos": [
                ("Fundador", 0xFFD700), 
                ("Amigo", 0x3498DB),
                ("Membro",0x3498DB)
            ],
            "categorias": {
                "GERAL": [
                    "💬┆geral", 
                    "📸┆imagens", 
                    "🎬┆clips", 
                    "🔗┆links", 
                    "🎮┆jogos"
                ],
                "CALL": [
                    "🔊┆Convívio 1",
                    "🔊┆Convívio 2",
                    "🔊┆Convívio 3",
                    "🔊┆Convívio 4",
                    "🔊┆Convívio 5",
                ],
                "AFK": [
                    "💤┆AFK", 
                    "🎶┆A ouvir música"
                ],
            },
        },
        "Comunidade": {
            "cargos": [
                ("Fundador", 0xFFD700), 
                ("Staff", 0x3498DB),
                ("Membro", 0x000000)
            ],
            "categorias": {
                "RECEPÇÃO": [
                    "entrada", 
                    "saida", 
                    "regras", 
                    "verificação"
                ],
                "COMUNIDADE": [
                    "chat", 
                    "clips", 
                    "imagens"
                ],
                "SUPORTE": [
                    "ticket", 
                    "sala de espera", 
                    "Suporte 1", 
                    "Suporte 2", 
                    "Suporte 3", 
                    "Suporte 4", 
                    "Suporte 5"
                ],
                "CALL": [
                    "Call 1", 
                    "Call 2", 
                    "Call 3", 
                    "Call 4", 
                    "Call 5"
                ]
            },
        },
        "agencia": {
            "cargos": [
                ("Dono", 0xFFD700), 
                ("Staff", 0x000000), 
                ("Parceria", 0x3498DB),  
                ("Cliente", 0x000000), 
                (Membro", 0x000000)
            ],
            "categorias": {
                "RECEPÇÃO": [
                    "entrada", 
                    "saida", 
                    "regras", 
                    "vetificação"
                ],
                "AGENCIA": [
                    "comunicados", 
                    "anúncios"
                ],
                "PORTOFÓLIO": [
                    "logos", 
                    "gifs", 
                    "banners", 
                    "thumbs", 
                    "loadingscreens", 
                    "artes", 
                    "flyers", 
                    "outros"
                ],
                "LOJA": [
                    "comunicados",
                    "anúncios", 
                    "loja"
                ],
                "COMUNIDADE": [
                    "chat", 
                    "feedback"
                ],
                "SUPORTE": [
                    "ticket", 
                    "dúvidas", 
                    "Sala de espera", 
                    "Suporte 1", 
                    "Suporte 2", 
                    "Suporte 3"
                ],
                "PARCERIAS": [
                    "parceria-1", 
                    "parceria-2", 
                    "parceria-3", 
                    "parceria-4", 
                    "parceria-5"
                ]
            },
        },
        "Servidor_vendas": {
            "cargos": [("Dono", 0xFFD700), ("Staff", 0x3498DB), ("Parceria", 0x000000), ("Cliente", 0x000000), ("Membro", 0x000000)],
            "categorias": {
                "RECEPÇÃO": ["entrada", "saida", "regras", "verificação"],
                "INFORMAÇÕES": ["comunicados", "anúncios", "produtos-venda", "preçário", "informações"],
                "LOJA": ["comunicados", "anúncios", "loja"],
                "COMUNIDADE": ["chat", "dúvidas"],
                "SUPORTE": ["ticket", "Sala de espera", "Suporte 1", "Suporte 2", "Suporte 3"],
                "PARCERIA": ["parceria-1", "parceria-2", "parceria-3"]
            },
        },
        "Suporte": {
            "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
            "categorias": {
                "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
                "🎮 JOGOS": ["🕹️-procurar-grupo"],
            },
        },
        "ver": {
            "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
            "categorias": {
                "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
                "🎮 JOGOS": ["🕹️-procurar-grupo"],
            },
        },
        "veremos": {
            "cargos": [("👑 Dono", 0xFFD700), ("🎮 Player", 0x3498DB)],
            "categorias": {
                "🏠 PRINCIPAL": ["💬-geral", "📢-anuncios"],
                "🎮 JOGOS": ["🕹️-procurar-grupo"],
            },
        },
    },


# --- CLASSE PARA O BOTÃO DE CONFIRMAÇÃO ---
class ConfirmacaoLimpeza(discord.ui.View):
    def __init__(self, fundador_id: int):
        super().__init__(timeout=30)
        self.fundador_id = fundador_id

    @discord.ui.button(
        label="CONFIRMAR E APAGAR TUDO", style=discord.ButtonStyle.danger, emoji="⚠️"
    )
    async def confirmar(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        if interaction.user.id != self.fundador_id:
            await interaction.response.send_message(
                "❌ Só o Fundador pode confirmar!", ephemeral=True
            )
            return

        button.disabled = True
        await interaction.response.edit_message(
            content="💣 **Limpeza total iniciada...**", view=self
        )

        guild = interaction.guild
        for canal in list(guild.channels):
            try:
                await canal.delete()
            except:
                pass

        for cargo in sorted(guild.roles, reverse=True):
            if (
                not cargo.is_default()
                and not cargo.managed
                and cargo < guild.me.top_role
            ):
                try:
                    await cargo.delete()
                except:
                    pass

        novo_canal = await guild.create_text_channel("✅-servidor-resetado")
        await novo_canal.send(
            f"🧹 **O servidor foi totalmente limpo por {interaction.user.mention}!**"
        )

    @discord.ui.button(label="CANCELAR", style=discord.ButtonStyle.secondary)
    async def cancelar(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.edit_message(
            content="❌ **Operação cancelada.**", view=None
        )
        self.stop()


# --- CLASSE PRINCIPAL DA COG ---
class gerardiscord(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="gerar", description="Cria a estrutura do servidor")
    @app_commands.describe(tema="Escolhe o tema do servidor")
    async def gerar(self, interaction: discord.Interaction, tema: str):
        tema_busca = tema.lower()
        guild = interaction.guild

        if interaction.user.id != guild.owner_id:
            await interaction.response.send_message(
                "❌ Apenas o **Fundador** pode usar este comando!", ephemeral=True
            )
            return

        if tema_busca not in TEMAS:
            await interaction.response.send_message(
                f"❌ Tema inválido!", ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"🏗️ A construir tema **{tema.upper()}**...", ephemeral=True
        )
        config = TEMAS[tema_busca]

        for item in config["cargos"]:
            nome, cor = item if isinstance(item, tuple) else (item, 0x99AAB5)
            if not discord.utils.get(guild.roles, name=nome):
                await guild.create_role(name=nome, color=discord.Color(cor), hoist=True)

        for cat_nome, canais in config["categorias"].items():
            categoria = await guild.create_category(cat_nome)
            for canal_nome in canais:
                if (
                    any(x in canal_nome for x in ["🔊", "🔈", "📞", "💤", "🎶"])
                    or "Call" in canal_nome
                ):
                    await guild.create_voice_channel(canal_nome, category=categoria)
                else:
                    await guild.create_text_channel(canal_nome, category=categoria)

        await interaction.followup.send(f"✅ Estrutura concluída!")

    @app_commands.command(name="limpar_servidor", description="⚠️ RESET TOTAL")
    async def limpar(self, interaction: discord.Interaction):
        if interaction.user.id != interaction.guild.owner_id:
            await interaction.response.send_message(
                "❌ Apenas o Fundador!", ephemeral=True
            )
            return

        view = ConfirmacaoLimpeza(fundador_id=interaction.user.id)
        msg = "⚠️ **AVISO CRÍTICO**: Queres mesmo apagar **TUDO**? Esta ação é irreversível!"
        await interaction.response.send_message(content=msg, view=view, ephemeral=True)


# --- FUNÇÃO SETUP (SEMPRE NO FIM) ---
async def setup(bot: commands.Bot):
    await bot.add_cog(gerardiscord(bot))


# --- CLASSE PARA COMANDOS DE INFORMAÇÃO ---
class Temas(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="temas", description="Lista de temas para o /gerar")
    async def listar_temas(self, interaction: discord.Interaction):
        if interaction.user.id != interaction.guild.owner_id:
            return await interaction.response.send_message("❌ Apenas o Fundador!", ephemeral=True)

        lista_nomes = list(TEMAS.keys())
        embed = discord.Embed(title="📂 Temas Disponíveis", color=0x00FF7F)
        
        texto_temas = ""
        for nome in lista_nomes:
            texto_temas += f"• `{nome}`\n"

        embed.add_field(name="Escolhe um nome para usar no /gerar:", value=texto_temas, inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

# --- SETUP ÚNICO NO FINAL DO ARQUIVO ---
async def setup(bot: commands.Bot):
    await bot.add_cog(gerardiscord(bot))
    await bot.add_cog(Temas(bot))
