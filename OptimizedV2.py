#!/usr/bin/python
# -*- coding: latin-1 -*-
"""
Algorithme permettant de maximiser le profit des clients après 2 ans
- Chaque action ne peut être achetée qu'une fois
- On ne peut pas acheter une fraction d'action
- On ne peut dépenser au maximum que 500 euros par client

On veut ici trouver une version plus rapide que bruteforce.py pour le même problème,
on a pour l'instant choisi d'implémenter un algorithme PSE branch and bound avec 
possiblement un algorithme glouton afin d'aider à calculer le "poids" des branches.

Voit pour l'instant le cours d'optimisation discrète de Melbourne disponible sur Coursera.
N'est peut-être pas le plus indiqué ici étant donné qu'on a pas vraiment deux séries de valeurs
différentes qui ne peuvent pas se mélanger, comme le poids et le prix d'un objet, ici avec les actions
et leur pourcentage ont a plutôt une seule valeur. Ou pas. On a d'un coté le prix qui correspond au
poids global et de l'autre coté le pourcentageXce prix qui donne la valeur future de cet achat. C'est
cette valeur là qu'on essaie de maximiser, en essayant de ne pas dépasser le poids, et donc le prix
limite.

"""

# Import des librairies
import csv
import time


# Lire les informations du fichier csv
cost_list = []
benefit_list = []
action_names = []

profit_format = ''

# file_to_open = './dataset1_Python+P7.csv'
file_to_open = './InvestInformation.csv'

if file_to_open == './InvestInformation.csv':
    print("The profit is written as percentage")
    profit_format = 'percentage'
    with open(file_to_open) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                cost_list.append(int(row[0]))
                benefit_list.append(float(row[1].replace(",", ".")))
                line_count += 1
else:
    print("The profit is written as is")
    profit_format = 'as_is'
    with open(file_to_open) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if float(row[1]) > 0:
                    action_names.append(row[0])
                    cost_list.append(float(row[1]))
                    benefit_list.append(float(row[2].replace(",", ".")))
                    line_count += 1
                else:
                    action_names.append(row[0])
                    cost_list.append(float(row[1]))
                    benefit_list.append(int(0))
                    line_count += 1


def index_exists(list, index):
    if index < len(list):
        return True
    else:
        return False


def Gloutonic(list1, list2, format, max_capacity):
    new_list = []
    # On veut remplir new_list avec la liste d'actions optimales
    # pour se faire on doit faire un rapport de cout/weight pour chaque action
    # trier ensuite tous ses rapports avec le plus fort en 1er

    # 1ere phase de gloutonic ou on sort les actions par leur rapport cout*intéret
    for index in range(len(list1)):
        # Pour chaque index du nombre d'éléments dans la list d'actions
        if list1[index] == 0:
            continue

        if format == 'percentage':
            rapport = [list1[index]*list2[index], index, list1[index]]

        else:
            rapport = [list2[index]/list1[index], index, list1[index]]

        if len(new_list) == 0:
            new_list.append(rapport)

        else:
            # cas 1 l'élément est plus grand ou égal que le dernier élément de la liste
            if new_list[-1][0] <= rapport[0]:
                new_list.append(rapport)
            # cas 2 l'element est plus petit ou egal que le 1er élément de la liste
            elif new_list[0][0] >= rapport[0]:
                new_list = [rapport] + new_list
            else:
                # cas 3 l'élément est entre les deux
                # dans ce cas, pour chaque élément de la liste on voit si il est sup ou inf à         # dans ce cas, pour chaque élément de la liste on voit si il est sup ou inf à celui d'après
                # ou d'avant celui d'après ou d'avant
                for element_index in range(len(new_list)):
                    if index_exists(new_list, element_index+1):
                        if new_list[element_index][0] <= rapport[0] <= new_list[element_index+1][0]:
                            new_list.insert(element_index+1, rapport)
                            break
                    # si notre rapport se situe entre un élément et l'élément d'après, alors
                    # si on est en fin de liste, pas besoin de continuer et faire index_exists
    # print(f'La new_list finale est égale à {new_list}')

    # 2e phase, on va maintenant remplir notre portefeuille d'actions en commençant par les actions
    # ayant le meilleur indice (pour se faire on va retourner la liste précédente) et en voyant 
    # ensuite si on peut remplir notre portefeuille jusqu'à la capacité maximale
    action_list = new_list[::-1]
    current_capacity = 0
    actions_bought = []
    for action in action_list:
        if current_capacity + action[2] <= max_capacity:
            # print(f'current_capacity={current_capacity}')
            # print(f'actions[1]={action[1]}')
            current_capacity += action[2]
            actions_bought.append(action[1])

    if format == 'percentage':
        return print(f'The current_capacity is {current_capacity} for the combination of actions {actions_bought}')
    
    else:
        names_list = []
        for action in actions_bought:
            names_list.append(action_names[action])
        
        return print(f'The current_capacity is {current_capacity} for the combination of actions {names_list}')

    # important, on doit ajouter +2 à chaque index pour pouvoir lire ceux-ci directement
    # comme on doit suppr les deux premières lignes du fichier csv
    # for index in range(len(actions_bought)):
    #     actions_bought[index] += 2

    # return print(f'The current_capacity is {current_capacity} for the actions_indexes {actions_bought} \
    #             and the names {names_list}')



        



def main():
    Gloutonic(cost_list, benefit_list, profit_format, 500)

start = time.perf_counter()
main()
end = time.perf_counter()

print(f"Le temps d'exécution de la fonction OptimizedV2.py est de {end - start}")

"""
téléch template google slide
mettre titres sur chaque slide
numéroter les pages et mettre sur combien de pages

la complexité est déjà un ordre de grandeur

complex temporelle temps d'éxecution

montrer les recherches déjà faites sur les algorithmes optimisés
pouvoir expliquer pourquoi avoir avoir choisi l'algo glouton en particulier

important mettre le comparatif a la fin

mettre juste quelques lignes de commentaires en-dessous de chaque fonction et supprimer
tous les autres commentaires"""