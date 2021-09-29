"""
Algorithme permettant de maximiser le profit des clients après 2 ans
- Chaque action ne peut être achetée qu'une fois
- On ne peut pas acheter une fraction d'action
- On ne peut dépenser au maximum que 500 euros par client

Le programme doit essayer toutes les combinaisons possibles et choisir le meilleur résultat.
Il doit donc lire un fichier contenant des informations sur les actions, explorer toutes les combinaisons possibles
et afficher un meilleur investissement.

"""

# Import des librairies
import csv


# Lire les informations du fichier csv
cost_list = []
benefit_list = []

with open('./InvestInformation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} euros of cost for {row[1]} of benefit')
            cost_list.append(int(row[0]))
            benefit_list.append(float(row[1].replace(",", ".")))
            line_count += 1
    # print(f'Processed {line_count} lines.')



#   Explorer les combinaisons possibles

#   On prend les résultats obtenus en lisant le fichier csv
#   On obtient et on déclare des listes correspondant à la colonne Coût et à la colonne Bénéfice

# max_amount = 500
# total_combinations = []
# #1ere boucle récursive
# current_amount = 0
# def take_index(index, current_amount, max_amount):  
#     current_cost = cost_list[index]
#     index_combinations = []
#     # on vérifie si il y a un un index suivant, si oui on rajoute cette action à la combinaison d'action (et dans la 
#     # la fonction au-dessus, on augmentera le current_amount du prix de cette action)
#     # c'est à ce stade là qu'on doit implanter une fonction récursive je pense
#     if cost_list[index+1]:
#         # POSSIBILITé DE RECURSIVITé 1 ?
#         for next_index in cost_list[index+1:-1]:
#             current_combination = []
#             next_cost = cost_list[next_index]
#             if (current_cost + next_cost) <= max_amount:
#                 current_amount += current_cost
#             # POSSIBILITé de RECURSIVITé 2 ?
#     else:
#         index_combinations.append(index)
#     return index_combinations
# working_combination = take_index(0, current_amount, max_amount)
#     # on enregistre toutes les combinaisons possibles avec cet index et ceux qui suivent
#     # on passe ensuite à l'index d'après et on recommence jusqu'à ce qu'on arrive à la fin ou il n'y a qu'une
#     # seule combinaison rétournée 
def index_exists(list, index):
    if index < len(list):
        return True
    else:
        return False


def take_index(index, list_of_costs, current_amount, max_amount, original_combination = [], total_combinations = []):  
    
    # le problème actuel est qu'il faudrait qu'au début de chaque original_combination, il y ait notre index de base, peu faire ça avant
    if index_exists(list_of_costs, index+1) and (current_amount + list_of_costs[index+1] <= 500):
        current_amount += list_of_costs[index+1]
        original_combination.append(index+1)
        
        return take_index(index+1, list_of_costs, current_amount, max_amount, original_combination, total_combinations)
        
    elif index_exists(list_of_costs, index+2):
        
        return take_index(index+1, list_of_costs, current_amount, max_amount, original_combination, total_combinations)
        
    return original_combination, current_amount

def calculate_investment_return(combination):
    total = 0
    for index in combination:
        total += (cost_list[index]*benefit_list[index])
    return total

# class CombinationHolder:

#     def __init__(self, combination):
#         self.combination = combination

#     # ne marche pas !
# outside_variable = []
        
