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

    # On va d'abord à l'aide d'une première fonction remplir notre portefeuille d'actions d'une
    # première combinaison à l'aide de la fonction take_first_combination
    original_combination, current_amount, current_profit = take_first_combination(index,\
                                                         list_of_costs, list_of_profits)                                                  
    current_best = [original_combination, current_amount, current_profit]
    print(f"L'original_combination est de {original_combination}")
    if best_combination != []:
        current_best = return_best(best_combination, original_combination, list_of_costs, \
                list_of_profits, max_amount)  

    original_copy = original_combination[:]
    
    # On rajoute notre combinaison originale à la liste des combinaisons
    # En gardant notre dernier index, on enlève-ensuite l'avant dernier index, 
    # on renregistre, puis l'avant-avant
    # dernier etc. jusqu'à ce qu'on arrive à l'index d'où part notre combinaison

    #@doit maintenant trouver un moyen d'executer la deuxieme partie du plan, récursion?

    # pour chaque action entre la 1ere et la derniere action, on va effectuer la boucle qu'on a déjà
    # construite. A la fin d'une boucle, on va juste commencer celle-ci un avant-dernier item plus
    # près.

    copy_throwable = original_combination[:]
    copy_length = len(copy_throwable)


    for action in range(copy_length):
        if len(copy_throwable) <= 2:
            print("top")
            break
        else:
            print(len(copy_throwable))
            copy_throwable.pop(-2)
            copy_2 = copy_throwable[:]
            current_best = return_best(current_best, copy_2, list_of_costs, \
                list_of_profits, max_amount)
            print(current_best)


    # En gardant notre dernier-index ET celui d'avant, on fait la même chose etc.
    # Une fois fini ces deux boucles,
    # on pop le tout dernier index et on recommence les deux boucles


    return current_best


max_amount = 500
best_combination = []
#1ere boucle récursive
current_amount = 0

for index in range(len(cost_list)):
    combination_start = [index]
    
    best_combination = add_combinations(index, cost_list, benefit_list, max_amount, best_combination)
   
    
    print("ON A ATTEINT LA FIN DE LA BOUCLE GLOBALE n°" + str(index+1))
    print(f"Pour l'instant le meilleur portefeuille d'actions est {best_combination}")
    print(f"Son return est de {calculate_investment_return(best_combination[0])}\n")


print(f"Le meilleur portefeuille d'actions est {best_combination}")
print(f"Son return est de {calculate_investment_return(best_combination[0])}")


# Afficher le résultat
# main()



