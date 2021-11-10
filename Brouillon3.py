#!/usr/bin/python
# -*- coding: latin-1 -*-

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
import time

# Lire les informations du fichier csv
cost_list = []
benefit_list = []
action_names = []

file_to_open = './dataset1_Python+P7.csv'

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
                print("found null!")
                action_names.append(row[0])
                cost_list.append(float(row[1]))
                benefit_list.append(int(0))
                line_count += 1


# def function_performance(function):
#     start = time.perf_counter()
#     function
#     end = time.perf_counter()
#     print(f"Le temps d'exécution de la fonction est de {end - start}")

def index_exists(list, index):
    if index < len(list):
        return True
    else:
        return False


def take_original_combination(index, list_of_costs, current_amount, max_amount, original_combination = [], total_combinations = []):  
    # le problème actuel est qu'il faudrait qu'au début de chaque original_combination, il y ait notre index de base, peu faire ça avant

    # Si il existe encore une action après celle actuelle, et que la rajouter à notre combinaison ne ferait pas dépasser
    # notre montant d'achat du montant maximum, alors on la rajoute à la combinaison ainsi que son coût au montant d'achat
    # actuel
    for action_number in range(len(list_of_costs[index:-1])):
        current_amount += list_of_costs[action_number]
        original_combination.append(action_number)
        total_combinations.append(original_combination)
        
    return original_combination, current_amount

def calculate_investment_return(combination):
    total = 0
    for index in combination:
        total += (cost_list[index]*benefit_list[index])
    return total

def is_best_combination(current_best, maybe_best, max_amount):
    if maybe_best

        
def add_combinations(index, used_list, current_amount, max_amount, combination_start, total_combinations):
    print("add_combinations est appelée")
    
    # On cherche ensuite la première combinaison possible avec take_index, à partir de laquelle on va chercher toutes
    # les autres combinaisons possibles à partir de l'action avec laquelle on débute add_combinations
    original_combination, current_amount = take_original_combination(index, used_list, current_amount, max_amount, combination_start)
    total_combinations.append(original_combination)
    # on fait d'abord une copie de notre original combination
    # on la met ensuite comme meilleure combinaison trouvée jusqu'à maintenant
    # à partir de la première combinaison trouvée on va ensuite pop l'avant-dernier numéro, puis l'avant-avant dernier etc
    # jusqu'à retomber sur le 1er index
    # si la solution trouvée est meilleure que notre meilleure solution trouvée jusqu'ici, on la remplace
    best_combination_found = original_combination[:]
    original_copy = original_combination[:]

    original_length = []
    original_length.append(len(original_copy))
    copy_length = original_length[:]
    original_amount = []
    original_amount.append(current_amount)
    copy_amount = original_amount[:]

    for i in range(copy_length):
        if i in [0,1]:
            pass
        else:
            while i != copy_length:
                index_to_pop = -i
                original_copy = original_copy[0:index_to_pop] + original_copy[-1]
                copy_amount -= used_list[index_to_pop]
                
                total_combinations.append(original_copy)
    

    # on va ensuite pop() le dernier index de notre combinaison originale puis recommencer la manip
    return total_combinations

    # if total_combinations != []:
    #     # Càd SI il y a déjà eu une boucle globale de faite et qu'on a déjà un portefeuille d'actions
    #     best_investment_found = calculate_investment_return(total_combinations[0])
    #     current_investment = calculate_investment_return(original_combination)
    #     # print(f"pour l'instant le meilleur return est de {best_investment_found}")
    #     # print(f"le current_investment serait de est de {current_investment}")
    #     # print(f'sachant que le current_amount est de {current_amount}')
    #     if best_investment_found < current_investment:
    #         print("ON CHANGE LE MEILLEUR RETURN EN DÉBUT DE BOUCLE!")
    #         new_combination = original_combination[:]
    #         total_combinations.pop()
    #         total_combinations.append(new_combination)
    # else:
    #     total_combinations.append(original_combination)
    
    # # print(f"au début total_combinations est égale à {total_combinations}")
    
    
    # # print(total_combinations[0])
    # # print(f"la 1ere combinaison est {original_combination}")
    # # print(f"total_combinations est donc égale à {total_combinations}")
    # index_combination = original_combination[:]
    # # C'est la première combinaison qu'on obtient, à partir de laquelle on va chercher les autres
    # BOUCLE = 0
    # while len(index_combination) >= 2:

    #     # La variable BOUCLE n'est utilisée que pour connaître le nombre d'itérations de while
    #     if BOUCLE % 100000 == 0:
    #         print(f'Boucle Locale n°{BOUCLE}')
    #     BOUCLE += 1

    #     # Tant qu'il existe des combinaisons possibles à partir de notre index, on continue d'en chercher
    #     index_to_switch = index_combination[-1]
        
    #     # essai pour calculer le retour sur investissement des actions choisies au moment où on trouve une nouvelle
    #     # combinaison, le but étant de remplacer la dernière combinaison par la nouvelle si celle-ci est plus
    #     # rentable
    #     # dans un premier temps, créer la fonction permettant de calculer la valeur de l'investissement après 2 ans
    #     best_investment_found = calculate_investment_return(total_combinations[0])
    #     current_investment = calculate_investment_return(index_combination)
        
    #     if best_investment_found < current_investment:
    #         print("ON CHANGE LE MEILLEUR RETURN !")
    #         new_combination = index_combination[:]
    #         total_combinations.pop()
    #         total_combinations.append(new_combination)

    #     index_combination.pop()
    #     current_amount -= used_list[index_to_switch]
    #     if index_exists(used_list, index_to_switch + 1):
            
    #         index_combination, current_amount = take_index(index_to_switch, used_list, current_amount, max_amount, index_combination)
           
    #         pass
            
    #     else:
    #         # cad si on est arrivé en fin de liste et qu'il n'existe plus d'autres index/actions à acheter pour faire
    #         # une combinaison, alors on passe 
    #         pass
    
    # best_investment_found = calculate_investment_return(total_combinations[0])
    # current_investment = calculate_investment_return(index_combination)
    # if best_investment_found < current_investment:
    #     total_combinations.pop()
    #     total_combinations.append(index_combination)
    # print("une fonction  add_combination s'est terminée")
    # print("le current_amount de notre action seule est" + str(current_amount))
    # print(f"son numéro d'index (donc le index_combination final) est de {index_combination}")
    
    


