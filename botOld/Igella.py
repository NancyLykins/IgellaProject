###################################################################################################
#                                                                                                 #
#          #####   #     #    ###     ##    #       #       ##    #    #######   #     #          #
#          #    #   #   #     ###     # #   #      # #      # #   #    #          #   #           #
#          #####     # #              #  #  #     #   #     #  #  #    #           # #            #
#          #    #     #       ###     #   # #    #######    #   # #    #            #             #
#          #####      #       ###     #    ##   #       #   #    ##    #######      #             #
#                                                                                                 # 
###################################################################################################        


from Commands.character.startCreation import Character
from Commands.giveItem import giveItem
from Commands.monsters.createMonster import createMonster
from Commands.monsters.extingMonster import extingMonster
from Commands.monsters.summonMonster import summonMonster
from Commands.newObject.createNewObject import createNewObject
from Commands.rollSkill.rollSkill import rollSkill
from Commands.session.createTurnControl import turn
from Commands.session.startSession import startSession
from Commands.sql.character.deleteChar import deleteChar
from Commands.sql.character.remove.removeEffect import removeEffect
from Commands.sql.character.remove.resetBuffs import resetBuffs
from Commands.sql.character.update.updateBuffs import updateBuffs
from Commands.sql.classes.select.takeClasses import takeClasses
from Commands.sql.effects.select.takeEffectBuff import takeEffectBuff
from Commands.sql.effects.select.takeEffectsId import takeEffectsId
from Commands.sql.effects.select.takeEffectLife import takeEffectLife
from Commands.sql.effects.select.takeEffectTime import takeEffectTime
from Commands.status.showStatus import showStatus
from Commands.tests.rollDice import rollDice
from Commands.tests.testeAgilidade import testeAgilidade
from Commands.tests.testeForca import testeForca
from Commands.tests.testeInteligencia import testeInteligencia
from Commands.tests.testePresenca import testePresenca
from Commands.tests.testeVigor import testeVigor
from Commands.sql.character.update.updateLife import updateLife
from configSetup import configSetup
from Commands.character.life import dealDamage, healLife
from Commands.character.mana import spendMana, recoveryMana
from Commands.tests.dices import xdx

effectBuff = {
    "agilidadeBuff": 0,
    "forcaBuff": 0,
    "inteligenciaBuff": 0,
    "presencaBuff": 0,
    "vigorBuff": 0
}



@client.event
async def on_member_update(before, after):
    global turn
    beforeRoles = []
    playerId = after.id
    await asyncio.sleep(5)
    for roleName in before.roles: beforeRoles.append(roleName)
    for role in after.roles:
        if role not in beforeRoles:
            for roleId in takeEffectsId():
                if role.id == roleId[0] :
                    life = takeEffectLife(role.id)
                    if life is not None:
                        try: 
                            life = int(life)
                        except:
                            life = xdx(life)
                        updateLife(playerId, life)
                            
                    effectTime = int(takeEffectTime(playerId, role.id))
                    effect = takeEffectBuff(role.id)
                    effectBuff["agilidadeBuff"] = effect[0]
                    effectBuff["forcaBuff"] = effect[1]
                    effectBuff["inteligenciaBuff"] = effect[2]
                    effectBuff["presencaBuff"] = effect[3]
                    effectBuff["vigorBuff"] = effect[4]
                    effectKeys = list(effectBuff.keys())
                    for effect in effectKeys:
                        if effectBuff[effect] != 0:
                            updateBuffs(playerId, effect, effectBuff[effect])
                
                    effectTime = effectTime + int(turn.get())
                    while(turn.get() <= effectTime):
                        await asyncio.sleep(1)
                    
                    effectKeys = list(effectBuff.keys())
                    for effect in effectKeys:
                        if effectBuff[effect] != 0:
                            resetBuffs(playerId, effect, effectBuff[effect])
                    removeEffect(playerId, role.id)
                    await after.remove_roles(role)



#    ###################
#    #   GAME MASTER   #
#    ###################

async def isGM(ctx, i=False):
    if i is False:
        autorRole = discord.utils.get(ctx.author.roles, name="GM")
        if autorRole is None:
            await ctx.send("Você não tem permissão para usar esse comando")
        return False if (autorRole is None) else True
    else:
        autorRole = discord.utils.get(ctx.user.roles, name="GM")
        if autorRole is None:
            await ctx.response.send_message("Você não tem permissão para usar esse comando", ephemeral=True)
        return False if (autorRole is None) else True

@client.command()
async def new(ctx, obj=None):
    if await isGM(ctx):
        await createNewObject(ctx, client, obj)

@client.command()
async def session(ctx, function=None):
    if await isGM(ctx):
        await startSession(ctx, function)

@client.command()
async def give(ctx, player=None):
    if await isGM(ctx):
        await giveItem(ctx, player)


#   #################
#   #   MONSTERS    #
#   #################

@client.command()
#CREATE A MONSTER
async def evok(ctx):
    if await isGM(ctx):
        await createMonster(ctx, client)
    
