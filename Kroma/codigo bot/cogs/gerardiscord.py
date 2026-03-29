import discord
from discord import app_commands
from discord.ext import commands

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
        "cargos": [("👑┆Fundador", 0xFFD700), ("🔰┆Staff líder", 0x3498DB), ("🔰┆Suporte", 0xFFD700), ("🔰┆Moderador", 0x3498DB), ("🔰┆Estagiário", 0xFFD700), ("🔰┆Staff", 0x3498DB), ("</>┆Developer", 0x3498DB), ("✏️┆Designer", 0x3498DB), ("💻┆Screen share", 0x3498DB), ("⚙️┆Dev car", 0x3498DB), ("📋┆Gestor de organizações legais", 0x3498DB), ("📋┆Gestor de organizações ilegais", 0x3498DB), ("📋┆Gestor de ticket", 0x3498DB), ("📋┆Gestor de creadores de conteúdo", 0x3498DB), ("📋┆Gestor de tags", 0x3498DB), ("📋┆Gestor de eventos", 0x3498DB), ("📋┆Gestor de VIP", 0x3498DB), ("💎┆vip 1", 0xFFD700), ("💎┆vip 2", 0x3498DB), ("💎┆vip 3", 0xFFD700), ("💎┆vip 4", 0x3498DB), ("💎┆vip 5", 0xFFD700), ("🎥┆Streamer Oficial", 0x3498DB), ("🎥┆Streamer Vip", 0xFFD700), ("🎥┆Streamer", 0x3498DB), ("💼┆Chefe de organização legal 1"), ("💼┆Organização legal 1"), ("💼┆Chefe de organização legal 2"), ("💼┆Organização legal 2"), ("💼┆Chefe de organização legal 3"), ("💼┆Organização legal 3"), ("💼┆Chefe de organização legal 4"), ("💼┆Organização legal 4"), ("💼┆Chefe de organização legal 5"), ("💼┆Organização legal 5"), ("💀┆Chefe de organização ilegal 1"), ("💀┆Organização ilegal 1"), ("💀┆Chefe de organização ilegal 2"), ("💀┆Organização ilegal 2"), ("💀┆Chefe de organização ilegal 3"), ("💀┆Organização ilegal 3"), ("💀┆Chefe de organização ilegal 4"), ("💀┆Organização ilegal 4"), ("💀┆Chefe de organização ilegal 5"), ("💀┆Organização ilegal 5"), ("💀┆Chefe de organização ilegal 6"), ("💀┆Organização ilegal 6"), ("💀┆Chefe de organização ilegal 7"), ("💀┆Organização ilegal 7"), ("💀┆Chefe de organização ilegal 8"), ("💀┆Organização ilegal 8"), ("🚫┆White list block", 0x3498DB), ("✅┆Verificado", 0xFFD700), ("👤┆Civil", 0x3498DB)],
        "categorias": {
            "STAFF": ["💬┆chat-staff-líder", "💬┆chat-staff", "💬┆chat-discord-developer", "💬┆chat-dev", "💬┆chat-dev-car", "💬┆chat-designer", "📢┆comunicados", "📢┆anúncios", "📌┆informações", "⌨️┆comandos", "❌┆bugs", "⌛┆ausências", "📫┆sugestões"],
            "RECEPÇÃO": ["🛬 ┆entradas", "🛫┆saidas", "✅┆verificação"],
            "INFORMAÇÕES": ["🚨┆regras", "📢┆comunicados", "📣┆atualizações", "📢┆regras-atualizações", "📊┆status", "📢┆comunicados-sorteios", "🎉┆sorteios", "🏆┆top-semanal", "🏆┆top-mensal", "⛔┆punições", "👀┆spoiler", "📊┆votações", "🚀┆boost-discord", "❓┆dúvidas"],
            "COMUNIDADE": ["💬┆chat-geral", "🔵┆pontos", "📫┆sugestões", "🗪┆debate-sugestões", "📢┆anúncios", "ℹ️┆info-self", "🎊┆eventos", "📩┆feedback-staff", "📩┆feedback-carros", "❌┆bugs", "⌛┆cooldown", "📢┆anúncios-orgs", "📊┆votações-orgs"],
            "SUPORTE": ["🎟️┆ticket", "⏳┆sala de espera", "🌐┆suporte-comunidade", "📞┆Suporte 1", "📞┆Supprte 2", "📞┆Suporte 3", "📞┆Suporte 4", "📞┆Suporte 5", "🔊┆Reuniões", "🔊┆Reuniões staff lider", "🔊┆Reuniões discord developer", "🔊┆Reuniões dev", "🔊┆Reuniões designer", "🔊┆Reuniões dev car", "🔊┆Convívio 1", "🔊┆Convívio 2", "🔊┆Convívio 3"],
            "VIP": ["💬┆chat-vip-geral", "💬┆chat-vip-1", "💬┆chat-vip-2", "💬┆chat-vip-3", "💬┆chat-vip-4", "💬┆chat-vip-5", "📢┆anúncios-loja", "🛒┆loja"],
            "STREAMERS": ["💬┆chat-streamers-geral", "💬┆chat-streamer-oficial", "💬┆chat-streamer-vip", "💬┆chat-streamer", "📜┆requesitos-streamer", "🎥┆streamer-oficial", "🎥┆streamer-vip", "🎥┆streamer"],
            "FAQ'S": ["💼┆trabalho-legal-1", "💼┆trabalho-legal-2", "💼┆trabalho-legal-3", "💼┆trabalho-legal-4", "💼┆trabalho-legal-5"],
            "FAQ'S": ["💀┆trabalho-ilegal-1", "💀┆trabalho-ilegal-2", "💀┆trabalho-ilegal-3", "💀┆trabalho-ilegal-4", "💀┆trabalho-ilegal-5"],
            "FAQ'S": ["💲┆preçario", "🚗┆bagageiras", "⌨️┆comandos", "🗑️┆limpar-cache", "👁️┆lag-visual", "🎮┆lategame"],
            "MÍDIA": ["📸┆imagens", "🎞️┆highlights", "🎬┆clips", "📱┆redes-sociais"],
            "CANDIDATURAS": ["📜┆requesitos-staff", "📝┆candidatura-staff", "📜┆requesitos-dev", "📝┆candidatura-dev", "📜┆requesitos-designer", "📝┆candidatura-designer", "📜┆requesitos-screen-share", "📝┆candidatura-screen-share", "📜┆requesitos-dev-car", "📝┆candidatura-dev-car", "📜┆requesitos-discord-developer", "📝┆candidatura-discord-developer"],
            "PARCERIAS": ["🤝┆parceria-1", "🤝┆parceria-2", "🤝┆parceria-3", "🤝┆parceria-4", "🤝┆parceria-5"],
            "GESTOR ORGANIZAÇÕES LEGAIS": ["💬┆chat", "📢┆comunicados", "📢┆anúncios", "🔖┆pedir-tag", "📻┆rádios", "💼┆organização-legal-1", "💼┆organização-legal-2", "💼┆organização-legal-3", "💼┆organização-legal-4", "💼┆organização-legal-5"],
            "GESTOR ORGANIZAÇÕES ILEGAIS": ["💬┆chat", "📢┆comunicados", "📢┆anúncios", "🔖┆pedir-tag", "📻┆rádios", "💀┆organização-ilegal-1", "💀┆organização-ilegal-2", "💀┆organização-ilegal-3", "💀┆oeganização-ilegal-4", "💀┆organização-ilegal-5", "💀┆organização-ilegal-6", "💀┆organização-ilegal-7", "💀┆oeganização-ilegal-8"]       
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

class gerardiscord(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # COMANDO SLASH: /gerar
    @app_commands.command(name="gerar", description="Cria a estrutura do servidor (Apenas para o Dono)")
    @app_commands.describe(tema="Escolhe o tema do servidor")
    async def gerar(self, interaction: discord.Interaction, tema: str):
        tema_busca = tema.lower()
        guild = interaction.guild

        # VERIFICAÇÃO: Apenas o Fundador (Owner) do servidor pode usar
        if interaction.user.id != guild.owner_id:
            await interaction.response.send_message("❌ Erro: Apenas o **Fundador** do servidor pode usar este comando!", ephemeral=True)
            return

        if tema_busca not in TEMAS:
            temas_disponiveis = ", ".join(TEMAS.keys())
            await interaction.response.send_message(f"❌ Tema inválido! Escolhe: `{temas_disponiveis}`", ephemeral=True)
            return

        # Responder imediatamente para evitar erro de timeout (3 segundos)
        await interaction.response.send_message(f"🏗️ A iniciar construção do tema **{tema.upper()}**...", ephemeral=True)

        config = TEMAS[tema_busca]

        # 1. CRIAR CARGOS
        for item in config["cargos"]:
            # Se o item for uma tuple (nome, cor), usa ambos. Se for só string, usa cor padrão.
            if isinstance(item, tuple):
                nome_cargo, cor = item
            else:
                nome_cargo, cor = item, 0x99AAB5

            if not discord.utils.get(guild.roles, name=nome_cargo):
                await guild.create_role(name=nome_cargo, color=discord.Color(cor), hoist=True)

        # 2. CRIAR CATEGORIAS E CANAIS
        for cat_nome, canais in config["categorias"].items():
            categoria = await guild.create_category(cat_nome)
            for canal_nome in canais:
                # Se tiver emoji de voz ou palavras chave de call, cria canal de voz
                if any(emoji in canal_nome for emoji in ["🔊", "🔈", "📞", "💤"]) or "Call" in canal_nome or "sala" in canal_nome.lower():
                    await guild.create_voice_channel(canal_nome, category=categoria)
                else:
                    await guild.create_text_channel(canal_nome, category=categoria)

        await interaction.followup.send(f"✅ Estrutura **{tema.upper()}** concluída com sucesso!")

    # COMANDO SLASH: /limpar_servidor
    @app_commands.command(name="limpar_servidor", description="⚠️ APAGA TUDO: Canais, Categorias e Cargos (Apenas Dono)")
    async def limpar(self, interaction: discord.Interaction):
        guild = interaction.guild

        # SEGURANÇA: Apenas o Fundador pode destruir o servidor
        if interaction.user.id != guild.owner_id:
            await interaction.response.send_message("❌ Erro: Comando restrito ao **Fundador**!", ephemeral=True)
            return

        await interaction.response.send_message("💣 A iniciar limpeza total... Isto pode demorar alguns segundos.", ephemeral=True)

        # 1. APAGAR TODOS OS CANAIS E CATEGORIAS
        for canal in guild.channels:
            try:
                await canal.delete()
            except Exception as e:
                print(f"Não consegui apagar o canal {canal.name}: {e}")

        # 2. APAGAR TODOS OS CARGOS (Exceto o @everyone e o cargo do Bot)
        for cargo in guild.roles:
            # Não apaga o @everyone nem cargos de integração (do próprio bot)
            if not cargo.is_default() and not cargo.managed:
                try:
                    await cargo.delete()
                except Exception as e:
                    print(f"Não consegui apagar o cargo {cargo.name}: {e}")

        # Criar um canal de texto temporário para avisar que acabou
        # (Já que apagámos todos, o bot precisa de um para falar)
        novo_canal = await guild.create_text_channel("✅-limpeza-concluída")
        await novo_canal.send(f"🧹 **O servidor foi resetado por {interaction.user.mention}!**\nTodos os canais, categorias e cargos foram removidos.")

# FUNÇÃO ESSENCIAL PARA CARREGAR A COG NO MAIN.PY
async def setup(bot: commands.Bot):
    await bot.add_cog(gerardiscord(bot))