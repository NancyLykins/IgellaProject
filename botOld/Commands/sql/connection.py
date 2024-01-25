import sqlite3

path = "Commands/sql/character.db"
connection = sqlite3.connect(path)
cursor = connection.cursor()