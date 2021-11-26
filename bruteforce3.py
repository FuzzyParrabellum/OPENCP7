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


def index_exists(list, index):
    if index < len(list):
        return True
    else:
        return False

def return_best(actual_best, possible_best, list_of_costs, list_of_profits, max):
    # On compare la meilleure combinaison trouvée jusqu'à présent avec une potentielle
    # meilleure combinaison, elle sera meilleure si elle ne dépasse pas la valeur 
    # d'achat maximum et si son profit est supérieur à la meilleure actuelle.
    possible_amount = 0
    possible_profit = 0
    # print(f'possible_best = {possible_best}')

    # On vérifie si possible_best est une combinaison d'index d'actions ou un seul index auquel cas 
    # on obtiendra un type 'int'
    # if isinstance(possible_best, int) == True:
    #     possible_amount += list_of_costs[possible_best]
    #     possible_profit += list_of_profits[possible_best]*list_of_costs[possible_best]
    #     if possible_amount > max:
    #         return actual_best

    #     else:
    #         actual_best_amount = actual_best[1]
    #         actual_best_profit = actual_best[2]

    #         if actual_best_amount > max or actual_best_profit < possible_profit:
    #             return [possible_best, possible_amount, possible_profit]

    #         else:
    #             return actual_best

    for i in possible_best:
        possible_amount += list_of_costs[i]
        possible_profit += list_of_profits[i]*list_of_costs[i]
    
    if possible_amount > max:
        return actual_best

    else:
        actual_best_amount = actual_best[1]
        actual_best_profit = actual_best[2]

        if actual_best_amount > max or actual_best_profit < possible_profit:
            return [possible_best, possible_amount, possible_profit]

        else:
            return actual_best



def take_first_combination(index, list_of_costs, list_of_profits):  
    
    original_combination = []
    current_amount = 0
    current_profit = 0
    # Si il existe encore une action après celle actuelle, et que la rajouter à notre combinaison ne ferait pas dépasser
    # notre montant d'achat du montant maximum, alors on la rajoute à la combinaison ainsi que son coût au montant d'achat
    # actuel
    for action_number in range(len(list_of_costs)):
        # la condition ci-dessous permet de ne pas rajouter les index déjà explorés par les précédents
        # appels de add_combinations
        if action_number in range(len(list_of_costs[0:index])):
            pass
        else:
            current_amount += list_of_costs[action_number]
            current_profit += list_of_profits[action_number]*list_of_costs[action_number]
            original_combination.append(action_number)   
        
    return original_combination, current_amount, current_profit

def calculate_investment_return(combination):
    total = 0
    for index in combination:
        total += (cost_list[index]*benefit_list[index])
    return total

        
