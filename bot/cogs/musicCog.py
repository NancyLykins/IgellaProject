import discord, youtube_dl, asyncio
from discord.ext import commands
from discord import app_commands

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}
YDL_OPTIONS = {"format": "bestaudio", "nonplaylist": "True"}


class musicCog(commands.Cog):
    def __init__(self, client: discord.client):
        self.client = client
        self.queue = {}
        
    @app_commands.command(name="play")
    @app_commands.describe(url="Qual a url da música")
    async def play(self, interaction: discord.Interaction, url: str):   
        await self.enterInChannel(interaction)
        source = await self.downloadUrl(interaction, URL=url)
        guildId = interaction.guild.id
        if guildId in self.queue.keys():            
            self.queue[guildId].append(source)
        else:
            self.queue[guildId] = [source]
            
        if not interaction.guild.voice_client.is_playing():
            await asyncio.sleep(5)
            source = self.queue[guildId].pop(0)
            interaction.guild.voice_client.play(source, after=lambda x=None: self.checkQueue(interaction, guildId, source))

    @app_commands.command(name="next")
    async def next(self, interaction: discord.Interaction):
        interaction.guild.voice_client.stop()
        if self.queue[interaction.guild.id] != []:
            await interaction.response.send_message("Pulou")
            await asyncio.sleep(10)
            interaction.guild.voice_client.play(self.queue[interaction.guild.id][0])
            self.queue[interaction.guild.id].pop(0)
        else:
            await interaction.response.send_message("Nenhum música na fila")
        
    @app_commands.command(name="pause", description="Pausa a música atual")
    async def pause(self, interaction: discord.Interaction):
        await interaction.guild.voice_client.pause()
        await interaction.response.send_message("Audio pausado!")
    
    @app_commands.command(name="resume", description="Despausa a música atual")
    async def resume(self, interaction: discord.Interaction):
        await interaction.guild.voice_client.resume()
        await interaction.response.send_message("Audio despausado!")

    @app_commands.command(name="stop", description="Para de tocar")
    async def stop(self, interaction: discord.Interaction):
        interaction.guild.voice_client.stop()
        await interaction.response.send_message("Áudio parou de tocar")
    
    def checkQueue(self, interaction, guildId, source):
        if guildId in self.queue and self.queue[guildId]:
            next_source = self.queue[guildId][0]
            self.queue[guildId].pop(0)

            if interaction.guild.voice_client and interaction.guild.voice_client.is_connected():
                interaction.guild.voice_client.play(next_source, after=lambda x=None: self.checkQueue(interaction, guildId, next_source))

    async def downloadUrl(self, interaction: discord.Interaction, URL=None):
        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                await interaction.response.send_message("Fazendo download do áudio", ephemeral=True)
                info = ydl.extract_info(URL, download=False)
                if not info:
                    await interaction.channel.send("Nenhum video encontrado nessa url",)
                await interaction.channel.send(content="Download feito com sucesso, adicionando música a fila",)
                source_url = info["formats"][0]["url"]
                source = await discord.FFmpegOpusAudio.from_probe(source_url, **FFMPEG_OPTIONS)
                return source
        except:
            await interaction.channel.send(content="Falha ao fazer o download do arquivo\nTente novamente mais tarde, se o problema persistir entre em contato com @u.hearv",)

    async def enterInChannel(self, interaction: discord.Interaction):
        if not interaction.user.voice:
            await interaction.response.send_message("Você não esta conectado a um canal de voz", ephemeral=True)
            return
        
        guildId = interaction.guild.id
        channel = interaction.user.voice.channel
        voiceChannel = discord.utils.get(interaction.guild.voice_channels, name=channel.name)
        if not interaction.guild.voice_client:
            await voiceChannel.connect()

async def setup(client: discord.Client) -> None:
    await client.add_cog(musicCog(client))
    