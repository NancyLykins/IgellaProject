from Commands.sql.connection import *

def saveMonster(monster):
    name = monster["name"]
    img = monster["img"]
    lvl = monster["lvl"]
    hp = monster["hp"]
    tempHp = monster["tempHp"]
    agi = monster["agi"]
    forca = monster["for"]
    int = monster["int"]
    pre = monster["pre"]
    vig = monster["vig"]
    
    query = f"INSERT INTO monster (name, img, lvl, hp, tempHp, agilidade, forca, inteligencia, presenca, vigor) VALUES('{name}', '{img}', '{lvl}', '{hp}', '{tempHp}', '{agi}', '{forca}', '{int}', '{pre}', '{vig}')"
    cursor.execute(query)
    connection.commit()
    