import discord
from discord.ext import commands
import json
import os

class personalizacaoperfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_path = 'config_servidores.json'
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def salvar_dados(self):
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=4, ensure_ascii=False)

    @commands.command(name="configbot")
    @commands.has_permissions(administrator=True)
    async def config_bot(self, ctx, nome: str, avatar_url: str):
        """
        Define o perfil personalizado para este servidor.
        Uso: !configbot "Nome do Bot" "https://link-da-imagem.png"
        """
        guild_id = str(ctx.guild.id)
        self.dados[guild_id] = {
            "nome": nome,
            "avatar": avatar_url
        }
        self.salvar_dados()
        await ctx.send(f"✅ **Perfil Local Atualizado!**\nNeste servidor eu agora sou o **{nome}**.")

    @commands.command(name="falar")
    async def falar(self, ctx, *, mensagem: str):
        """Envia uma mensagem usando o perfil definido para o servidor."""
        guild_id = str(ctx.guild.id)
        
        # Verifica se o servidor tem perfil customizado
        if guild_id in self.dados:
            config = self.dados[guild_id]
            
            # Procura ou cria um Webhook para simular o bot
            webhooks = await ctx.channel.webhooks()
            webhook = discord.utils.get(webhooks, name="BotPersonalizado")
            
            if not webhook:
                webhook = await ctx.channel.create_webhook(name="BotPersonalizado")

            await ctx.message.delete() # Apaga o comando do utilizador
            await webhook.send(
                content=mensagem,
                username=config["nome"],
                avatar_url=config["avatar"]
            )
        else:
            await ctx.send(f"O perfil personalizado não está configurado. Use `!configbot` primeiro.")

    @config_bot.error
    async def config_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Apenas administradores ou o fundador podem alterar o meu perfil!")

async def setup(bot):
    await bot.add_cog(personalizacaoperfil(bot))
