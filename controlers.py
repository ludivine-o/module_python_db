from models import *

def calc_average():
    # calcule la moyenne du prix de toutes les plantes selon une famille
    plantes = Plante.select(Family.name, fn.AVG(Plante.price).alias("moy"))\
        .join(Family)\
        .group_by(Plante.family)\
        .order_by(Plante.family)
    for plante in plantes:
        print(plante.family.name, plante.moy)

def calc_average_indication():
    # calcule la moyenne du prix de toutes les plantes selon une indication
    moy_indic = Plante.select(Indication.name, fn.AVG(Plante.price).alias("moy"))\
        .join(Indication)\
        .group_by(Indication.name)
    for plante in moy_indic:
        print(plante.indication.name, plante.moy)


def calc_plante_par_sous_classe():
    result = Plante.select(SubClass.name, fn.COUNT(Plante.name).alias("calc"))\
        .join(Family)\
        .join(SubClass)\
        .group_by(SubClass.name)
    for row in result:
        print(row.family.sub_class.name, row.calc)

def calc_plante_par_famille():
    result = \
        Family.select(Family.name, fn.COUNT(Plante.name).alias("somme"))\
        .join(Plante).\
        group_by(Family.name)
    for row in result:
        print(row.name, row.somme)

    # result = Family.select()
    # for row in result:
    #     print(row.name, row.plants.count())

def price_min_max_par_sub_class():
    result = \
        Plante.select(SubClass.name, fn.MAX(Plante.price).alias("max"), fn.MIN(Plante.price).alias("min"))\
        .join(Family)\
        .join(SubClass)\
        .group_by(SubClass.name)
    for row in result:
        print(row.family.sub_class.name, row.max, row.min)


price_min_max_par_sub_class()


