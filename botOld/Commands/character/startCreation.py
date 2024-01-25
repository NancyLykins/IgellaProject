import discord, random, math, time
from Commands.status.statusEmbeds.infosEmbed import infosEmbed
from Commands.sql.character.saveCharacter import saveCharacter
from Commands.sql.classes.select.takeClasses import takeClasses
from Commands.sql.classes.select.takeClassesName import takeClassesName
from Commands.sql.classes.select.takeClassesNameAndDesc import takeClassesNameAndDesc
from Commands.sql.classes.select.takeClassBuff import takeClassBuff
from Commands.sql.races.select.takeRaces import takeRaces
from Commands.sql.races.select.takeRacesNameEmojiAndDesc import takeRacesNameEmojiAndDesc
from Commands.sql.skills.select.takeSkillNameAndDesc import takeSkillNameAndDesc
from Commands.newObject.createObjects.waitForInt import waitForInt

character = []

class Character():
    def __init__(self, ctx, client, id):
        seed = int(time.time())
        random.seed(seed)
        self.client = client
        self.ctx = ctx
        self.rerollRest = 2
        self.trigget = 0
        self.attribute = ["Agilidade", "Força", "Inteligencia", "Presença", "Vigor"]
        self.attributeCounter = 0
        self.points = ["8", "10", "12", "13", "14"]
        self.skillsDafault = 3
        self.skillsTaken = 0

        
        self.id = id
        self.name = ""
        self.gender = ""
        self.age = ""
        self.magic = ""
        self.race = ""
        self.classe = ""
        self.attributes = {
            "Agilidade": 0,
            "Força": 0,
            "Inteligencia": 0,
            "Presença": 0,
            "Vigor": 0
        }
        self.buffs = {
            "agilidadeBuff": 0,
            "forcaBuff": 0,
            "inteligenciaBuff": 0,
            "presencaBuff": 0,
            "vigorBuff": 0,
            "periciaBuff": 0,
        }
        self.skills = []
        
        self.hp = 0
        self.mana = 0
        
    def set_name(self, name):
        self.name = name
        
    def set_gender(self, gender):
        self.gender = gender
        
    def set_age(self, age):
        self.age = age
    
    def set_magic(self, magic):
        self.magic = magic
        
    def set_race(self, race):
        self.race = race
        
    def set_class(self, classe):
        self.classe = classe
        
    def set_attributes(self, attributes):
        self.attibutes = attributes
        
    def set_skills(self, skills):
        self.skills = skills
    
    async def ask_name(self):
        msg = await self.ctx.send(">>> Qual o nome do personagem?")
        
        def check(message):
            return message.author == self.ctx.author and message.channel == self.ctx.channel
    
        charName = await self.client.wait_for("message", check=check, timeout=120)
        await charName.delete()
        await msg.delete()
        self.set_name(charName.content)

    async def ask_gender(self):
        view = discord.ui.View()
        async def on_click(interaction: discord.Interaction):
            self.set_gender(interaction.data["custom_id"])
            await interaction.message.delete()
        genders = ["Homem", "Mulher", "Outro"]
        for gender in genders:
            button = discord.ui.Button(label=gender, style=discord.ButtonStyle.blurple)
            button.callback = on_click
            button.custom_id = gender
            view.add_item(button)
        await self.ctx.send(content=">>> Qual o gênero do personagem?", view=view)   
        def check(interaction):
            return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel
        await self.client.wait_for("interaction", check=check)
    
    async def ask_age(self):
        msg = await self.ctx.send(">>> Quantos anos seu personagem tem?")
        def check(message):
            messageContent = message.content
            try:
                messageContent = int(messageContent)
                return message.author == self.ctx.author and message.channel == self.ctx.channel and isinstance(messageContent, int)
            except:
                return False
        age = await self.client.wait_for("message", check=check, timeout=180)
        self.set_age(int(age.content))
        await msg.delete()
        await age.delete()
        
    async def ask_race(self):
        i = 0
        raceBuffs = []
        embed = createRaceEmbed()
        msg = await self.ctx.send(embed=embed)
        races = takeRaces()
        
        for race in races:
            await msg.add_reaction(race[1])

        reaction, user = await self.client.wait_for("reaction_add", timeout=10800)
        emoji = reaction.emoji

        for race in races:
            if(race[1] == emoji):
                selectedRace = race
        
        race = selectedRace[0].title()
        self.set_race(race)
        

        for value in selectedRace:
            if(isinstance(value, int)):
                raceBuffs.append(value)
        
        for attr in raceBuffs:
            match i:
                case 0:
                    self.buffs["agilidadeBuff"] += attr
                case 1:
                    self.buffs["forcaBuff"] += attr
                case 2:
                    self.buffs["inteligenciaBuff"] += attr
                case 3:
                    self.buffs["presencaBuff"] += attr
                case 4:
                    self.buffs["vigorBuff"] += attr
                case 5:
                    self.buffs["periciaBuff"] += attr
            i +=1

        await msg.delete()
 
    async def ask_class(self):
        classes = takeClassesName()
        embed = createClassEmbed()
        view = discord.ui.View(timeout=10800)
        
        async def on_click(interaction: discord.Interaction):
            classe = interaction.data["custom_id"].title()
            self.set_class(classe)
            agility, strength, inteligence, presence, vigour, pericias = takeClassBuff(classe.lower())
            self.buffs["agilidadeBuff"] += agility
            self.buffs["forcaBuff"] += strength
            self.buffs["inteligenciaBuff"] += inteligence
            self.buffs["presencaBuff"] += presence
            self.buffs["vigorBuff"] += vigour
            self.buffs["periciaBuff"] += pericias
            await msg.delete()
        
        for classe in classes:
            classe = classe[0]
            button = discord.ui.Button(label=classe.title(), style=discord.ButtonStyle.primary)
            button.callback = on_click
            button.custom_id = classe
            view.add_item(button)
        msg = await self.ctx.send(embed=embed, view=view)
        def check(interaction):
            return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel
        await self.client.wait_for("interaction", check=check)

    async def set_power(self):
        magics = [
            ("Água", 5),
            ("Alma", 1),
            ("Ar", 5),
            ("Caos", 1),
            ("Corporal", 10),
            ("Eletricidade", 4),
            ("Escuridão", 1),
            ("Espaço", 1),
            ("Fogo", 5),
            ("Gelo", 2),
            ("Gravidade", 1),
            ("Luz", 2),
            ("Madeira", 1),
            ("Metal", 3),
            ("Planta", 4),
            ("Sagrada", 2),
            ("Sem Magia", 15),
            ("Sombra", 3),
            ("Sonora", 2),
            ("Tempo", 1),
            ("Terra", 5),
            ("Vazio", 1),
            ("Veneno", 2),
        ]
        magic_list = [magic[0] for magic in magics for _ in range(magic[1])]

        embed = discord.Embed(title="Sua magia é de:", colour=991111)
        view = discord.ui.View(timeout=120)
                   
        async def randomPower(interaction: discord.Interaction):
            magic = random.choice(magic_list)
            self.set_magic(magic)

            embed = discord.Embed(
                title ="Sua magia é de:",
                colour= 991111,
            )
            embed.add_field(name=magic, value="", inline=False)
            embed.set_footer(text=f"Tentativas restantes: {self.rerollRest}")
            view = discord.ui.View(timeout=120)
            
            async def continuar(interaction):
                await interaction.message.delete()

            async def rollagaing(interaction):
                self.rerollRest -=1
                await randomPower(interaction)
            
            continueButton = discord.ui.Button(label="Continuar", style=discord.ButtonStyle.green) 
            continueButton.callback = continuar
            continueButton.custom_id = "continue"
            view.add_item(continueButton)
            if(self.rerollRest >= 1):
                reRollButton = discord.ui.Button(label="RE-ROLL", style=discord.ButtonStyle.red)
                reRollButton.callback = rollagaing
                reRollButton.custom_id = "reroll"
                view.add_item(reRollButton)
            
            await interaction.response.edit_message(embed=embed, view=view)
            def check(interaction):
                return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel
            await self.client.wait_for("interaction", check=check)
                
        button = discord.ui.Button(label="SPIN", style=discord.ButtonStyle.red)
        button.callback = randomPower
        view.add_item(button)
        await self.ctx.send(embed=embed, view=view)
        
        def check(interaction):
            return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel and interaction.data["custom_id"] == "continue"

        await self.client.wait_for("interaction", check=check, timeout=None)

    async def ask_attributes(self):
        if self.trigget == 0:
            embed = explainAttributes()
            msg = await self.ctx.send(embed=embed)
        
        if(self.attributeCounter < len(self.attribute)):
            self.trigget = 1
            embed = discord.Embed(
                title=f"Agora, quantos pontos vai adicionar em {self.attribute[self.attributeCounter]}",
                colour=428754
            )
            self.attributeCounter += 1

            view = discord.ui.View(timeout=10800)        
                
            async def attributeButtonClick(interaction: discord.Interaction):
                point = interaction.data["custom_id"]
                atributo = self.attribute[self.attributeCounter - 1]
                self.attributes[atributo] = point

                self.points.remove(interaction.data["custom_id"])

                await interaction.message.delete()
                await self.ask_attributes()

            for point in self.points:
                button = discord.ui.Button(label=point, style=discord.ButtonStyle.primary)
                button.callback = attributeButtonClick
                button.custom_id = point

                view.add_item(button)

            await self.ctx.send(embed=embed, view=view)

                
        def check(interaction):
            return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel and self.attributeCounter == len(self.attributes)

        await self.client.wait_for("interaction", check=check, timeout=10800)
        await msg.delete()

    async def ask_skills(self):
        periciasTotal = self.skillsDafault + self.buffs["periciaBuff"]
        skills = takeSkillNameAndDesc()

        embed = discord.Embed(
            title="Hora de escolher algumas pericias",
            description=f"Você podera escolher {periciasTotal} pericias das seguintes, pressione o botão correspondente com cada uma desejada.",
            colour=439823
        )
        embed.add_field(name="Lista de pericias:", value="", inline=False)
        view = discord.ui.View()

        async def escolherPericia(interaction: discord.Interaction):
            buttonId = interaction.data["custom_id"]
            self.skills.append(buttonId)
            self.skillsTaken += 1

            if(self.skillsTaken < periciasTotal):
                embed = discord.Embed(
                title="Hora de escolher algumas pericias",
                description=f"Você podera escolher {periciasTotal} pericias das seguintes, pressione o botão correspondente com cada uma desejada.",
                colour=439823
                )

                for skill in skills:
                    skillName = skill[0].title()
                    skillDesc = skill[1].capitalize()
                    embed.add_field(name=skillName, value=skillDesc, inline=False)
                
                embed.set_footer(text=f"Pericias restantes {periciasTotal - self.skillsTaken}")

                for button in view.children:
                    if button.label == buttonId.title():
                        button.disabled = True
                
                await interaction.response.edit_message(embed=embed, view=view)
            
            else:
                await interaction.message.delete()
                playerCategory = discord.utils.get(self.ctx.guild.categories, name="Players")
                channel = await  self.ctx.guild.create_text_channel(name=self.name, category=playerCategory)
                permissions = {
                    self.ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    interaction.user: discord.PermissionOverwrite(read_messages=True)
                }
                await channel.edit(overwrites=permissions)

        for skill in skills:
            skillName = skill[0].title()
            skillDesk = skill[1].capitalize()
            embed.add_field(name=skillName, value=skillDesk, inline=False)
            button = discord.ui.Button(label=skillName, style=discord.ButtonStyle.primary)
            button.callback = escolherPericia
            button.custom_id = skillName.lower()
            view.add_item(button)

        embed.set_footer(text=f"Pericias restantes {periciasTotal - self.skillsTaken}")
        await self.ctx.send(embed=embed, view=view)
        def check(interaction):
            return interaction.user == self.ctx.author and interaction.channel == self.ctx.channel and (self.skillsTaken + 1) == periciasTotal
        
        await self.client.wait_for("interaction", check=check)

    def save(self):
        vigor = int(self.attributes["Vigor"]) + int(self.buffs["vigorBuff"])
        forca = int(self.attributes["Força"]) + int(self.buffs["forcaBuff"])
        inteligencia = int(self.attributes["Inteligencia"]) + int(self.buffs["inteligenciaBuff"])
        self.hp = vigor*2 + math.floor(forca/2)
        self.mana = vigor + inteligencia*2

        saveCharacter(id=self.id, name=self.name, age=self.age, gender=self.gender, race=self.race, magic=self.magic, classe=self.classe, hp=self.hp, mana=self.mana, attributes=self.attributes, buffs=self.buffs, skills=self.skills)

