import mysql.connector
import module as action

def main():
    db = mysql.connector.connect(host="127.0.0.1", user="ludivineo", password="CN-9564", database="herboriste")
    cursor = db.cursor()
    while True:
        choice = input("(L)ister, (R)echercher, (A)jouter, (S)upprimer, (M)odifier, (MALL) Modifier tout un champ, (Q)uitter : ")
        if choice.upper() == 'L':
            action.read(cursor)
        elif choice.upper() == 'R':
            print(action.search(cursor))
        elif choice.upper() == 'A':
            action.insert(db, cursor)
        elif choice.upper() == 'S':
            action.delete(db, cursor)
        elif choice.upper() == 'M':
            action.modify(db, cursor)
        elif choice.upper() == 'MALL':
            action.modify_all(db, cursor)
        elif choice.upper() == 'Q':
            db.close()
            break
        else:
            print('veuillez entrer un choix valide.\n')


if __name__ == "__main__":
    main()