def add_combinations(index, list_of_costs, list_of_profits, max_amount,\
                     best_combination = []):
    print("add_combinations est appelé")
    print(f"à la boucle n° {index}, la best_combination est {best_combination}")
    # à partir d'un index d'une liste donnée, on va chercher toutes les combinaisons possibles
    # à partir du reste des index de cette liste, ces combinaisons ne devant pas dépasser le maximum
    # autorisé d'achat symbolisé par la variable max_amount. 

    # condition pour vérifier qu'on a bien une liste et un coût maximal
    # if len(list_of_costs) == 0 or len(list_of_profits) == 0 or max_amount == 0:
    #     return 0

    # On va d'abord à l'aide d'une première fonction remplir notre portefeuille d'actions d'une
    # première combinaison à l'aide de la fonction take_first_combination
    original_combination, current_amount, current_profit = take_first_combination(index,\
                                                         list_of_costs, list_of_profits)                                                  
    current_best = [original_combination, current_amount, current_profit]
    print(f"L'original_combination est de {original_combination}")
    # La condition ci-dessous sert à déterminer si add_combinations a déjà été apellée et permet
    # de check quelle est la meilleure coombinaison entre les appels de add_combination précédents et
    # l'original_combination de notre add_combination actuelle.
    if best_combination != []:
        current_best = return_best(best_combination, original_combination, list_of_costs, \
                list_of_profits, max_amount)  

    original_copy = original_combination[:]
    
    # On rajoute notre combinaison originale à la liste des combinaisons
    # En gardant notre dernier index, on enlève-ensuite l'avant dernier index, 
    # on renregistre, puis l'avant-avant
    # dernier etc. jusqu'à ce qu'on arrive à l'index d'où part notre combinaison

    #@doit maintenant trouver un moyen d'executer la deuxieme partie du plan, récursion?

    # Pour chaque élément de notre original_combination - 1, on va effectuer la fonction A
    # BOUCLE FONCTION A qu'on effectue len(original_combination) - 1:
        # On ne rajoute aucune des deux dernières valeurs 
        # On rajoute seulement la dernière valeur
        # On rajoute seulement l'avant-dernière valeur
        # On rajoute les deux dernières valeurs
    action_index = [i for i in range(len(cost_list))]
    # Avec toute cette liste qu'on a déjà, on va faire exactement la même liste mais en rajoutant
    # l'index juste avant et ainsi de suite
    before_stop = 0
    combinations = []
    for element in range(len(original_combination) - 1):
        # print(f"Juste après le element, combinations={combinations}")
        before_stop += 1
        current_list = []
        if element == 0:
            # alors rien, c'est le premier truc
            current_list.append([action_index[-1]])
            current_list.append([action_index[-2]])
            current_list.append([action_index[-1], action_index[-2]])
            # print(f'Au premier tour current_list = {current_list}')
            combinations = combinations + current_list
            for combination in current_list:
                current_best = return_best(current_best, combination, list_of_costs, \
                list_of_profits, max_amount) 
            # print(f'Et combinations = {combinations}')
        # autrement truc
        else:
            index_to_add = element + 2
        #         # C'est à dire juste après notre 1ere condition
            # ici on ajoute l'index sur lequel devant toutes les combinaisons que l'on a déjà
            for combination in combinations:
                # on vérifie ci-dessous que combination est bien une combinaison et pas un index seul
                if isinstance(combination, int) == True:
                    current_list.append([action_index[-index_to_add], combination])
                    current_best = return_best(current_best, combination, list_of_costs, \
                    list_of_profits, max_amount) 
                else:
                    
                    new_combination = [action_index[-index_to_add]] + combination 
                    current_list.append(new_combination)
                    
                    current_best = return_best(current_best, new_combination, list_of_costs, \
                    list_of_profits, max_amount) 
            # ici on ajoute l'index seul à nos combinaisons
            combinations.insert(0, [action_index[-index_to_add]])
            current_best = return_best(current_best, [action_index[-index_to_add]], list_of_costs, \
                list_of_profits, max_amount) 
            # ici on rajoute toutes les combinaisons trouvées de current_list dans notre
            # combinations total
            combinations = current_list + combinations

        # if before_stop == 5:
        #     hello = input('what next?')
        #     print(hello)


        # if len(current_list) == 0:
        #     # alors rien, c'est le premier truc
        #     current_list.append(action_index[-1])
        #     current_list.append(action_index[-2])
        #     current_list.append([action_index[-1], action_index[-2]])
        # # autrement truc
        # else:
        #     if len(current_list) == 3:
        #         # C'est à dire juste après notre 1ere condition
        #         current_list.append(action_index[-3])
        #         for combination in current_list:
        #             current_list.append(action_index[-3] + combination)
        #     else:
        #         # le troisième cas quand on a la suite
        #         # il faudrait rendre ce 3e cas itérable peu importe le nombre d'actions et d'index,
        #         # et donc écrire autre chose que current_list.append(action_index[-4] + combination)
        #         current_list.append(action_index[-4])
        #         for combination in current_list:
        #             current_list.append(action_index[-4] + combination)

        # normalement à partir d'ici, devrait avoir le bon current_best et peut donc lancer le code
        # pour voir ce que ça donne.
        

        # Ici il faut faire une comparaison de chaque combinaison que l'on trouve avec notre
        # current best
        # Est-ce qu'il ne faudrait pas avoir bcp plus de combinaison / de boucles ?

        # pourrait supprimer current_list pour juste le remplacer par combinations, ou alors sortir
        # current_list d'un niveau et supprimer combinations, je pense que c'est redondant d'avoir
        # les deux.

    


    # pour chaque action entre la 1ere et la derniere action, on va effectuer la boucle qu'on a déjà
    # construite. A la fin d'une boucle, on va juste commencer celle-ci un avant-dernier item plus
    # près.
    # if len(original_copy) > 2:
    #     while len(original_copy) > 2:
    #         print("while loop")
    #         for item in range(len(original_copy)-2):
    #             copy_throwable = original_copy[:]
    #             copy_length = len(copy_throwable)

    #             last_index_starter = 2
    #             for action in range(copy_length):
    #                 if len(copy_throwable) <= last_index_starter:
    #                     # print("top")
    #                     break
    #                 else:
    #                     print(len(copy_throwable))
    #                     copy_throwable.pop(-last_index_starter)
    #                     copy_2 = copy_throwable[:]
    #                     current_best = return_best(current_best, copy_2, list_of_costs, \
    #                         list_of_profits, max_amount)
    #                     # print(current_best)
    #             last_index_starter += 1
    #         original_copy.pop()
    # else:
    #     pass


    # En gardant notre dernier-index ET celui d'avant, on fait la même chose etc.
    # Une fois fini ces deux boucles,
    # on pop le tout dernier index et on recommence les deux boucles


    return current_best


max_amount = 500
best_combination = []
current_amount = 0

start = time.perf_counter()
for index in range(len(cost_list)):
    combination_start = [index]
    
    best_combination = add_combinations(index, cost_list, benefit_list, max_amount, best_combination)
   
    
    print("ON A ATTEINT LA FIN DE LA BOUCLE GLOBALE n°" + str(index+1))
    print(f"Pour l'instant le meilleur portefeuille d'actions est {best_combination}")
    print(f"Son return est de {calculate_investment_return(best_combination[0])}\n")


print(f"Le meilleur portefeuille d'actions est {best_combination}")
print(f"Son return est de {calculate_investment_return(best_combination[0])}")

end = time.perf_counter()
print(f"Le temps d'exécution de la fonction bruteforce3.py est de {end - start}")

# Afficher le résultat
# main()



