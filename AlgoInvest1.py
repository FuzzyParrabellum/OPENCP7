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


def take_index(index, current_amount, max_amount, original_combination = []):  
    print("take_index est appelée")
    # le problème actuel est qu'il faudrait qu'au début de chaque original_combination, il y ait notre index de base, peu faire ça avant
    if index_exists(cost_list, index+1) and (current_amount + cost_list[index+1] <= 500):
        # si il existe un index suivant (qu'on n'est donc pas à la fin de la liste) et que l'ajout du coût de son action
        # ne fait pas dépasser notre coût maximal d'achat, alors on achète cette action, et on l'ajoute à notre combinaison
        # actuelle, puis on relance la fonction pour voir si on peut encore rajouter une action à notre portefeuille
        current_amount += cost_list[index+1]
        original_combination.append(index+1)
        print("la première sorte de take_index est appelée")
        print("le current_amount est de " + str(current_amount))
        return take_index(index+1, current_amount, max_amount, original_combination)
        
    elif index_exists(cost_list, index+2):
        # si l'ajout du coût de l'action du prochain index fait dépasser le montant maximum, on vérifie si on peut
        # sauter un index (càd si ce n'était pas le dernier élément de la liste) et si c'est le cas on relance la fonction
        # pour voir si on peut rajouter cette action à notre portefeuille
        print("la deuxième sorte de take_index est appelée")
        print("le current_amount est de " + str(current_amount))
        return take_index(index+1, current_amount, max_amount, original_combination)
        
    print("une fonction take_index globale s'est terminée")
    print("le current_amount est de " + str(current_amount))
    return original_combination


max_amount = 500
total_combinations = []
#1ere boucle récursive
current_amount = 0
# Pour chaque action dans notre portefeuille d'action, on prend l'index de notre action que l'on passe dans la fonction
# take_index(). Celle-ci va nous retourner toutes les combinaisons possibles d'actions ne dépassant pas notre max_amount
# comprenant l'action que l'on a passé en paramètre et l'ajouter à notre liste total_combinations.
for index in range(len(cost_list)):
    combination_start = [index]
    # le problème actuel est que take_index ne fonctionne qu'une fois, càd qu'elle ne va return qu'une seule combinaison
    # et pas toutes les combinaisons possibles avec un seul index
    index_combinations = take_index(index, current_amount + cost_list[index], max_amount, combination_start)
    # print("la liste comprenant toutes les combinaisons d'un seul index est: \n")
    # print(index_combinations)
    total_combinations = total_combinations + index_combinations
    print("ON A ATTEINT LA FIN DE LA PREMIERE BOUCLE")

print("toutes les combinaisons possibles sont :")
print(total_combinations)




        

#   On déclare une fonction qui prend un index, puis append dans une liste [le coût de l'action correspondant à cet 
#   index ainsi que son pourcentage de bénéfice]
#   On ajoute le coût à une variable coût total qui ne doit pas dépasser 500
#   On itère la boucle et on continue à append des listes [coût, bénéfice] jusqu'à ce qu'on arrive à 500
    
    

#   Il faut trouver un moyen pour pour qu'on passe à chaque fois qu'on a déjà effectué une combinaison



#   (l'index correspondrait au numéro de l'action - 1)



# Afficher le résultat
# main()



