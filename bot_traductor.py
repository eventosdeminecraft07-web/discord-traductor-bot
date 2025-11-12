import discord
from discord.ext import commands
from googletrans import Translator
import os  

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def traduce(ctx, idioma_origen, idioma_destino, *, texto):
    """Ejemplo: !traduce en es Hello world"""
    try:
        result = translator.translate(texto, src=idioma_origen, dest=idioma_destino)
        await ctx.send(f"🌍 Traducción ({idioma_origen} → {idioma_destino}): {result.text}")
    except Exception as e:
        await ctx.send(f"❌ Error al traducir: {e}")

import os
bot.run(os.getenv("DISCORD_TOKEN"))
