import os

nom = input("Saisir le nom du nouveau repertoire à créer : ")
nvx_rep = '/home/ludivineo/pycharmproject/module_python_db/' + nom
if os.path.isdir(nvx_rep):
    print("Ce nom existe deja ! dommage")

else:
    os.mkdir(nvx_rep)
    os.rename('/home/ludivineo/Desktop/mon_fichier', nvx_rep + '/mon_fichier')
    print("le nouveaux repertoire " + nom + " a été crée, et le fichier 'mon_fichier' y a été déplacé !")



