@client.command()
#SUMMON A MONSTER
async def summon(ctx):
    if await isGM(ctx):
        monsterName = ctx.message.content.split(".summon ")[1]
        print(monsterName)
        if monsterName is not None:
            await summonMonster(ctx, client, monsterName)
        else:
            await ctx.send("Escolha o monstro e tente novamente")
    
@client.command()
#DELETE A MONSTER
async def exting(ctx, monsterName=None):
    if await isGM(ctx):
        if monsterName is not None:
            await extingMonster(ctx, client, monsterName)
        else:
            await ctx.send("Escolha o monstro e tente novamente")

#    ##################
#    #   CHARACTERS   #
#    ##################

characters = {}
@client.command()
#CREATE CHARACTER 
async def create(ctx):
    trigget = await checkCharacter.checkCharacterNExist(ctx)
    if trigget == 0:
        await ctx.message.delete()
        id = ctx.author.id
        characters[id] = Character(ctx, client, id)
        await characters[id].ask_name()
        await characters[id].ask_gender()
        await characters[id].ask_age()
        await characters[id].set_power()
        await characters[id].ask_race()
        await characters[id].ask_attributes()
        await characters[id].ask_class()
        await characters[id].ask_skills()
        characters[id].save()


@client.command()
#SHOW CHARACTER STATUS
async def status(ctx):
    try:
        await showStatus(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)

@client.command()
async def spell(ctx, amount):
    await spendMana(ctx, amount)
    
@client.command()
async def recovery(ctx, player: discord.Member, amount):
    await recoveryMana(ctx, player, amount)

#   #############
#   #   TESTS   #
#   #############

@client.command()
async def roll(ctx):
    await rollDice(ctx)

@client.command()
async def usar(ctx, skill=None):
    try:
        if skill is not None:
            await rollSkill(ctx, skill)
        else:
            await ctx.send("Escolha uma perícia e tente novamente")
    except:
        await checkCharacter.checkCharacterExist(ctx)
        
@client.command(name="agi")
async def AGI(ctx):
    try:
        await testeAgilidade(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)

@client.command(name="for")
async def FOR(ctx):
    try:
        await testeForca(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)

@client.command(name="int")
async def INT(ctx):
    try:
        await testeInteligencia(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)

@client.command(name="pre")
async def PRE(ctx):
    try:
        await testePresenca(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)

@client.command(name="vig")
async def VIG(ctx):
    try:
        await testeVigor(ctx)
    except:
        await checkCharacter.checkCharacterExist(ctx)


####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################

#   ###########
#   #   ADM   #
#   ###########

@client.tree.command(name="edit_channel_name")
@app_commands.describe(channel_to_edit="Marque o canal que deseja alterar o nome")
@app_commands.describe(new_name="Novo nome para o canal")
async def editChannelName(interaction: discord.Interaction, channel_to_edit: str, new_name: str):
    channel = discord.utils.get(interaction.guild.text_channels, id=int(channel_to_edit.split("<#")[1][:-1]))
    await channel.edit(name=new_name)
    await interaction.response.send_message(f"Nome do canal trocado com sucesso", ephemeral=True)

@client.tree.command(name="say")
@app_commands.describe(message="Escreva a mensagem que deve ser enviada")
async def say(interaction: discord.Interaction, message: str):
    if interaction.user.id == 663141450564894750:
        await interaction.channel.send(message)
        await interaction.response.send_message("Mensagem enviada com sucesso!", ephemeral=True)
    else:
        await interaction.response.send_message("Você não tem permissão de usar esse comando", ephemeral=True)

@client.tree.command(name="say_text")
@app_commands.describe(title="Titulo do texto")
@app_commands.describe(message="Mensagem do texto")
@app_commands.describe(footer="Rodapé do texto")
async def sayText(interaction: discord.Interaction, title: str, message: str, footer: str):
    if interaction.user.id == 663141450564894750:
        await interaction.channel.send(title)
        await interaction.channel.send(message)
        await interaction.channel.send(footer)
        await interaction.response.send_message("Mensagem enviada com sucesso!", ephemeral=True)
    else:
        await interaction.response.send_message("Você não tem permissão de usar esse comando", ephemeral=True)

@client.tree.command(name="setup")
async def setup(interaction: discord.Interaction):
    await configSetup(interaction)
    await interaction.response.send_message("Configurações feitas com sucesso", ephemeral=True)

