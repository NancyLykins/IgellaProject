from Commands.sql.connection import *


def takeSkills(id):
    try:
        query = f"SELECT * FROM characterSkills WHERE user={id}"
        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()

    except Exception as e:
        print(e)