max_amount = 500
total_combinations = []
#1ere boucle récursive
current_amount = 0

start = time.perf_counter()

def main():
    # Pour chaque action, on va return la liste des combinaisons possibles avec celle-ci avec la fonction add_combinations,
    # on fait commencer la fonction add_combinations par l'index auquel on est rendu dans la boucle.
    for index in range(len(cost_list)):
        combination_start = [index]
        
        total_combinations = add_combinations(index, cost_list, current_amount, max_amount, combination_start, total_combinations)
        
        print("ON A ATTEINT LA FIN DE LA BOUCLE GLOBALE n°" + str(index+1))
        print(f"Pour l'instant le meilleur portefeuille d'actions est {total_combinations}")
        print(f"Son return est de {calculate_investment_return(total_combinations[0])}\n")


    print(f"Le meilleur portefeuille d'actions est {total_combinations}")
    print(f"Son return est de {calculate_investment_return(total_combinations[0])}")

main()

end = time.perf_counter()

print(f"Le temps d'exécution de la fonction bruteforce.py est de {end - start}")






        

#   On déclare une fonction qui prend un index, puis append dans une liste [le coût de l'action correspondant à cet 
#   index ainsi que son pourcentage de bénéfice]
#   On ajoute le coût à une variable coût total qui ne doit pas dépasser 500
#   On itère la boucle et on continue à append des listes [coût, bénéfice] jusqu'à ce qu'on arrive à 500
    
    

#   Il faut trouver un moyen pour pour qu'on passe à chaque fois qu'on a déjà effectué une combinaison



#   (l'index correspondrait au numéro de l'action - 1)



# Afficher le résultat
# main()



