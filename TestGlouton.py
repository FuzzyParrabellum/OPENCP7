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


# La fonction Glouton calcule l'indice de tous les éléments de la liste, puis les classe par
# ordre de grandeur et prend ensuite chaque élément du plus grand au plus petit jusqu'à avoir
# rempli la capacité maximale.

def index_exists(list, index):
    if index < len(list):
        return True
    else:
        return False


def Gloutonic(list1, list2, max_capacity):
    new_list = []
    # On veut remplir new_list avec la liste d'actions optimales
    # pour se faire on doit faire un rapport de cout/weight pour chaque action
    # trier ensuite tous ses rapports avec le plus fort en 1er

    # 1ere phase de gloutonic ou on sort les actions par leur rapport cout*intéret
    for index in range(len(list1)):
        # Pour chaque index du nombre d'éléments dans la list d'actions
        rapport = [list1[index]*list2[index], index, list1[index]]
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
                    # pom pom pom
                    # si on est en fin de liste, pas besoin de continuer et faire index_exists
    print(f'La new_list finale est égale à {new_list}')

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

    return print(f'The current_capacity is {current_capacity} for the actions_indexes {actions_bought}')

        
Gloutonic(cost_list, benefit_list, 500)
# pour l'instant le big O erait de (n2 + n) ?
