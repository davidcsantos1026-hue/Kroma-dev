import discord
from discord.ext import commands

class PermissoesOrganizacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def configurar_permissoes_detalhadas(self, guild):
        # 1. Obter Cargos
        role_everyone = guild.default_role
        role_chefe = discord.utils.get(guild.roles, name="💀┆Chefe")
        role_admin = discord.utils.get(guild.roles, name="🔰┆Admin")
        role_org = discord.utils.get(guild.roles, name="😈┆Organização")
        role_amigo = discord.utils.get(guild.roles, name="🤝🏻Amigo")
        role_civil = discord.utils.get(guild.roles, name="👤Civil")

        # 2. Percorrer todas as categorias do servidor
        for categoria in guild.categories:
            nome_cat = categoria.name.upper()

            # --- PERMISSÕES DE CATEGORIA (BASE) ---
            if "CHEFES" in nome_cat:
                await categoria.set_permissions(role_everyone, view_channel=False)
                await categoria.set_permissions(role_chefe, view_channel=True)
            
            elif "COMUNIDADE" in nome_cat or "ECONOMIA" in nome_cat or "CALL" in nome_cat:
                await categoria.set_permissions(role_everyone, view_channel=False)
                await categoria.set_permissions(role_org, view_channel=True)

            # --- PERMISSÕES INDIVIDUAIS POR CANAL ---
            for canal in categoria.channels:
                
                # Canais de LEITURA APENAS (Regras, Anúncios, Informações)
                if any(x in canal.name for x in ["regras", "anuncios", "comunicados", "informações", "preçário"]):
                    await canal.set_permissions(role_everyone, send_messages=False)
                    await canal.set_permissions(role_org, send_messages=False)
                    await canal.set_permissions(role_admin, send_messages=True)

                # Canais de ENTRADAS/SAÍDAS (Ninguém escreve, só vê)
                elif "entradas" in canal.name or "saidas" in canal.name:
                    await canal.set_permissions(role_everyone, view_channel=True, send_messages=False)

                # Canais de BAÚ / STASH (Privados para cargos superiores)
                elif "bau-chefes" in canal.name:
                    await canal.set_permissions(role_org, view_channel=False)
                    await canal.set_permissions(role_chefe, view_channel=True)

                # Canais de LOGS / ENCOMENDAS (Apenas Org escreve)
                elif "encomendas" in canal.name or "vendas" in canal.name:
                    await canal.set_permissions(role_org, view_channel=True, send_messages=True)
                    await canal.set_permissions(role_everyone, view_channel=False)

                # Canais de VOZ (Call)
                if isinstance(canal, discord.VoiceChannel):
                    if "AFK" in canal.name:
                        await canal.set_permissions(role_everyone, speak=False)
                    elif "Convício" in canal.name:
                        await canal.set_permissions(role_org, connect=True, speak=True)

    @commands.command(name="aplicar_permissoes_org")
    @commands.has_permissions(administrator=True)
    async def aplicar_comando(self, ctx):
        await ctx.send("⏳ A configurar permissões de canais e categorias (Tema Organização)...")
        await self.configurar_permissoes_detalhadas(ctx.guild)
        await ctx.send("✅ **Concluído!** Canais trancados e configurados individualmente.")

async def setup(bot):
    await bot.add_cog(PermissoesOrganizacao(bot))