@client.tree.command(name="clear")
@app_commands.describe(limit="Quantas mensagens deseja apagar?")
async def clear(interaction: discord.Interaction, limit: str):
    if interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("Comando executado com sucesso", ephemeral=True)
        if(isinstance(limit, str) and limit == "*"):
            messagesDelete = await interaction.channel.purge(limit=9999999999)
            deleteMessagesNumber = len(messagesDelete)
            await interaction.channel.send(f"` {deleteMessagesNumber} ` {'mensagem foi apagada' if deleteMessagesNumber == 1 else 'mensagens foram apagadas'}")
        else:
            try:
                limit = int(limit)
                messagesDelete = await interaction.channel.purge(limit=limit)
                deleteMessagesNumber = len(messagesDelete)
                await interaction.channel.send(f"` {deleteMessagesNumber} ` {'mensagem foi apagada' if deleteMessagesNumber == 1 else 'mensagens foram apagadas'}")
                
            except:
                await interaction.channel.send("Comando digitado incorretamente", ephemeral=True)
    else:
        await interaction.response.send_message("Você não tem permissão para usar esse comando", ephemeral=True)
###########################################################################################################################

#   #############
#   #   MUSIC   #
#   #############

@client.tree.command(name="join")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message(">>> Você precisa estar em um canal de voz primeiro", ephemeral=True)
    else:
        channel = interaction.user.voice.channel
        if interaction.guild.voice_client is None:
            await channel.connect()
        else:
            await interaction.guild.voice_client.move_to(channel)
        await interaction.response.send_message(f"{client.user.name.title()} entrou no canal {channel.name}", ephemeral=True)

@client.tree.command(name="disconnect")
async def disconnect(interaction: discord.Interaction):
    if interaction.guild.voice_client is not None:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Disconectado com sucesso", ephemeral=True)
    else:
        await interaction.response.send_message("Não foi possivel desconectar, não estou em nenhum canal de voz", ephemeral=True)


def checkQueue(interaction, guildId, source):
    if guildId in queue and queue[guildId]:
        next_source = queue[guildId][0]
        queue[guildId].pop(0)

        if interaction.guild.voice_client and interaction.guild.voice_client.is_connected():
            interaction.guild.voice_client.play(next_source, after=lambda x=None: checkQueue(interaction, guildId, next_source))

# @client.tree.command(name="play")
# @app_commands.describe(url="Qual a url da música")
# async def play(interaction: discord.Interaction, url: str):   
#     if not interaction.user.voice:
#         await interaction.response.send_message("Você não esta conectado a um canal de voz", ephemeral=True)
#         return
#     guildId = interaction.guild.id
#     channel = interaction.user.voice.channel
#     voiceChannel = discord.utils.get(interaction.guild.voice_channels, name=channel.name)
#     if not interaction.guild.voice_client:
#         await voiceChannel.connect()
        
#     try:
#         with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(url, download=False)
#             if not info:
#                 await interaction.response.send_message("Nenhum video encontrado nessa url", ephemeral=True)
#             source_url = info["formats"][0]["url"]
#             source = await discord.FFmpegOpusAudio.from_probe(source_url, **FFMPEG_OPTIONS)
#             if guildId in queue.keys():            
#                 queue[guildId].append(source)
#             else:
#                 queue[guildId] = [source]
#             await interaction.response.send_message(f"Now playing")
#     except:
#         await interaction.response.send_message("Não foi possivel carregar o video ou url invalida", ephemeral=True)

#     if not interaction.guild.voice_client.is_playing():
#         interaction.guild.voice_client.play(source, after=lambda x=None: checkQueue(interaction, guildId, source))



# @client.tree.command(name="next")
# async def next(interaction: discord.Interaction):
#     interaction.guild.voice_client.stop()
#     if queue[interaction.guild.id] != []:
#         await interaction.response.send_message("Pulou")
#         await asyncio.sleep(10)
#         interaction.guild.voice_client.play(queue[interaction.guild.id][0])
#         queue[interaction.guild.id].pop(0)
#     else:
#         await interaction.response.send_message("Nenhum música na fila")

#       ################################
#       #   ####    #####    ######    #
#       #   #   #   #    #  #          #
#       #   #   #   #    #  #          #
#       #   ####    #####   #    ###   #
#       #   #   #   #       #      #   #
#       #   #    #  #        #####     #
#       ################################

@client.tree.command(name="give")
@app_commands.describe(player="Quem vai receber o item?")
@app_commands.describe(item="O item que a pessoa deve receber")
@app_commands.describe(amount="Quantidade de itens que o jogador deve receber")
async def give(interaction: discord.Interaction, player: discord.Member, item: str, amount: int):
    if await isGM(interaction, i=True):
        await giveItem(interaction, player, item, amount)

@client.tree.command(name="damage")
@app_commands.describe(player="O personagem de quem recebera dano?")
@app_commands.describe(damage="Quanto de dano o personagem deve receber?")
async def damage(interaction: discord.Interaction, player: discord.Member, damage: int):
    await dealDamage(interaction, player, damage)


@client.tree.command(name="heal")
@app_commands.describe(player="O personagem de quem sera curado?")
@app_commands.describe(heal="Quanto de vida deve ser restaurado?")
async def damage(interaction: discord.Interaction, player: discord.Member, heal: int):
    await healLife(interaction, player, heal)


@client.tree.command(name="classes")
async def classes(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Classes"
    )
    for classe in takeClasses():
        embed.add_field(name=classe[0].title(), value=classe[1].capitalize(), inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)
