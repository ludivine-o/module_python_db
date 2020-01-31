import mysql.connector
import requests


def read(cursor):
    cursor.execute("SELECT * FROM plante")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2} -{3} - {4}'.format(row[0], row[1], row[2], row[3], row[4]))


def search(cursor):
    search_choice = input("souhaitez-vous faire une recherche stricte dans n'importe quel champs (S) "
                          "ou multiple (qui affiche plusieurs resultats) par nom (M) ? : ").upper()
    if search_choice == "S":
        search_field = input("par quel champs souhaitez-vous faire votre recherche ? ").upper()
        search = input("quel est l'élément recherché dans ce champs : ")

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

    elif search_choice == "M":
        search = input("quel est le nom de l'élément recherché : ").upper()
        cursor.execute(("SELECT * FROM plante WHERE nom LIKE '%{}%' ORDER BY nom ASC, prix ASC LIMIT 3").format(search))
        rows = cursor.fetchall()
        for row in rows:
            print('{0} - {1} : {2} ({3}) - {4} €'.format(row[0], row[1], row[2], row[3], row[4]))



def insert(db, cursor):
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
    db.commit()



def delete(db, cursor):
    del_nom = input("saisir le nom de la plante à supprimer")
    cursor.execute("DELETE FROM plante WHERE nom = '" + del_nom + "'")
    db.commit()


def modify(db, cursor):
    mod_nom = input("saisir le nom de la plante à modifier : ")
    field = input("quel champs souhaitez-vous modifier ? "
                  "\n (ID)d, (N)om, (I)ndication, (PU)partie_utilisee, (P)rix : ").upper()
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


def modify_all(db, cursor):
    field = input \
        ("quel champs souhaitez-vous modifier ? "
         "\n (ID)d, (N)om, (I)ndication, (PU)partie_utilisee, (P)rix : ").upper()
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






