def add_combinations(index, used_list, current_amount, max_amount, combination_start, total_combinations):
    print("add_combinations est appelé")
    if current_amount == 0:
        current_amount = current_amount + used_list[index]
    original_combination, current_amount = take_index(index, used_list, current_amount, max_amount, combination_start)
    if total_combinations != []:
        # Càd si il y a déjà eu une boucle globale de faite et qu'on a déjà un portefeuille d'
        best_investment_found = calculate_investment_return(total_combinations[0])
        current_investment = calculate_investment_return(original_combination)
        # print(f"pour l'instant le meilleur return est de {best_investment_found}")
        # print(f"le current_investment serait de est de {current_investment}")
        # print(f'sachant que le current_amount est de {current_amount}')
        if best_investment_found < current_investment:
            print("ON CHANGE LE MEILLEUR RETURN EN DÉBUT DE BOUCLE!")
            new_combination = original_combination[:]
            total_combinations.pop()
            total_combinations.append(new_combination)
    else:
        total_combinations.append(original_combination)
    
    # print(f"au début total_combinations est égale à {total_combinations}")
    
    
    # print(total_combinations[0])
    # print(f"la 1ere combinaison est {original_combination}")
    # print(f"total_combinations est donc égale à {total_combinations}")
    index_combination = original_combination[:]
    # C'est la première combinaison qu'on obtient, à partir de laquelle on va chercher les autres
    BOUCLE = 0
    # while len(index_combination) >= 2:
    while len(index_combination) >= 2:
        if BOUCLE % 100000 == 0:
            print(f'Boucle Locale n°{BOUCLE}')
        BOUCLE += 1
        # print(index_combination)
        # print(total_combinations[0])
        # Tant qu'il existe des combinaisons possibles à partir de notre index, on continue d'en chercher
        index_to_switch = index_combination[-1]
        
        # essai pour calculer le retour sur investissement des actions choisies au moment où on trouve une nouvelle
        # combinaison, le but étant de remplacer la dernière combinaison par la nouvelle si celle-ci est plus
        # rentable
        # dans un premier temps, créer la fonction permettant de calculer la valeur de l'investissement après 2 ans
        best_investment_found = calculate_investment_return(total_combinations[0])
        current_investment = calculate_investment_return(index_combination)
        # print(f"pour l'instant le meilleur return est de {best_investment_found}")
        # print(f"le current_investment serait de est de {current_investment}")
        # print(f'sachant que le current_amount est de {current_amount}')
        if best_investment_found < current_investment:
            print("ON CHANGE LE MEILLEUR RETURN !")
            new_combination = index_combination[:]
            total_combinations.pop()
            total_combinations.append(new_combination)

        # total_combinations.append(index_combination)
        index_combination.pop()
        current_amount -= used_list[index_to_switch]
        if index_exists(used_list, index_to_switch + 1):
            # index_combination, current_amount = take_index(index_to_switch + 1, used_list, current_amount, max_amount, index_combination)
            index_combination, current_amount = take_index(index_to_switch, used_list, current_amount, max_amount, index_combination)
            # print(f'Est-ce que total_combinations[0] a changé ? : {total_combinations[0]}')
            # print(f'Est-ce que outside_variable a changé ? : {outside_variable[0]}')
            # total_combinations.append(index_combination)
            pass
            
        else:
            # cad si on est arrivé en fin de liste et qu'il n'existe plus d'autres index/actions à acheter pour faire
            # une combinaison, alors on passe juste
            # total_combinations = total_combinations + index_combination
            pass
    
    best_investment_found = calculate_investment_return(total_combinations[0])
    current_investment = calculate_investment_return(index_combination)
    if best_investment_found < current_investment:
        total_combinations.pop()
        total_combinations.append(index_combination)
    print("une fonction  add_combination s'est terminée")
    print("le current_amount de notre action seule est" + str(current_amount))
    print(f"son numéro d'index (donc le index_combination final) est de {index_combination}")
    
    return total_combinations


max_amount = 500
total_combinations = []
#1ere boucle récursive
current_amount = 0

for index in range(len(cost_list)):
    combination_start = [index]
    # le problème actuel est que take_index ne fonctionne qu'une fois, càd qu'elle ne va return qu'une seule combinaison
    # et pas toutes les combinaisons possibles avec un seul index
    total_combinations = add_combinations(index, cost_list, current_amount, max_amount, combination_start, total_combinations)
    # all_index_combinations = add_combinations(index, cost_list, current_amount, max_amount, combination_start, total_combinations)
    
    # print("la liste comprenant toutes les combinaisons d'un seul index est: \n")
    # print(index_combinations)
    # total_combinations = total_combinations + all_index_combinations
    
    print("ON A ATTEINT LA FIN DE LA BOUCLE GLOBALE n°" + str(index+1))
    print(f"Pour l'instant le meilleur portefeuille d'actions est {total_combinations}")
    print(f"Son return est de {calculate_investment_return(total_combinations[0])}\n")

# print("total_combinations est égal à :")
# print(total_combinations)
print(f"Le meilleur portefeuille d'actions est {total_combinations}")
print(f"Son return est de {calculate_investment_return(total_combinations[0])}")







        

#   On déclare une fonction qui prend un index, puis append dans une liste [le coût de l'action correspondant à cet 
#   index ainsi que son pourcentage de bénéfice]
#   On ajoute le coût à une variable coût total qui ne doit pas dépasser 500
#   On itère la boucle et on continue à append des listes [coût, bénéfice] jusqu'à ce qu'on arrive à 500
    
    

#   Il faut trouver un moyen pour pour qu'on passe à chaque fois qu'on a déjà effectué une combinaison



#   (l'index correspondrait au numéro de l'action - 1)



# Afficher le résultat
# main()



