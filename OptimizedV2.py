#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Algorithme permettant de maximiser le profit des clients après 2 ans
- Chaque action ne peut être achetée qu'une fois
- On ne peut pas acheter une fraction d'action
- On ne peut dépenser au maximum que 500 euros par client

On veut ici trouver une version plus rapide que bruteforce.py pour le même problème,
on a pour l'instant choisi d'implémenter un algorithme glouton pour se faire.

"""

# Import des librairies
import csv
import time


# Lecture des informations du fichier csv
cost_list = []
benefit_list = []
action_names = []

profit_format = ''

# On indique ici le fichier dataset à ouvrir
# file_to_open = './dataset2_Python+P7.csv'
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
    """Fonction permettant de vérifier qu'un index existe bien"""
    if index < len(list):
        return True
    else:
        return False

def calculate_investment_return(combination, format):
    total = 0
    if format == 'percentage':
        for index in combination:
            total += (cost_list[index]*benefit_list[index])
    else:
        for index in combination:
            total += (benefit_list[index]/cost_list[index])
    return total

def Gloutonic(list1, list2, format, max_capacity):
    """Fonction principale utilisant un algorithme glouton afin de trier les actions suivant
    un rapport coût/bénéfice pour ensuite remplir un portefeuille d'action avec les actions
    présentant les meilleurs rapports sans dépasser un coût d'achat maximal.
    list1 correspond aux coûts, list2 correspond aux bénéfices, format est le format des bénéfices
    (pourcentage ou autre), max_capacity est le coût maximal à ne pas dépasser pour remplir le
    portefeuille d'actions.
    """
    new_list = []
    # 1ere phase de gloutonic ou on sort les actions par leur rapport cout*intéret
    for index in range(len(list1)):
        if list1[index] == 0:
            continue

        if format == 'percentage':
            rapport = [list1[index]*list2[index], index, list1[index]]

        else:
            rapport = [list2[index]/list1[index], index, list1[index]]

        if len(new_list) == 0:
            new_list.append(rapport)

        else:
            if new_list[-1][0] <= rapport[0]:
                new_list.append(rapport)

            elif new_list[0][0] >= rapport[0]:
                new_list = [rapport] + new_list

            else:
                for element_index in range(len(new_list)):
                    if index_exists(new_list, element_index+1):
                        if new_list[element_index][0] <= rapport[0] <= new_list[element_index+1][0]:
                            new_list.insert(element_index+1, rapport)
                            break

    # 2e phase, on va maintenant remplir notre portefeuille d'actions en commençant par les actions
    # ayant le meilleur indice (pour se faire on va retourner la liste précédente) et en voyant 
    # ensuite si on peut remplir notre portefeuille jusqu'à la capacité maximale
    action_list = new_list[::-1]
    current_capacity = 0
    actions_bought = []
    for action in action_list:
        if current_capacity + action[2] <= max_capacity:
            current_capacity += action[2]
            actions_bought.append(action[1])

    total_profit = calculate_investment_return(actions_bought, format)

    if format == 'percentage':
        return current_capacity, actions_bought, total_profit
    
    else:
        names_list = []
        for action in actions_bought:
            names_list.append(action_names[action])
        
        return current_capacity, names_list, total_profit



def main():
    current_cap, names, profit = Gloutonic(cost_list, benefit_list, profit_format, 500)
    print(f'''The current_capacity is {current_cap} for the combination of actions {names}
    with a return of {profit}''')

start = time.perf_counter()
main()
end = time.perf_counter()

print(f"Le temps d'exécution de la fonction OptimizedV2.py est de {end - start}s")
