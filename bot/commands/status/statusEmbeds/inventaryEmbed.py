import discord
from Commands.sql.itens.select.takeItensInInventary import takeItensInInventary

dinheiro = {
    "img": "",
    "quant": ""
}

has = {
    "equipable": False,
    "usable": False
}

async def inventaryEmbed(characterId):
    embed = discord.Embed(
        title= "Inventário",
        colour= 119911 
    )


    for item in takeItensInInventary(characterId):
        if(item[0] != "moeda"):
            match item[3]:
                case "equipable":
                    has["equipable"] = True
                case "usable":
                    has["usable"] = True
                             
            embed.add_field(name="", value=f"{item[1]} {item[0].title()}: {item[2]}", inline=False)
        else:
            dinheiro["img"] = item[1]
            dinheiro["quant"] = f"{item[2]}¤"
    
    embed.add_field(name="", value=f"{dinheiro['img']} Dinheiro: {dinheiro['quant']}")
    return embed, has
