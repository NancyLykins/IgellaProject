from Commands.sql.connection import *

def saveItem(item):
    name = item["name"]
    emoji = item["img"]
    desc = item["desc"]
    type = item["type"]
    action = item["action"]
    time = item["time"]
    slot = item["slot"]
    
    query = f"INSERT INTO itens (name, emoji, desc, type, action, time, slot) VALUES('{name}', '{emoji}', '{desc}', '{type}', '{action}', '{time}', '{slot}')"
    cursor.execute(query)
    connection.commit()