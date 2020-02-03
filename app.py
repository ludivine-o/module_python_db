import mysql.connector
import module as action

def main():
    db = mysql.connector.connect(host="127.0.0.1", user="ludivineo", password="CN-9564", database="herboriste")
    cursor = db.cursor()
    while True:
        choice = input("\n"
                       "(L)ister, (R)echercher, (A)jouter, (S)upprimer, (M)odifier, (MALL) Modifier tout un champ, (Q)uitter : ")

        if choice.upper() == 'L':
            action.read(cursor)

        elif choice.upper() == 'R':
            search_choice = input("souhaitez-vous faire une recherche stricte dans n'importe quel champs (S) "
                                  "ou multiple (qui affiche plusieurs resultats) par nom (M) ? : ").upper()
            if search_choice == "M":
                search = input("quel est le nom de l'élément recherché : ").upper()
                print(action.multiple_search(cursor, search))
            elif search_choice == "S":
                search_field = input("Dans quel champs souhaitez-vous faire votre recherche ? "
                                     "\n (ID)d, (N)om, (I)ndication, (PU)partie_utilisee, (P)rix : ").upper()
                search = input("quel est l'élément recherché dans ce champs : ")
                print(action.strict_search(cursor, search_field, search))
            else:
                print('veuillez entrer un choix valide.\n')

        elif choice.upper() == 'A':
            id = input("saisir l'ID de la plante à ajouter")
            nom = input("saisir le nom de la plante à ajouter")
            indication = input("saisir l'indication de la plante à ajouter")
            partie_utilisee = input("saisir la partie utilisée de la plante à ajouter")
            prix = input("saisir le prix de la plante à ajouter")
            action.insert(db, cursor, id, nom, indication, partie_utilisee, prix)

        elif choice.upper() == 'S':
            del_nom = input("saisir le nom de la plante à supprimer")
            action.delete(db, cursor, del_nom)

        elif choice.upper() == 'M':
            mod_nom = input("saisir le nom de la plante à modifier : ")
            field = input("quel champs souhaitez-vous modifier ? "
                          "\n (ID)d, (N)om, (I)ndication, (PU)partie_utilisee, (P)rix : ").upper()
            action.modify(db, cursor, mod_nom, field)

        elif choice.upper() == 'MALL':
            field = input("quel champs souhaitez-vous modifier ? "
                          "\n (ID)d, (N)om, (I)ndication, (PU)partie_utilisee, (P)rix : ").upper()
            action.modify_all(db, cursor, field)

        elif choice.upper() == 'Q':
            db.close()
            break

        else:
            print('veuillez entrer un choix valide.\n')


if __name__ == "__main__":
    main()

