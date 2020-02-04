#/////////////////////COMP : Manipulation de fichiers ////////////////////////////////////////////////
#
# import os
#
# nom = input("Saisir le nom du nouveau repertoire à créer : ")
# nvx_rep = '/home/ludivineo/pycharmproject/module_python_db/' + nom
# if os.path.isdir(nvx_rep):
#     print("Ce nom existe deja ! dommage")
#
# else:
#     os.mkdir(nvx_rep)
#     os.rename('/home/ludivineo/Desktop/mon_fichier', nvx_rep + '/mon_fichier')
#     print("le nouveaux repertoire " + nom + " a été crée, et le fichier 'mon_fichier' y a été déplacé !")


#/////////////////////COMP : Try Except ////////////////////////////////////////////////
# Ecrire une application de calcul d'amortissement d'un emprunt. L'application demandera la saisie :
#     du montant total de l'emprunt
#     de la durée en année
# L'application affichera le montant amorti chaque année (montant total / durée)
# Vous devrez capturer 2 erreurs :
#     Si l'utilisteur saisit des lettres pour une des données demandées, l'application devra afficher "Merci de saisir un chiffre"
#     Si la durée totale est égale à 0, la division par zéro devra être capturée et le message suivant sera affiché : "La durée ne doit pas être égale à 0".
#

while True:
    try:
        raise TypeError()
        montant = int(input("veuillez saisir le montant total de l'emprunt : "))
        duree = int(input("veuillez saisir la durée en année de l'emprunt : "))
        result = montant / duree
        print("amortissement annuel : " + str(result))
        print()
    except ValueError:
        print("merci de saisir des chiffres")
    except ZeroDivisionError:
        print("la durée ne doit pas etre égale à zero")
    except TypeError:
        print("erreur de type")





