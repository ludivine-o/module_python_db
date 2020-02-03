import mysql.connector
import requests


def read(cursor):
    cursor.execute("SELECT * FROM plante")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2} -{3} - {4}'.format(row[0], row[1], row[2], row[3], row[4]))


def strict_search(cursor, search_field, search):
        if search_field == 'ID':
            search_field = 'id'
        elif search_field == 'N':
            search_field = 'nom'
        elif search_field == 'I':
            search_field = 'indication'
        elif search_field == 'PU':
            search_field = 'partie_utilisee'
        elif search_field == 'P':
            search_field = 'prix'
        else:
            print("ce n'est pas un champs valide")
        cursor.execute("SELECT * FROM plante WHERE " + search_field + " = '" + search + "'")
        var = cursor.fetchall()
        return var


def multiple_search(cursor, search):
        cursor.execute(("SELECT * FROM plante WHERE nom LIKE '%{}%' ORDER BY nom ASC, prix ASC LIMIT 3").format(search))
        rows = cursor.fetchall()
        for row in rows:
            print('{0} - {1} : {2} ({3}) - {4} €'.format(row[0], row[1], row[2], row[3], row[4]))


def insert(db, cursor, id, nom, indication, partie_utilisee, prix):
    cursor.execute("INSERT INTO plante (id, nom, indication, partie_utilisee, prix) "
                   "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                        id,
                        nom,
                        indication,
                        partie_utilisee,
                        prix))
    db.commit()


def delete(db, cursor, del_nom):
    cursor.execute("DELETE FROM plante WHERE nom = '" + del_nom + "'")
    db.commit()


def modify(db, cursor, mod_nom, field):
    if field == 'ID':
        field = 'id'
    elif field == 'N':
        field = 'nom'
    elif field == 'I':
        field = 'indication'
    elif field == 'PU':
        field = 'partie_utilisee'
    elif field == 'P':
        field = 'prix'
    else:
        print("ce n'est pas un champs valide")
    modif = input("saisir le nouvel élément :")
    cursor.execute("UPDATE plante SET " + field + " = '" + modif + "' where nom = '" + mod_nom + "'")
    db.commit()


def modify_all(db, cursor, field):
    if field == 'ID':
        field = 'id'
    elif field == 'N':
        field = 'nom'
    elif field == 'I':
        field = 'indication'
    elif field == 'PU':
        field = 'partie_utilisee'
    elif field == 'P':
        field = 'prix'
    else:
        print("ce n'est pas un champs valide")
    ex_donnee = input("saisir l'élément erroné :")
    modif = input("saisir le nouvel élément corrigé :")
    cursor.execute("UPDATE plante SET " + field + " = '" + modif + "' WHERE " + field + " = '" + ex_donnee + "'")
    db.commit()


if __name__ == "__main__":
    db = mysql.connector.connect(host="127.0.0.1", user="ludivineo", password="CN-9564", database="herboriste")
    cursor = db.cursor()






