def explainAttributes():
    embed = discord.Embed(
        title= "Hora de distribuir seus pontos",
        colour= 428754
    )
    embed.add_field(name="Você tem 5 atributos:", value="__Agilidade__, __Força__, __Inteligencia__, __Presença__ e __Vigor__", inline=False)
    embed.add_field(name="Além disso você pode adicionar os pontos em cada um deles", value="[8] [10] [12] [13] [14]", inline=False)
    embed.add_field(name="", value="10 sendo o padrão, 8 sendo abaixo da média e dando -1 para cada ação com essa habilidade, 12 e 13 sendo um pouco acima da média dando +1 para cada teste e 14 dando +2.", inline=False)   
    return embed
    
def createRaceEmbed():
    embed = discord.Embed(
        title="Raças",
        colour = 642463
    )
    races = takeRacesNameEmojiAndDesc()
    for race in races:
        raceName = race[0].title()
        raceEmoji = race[1]
        raceDesc = race[2].capitalize()
        embed.add_field(name=f"{raceEmoji} {raceName}:", value=raceDesc, inline=False)

    return embed

def createClassEmbed():
    embed = discord.Embed(
        title="Classes",
        colour= 184423
        )
    
    classes = takeClassesNameAndDesc()   
    for classe in classes:
        className = classe[0].title()
        classDesc = classe[1].capitalize()
        embed.add_field(name=className, value=classDesc, inline=False)
      
    return embed
