from Commands.sql.connection  import *

def takeCharacter(id):
    try:
        query = f"SELECT * FROM character WHERE id={id}"
        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()

    except Exception as e:
        print(e)
