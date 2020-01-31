import module
import mysql.connector

if __name__ == "__main__":
    db = mysql.connector.connect(host="127.0.0.1", user="ludivineo", password="CN-9564", database="herboriste")
    cursor = db.cursor()
    module.read(cursor)

