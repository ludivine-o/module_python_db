import requests
import mysql.connector

db = mysql.connector.connect(host="127.0.0.1", user="ludivineo", password="CN-9564", database="herboriste")
cursor = db.cursor()


def read():
    cursor.execute("SELECT * FROM plante")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2} -{3} - {4}'.format(row[0], row[1], row[2], row[3], row[4]))


def insert():
    id = input("saisir l'ID de la plante à ajouter")
    nom = input("saisir le nom de la plante à ajouter")
    indication = input("saisir l'indication de la plante à ajouter")
    partie_utilisee = input("saisir la partie utilisée de la plante à ajouter")
    prix = input("saisir le prix de la plante à ajouter")

    cursor.execute("INSERT INTO plante (id, nom, indication, partie_utilisee, prix) "
                   "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                        id,
                        nom,
                        indication,
                        partie_utilisee,
                        prix))


def delete():
    del_nom = input("saisir le nom de la plante à supprimer")
    cursor.execute("DELETE FROM plante WHERE nom = '" + del_nom + "'")


def modify():

    mod_nom = input("saisir le nom de la plante à modifier")
    cursor.execute("DELETE FROM plante WHERE nom = '" + del_nom + "'")


db.close()


























