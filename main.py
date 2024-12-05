"""Importation du fichier"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>
    Args:
        filename (str): nom du fichier à lire
    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    tab = []
    temp = []
    with open(filename, mode='r',encoding='utf8') as f:
        for i in f.readlines():
            l.append(i.replace("\n","").split(";"))
        for i in l:
            for j in i:
                temp.append(int(j))
            tab.append(temp)
            temp = []
    return tab

def get_list_k(data, k):
    """On retourne l'élément k de data"""
    return data[k]

def get_first(l):
    """On retourne le premier élément de  l"""
    return l[0]

def get_last(l):
    """On retourne le dernier élément de  l"""
    return l[-1]

def get_max(l):
    """On retourne le max de  l"""
    return max(l)

def get_min(l):
    """On retourne le minimum de  l"""
    return min(l)

def get_sum(l):
    """On retourne la somme des éléments de  l"""
    return sum(l)

#### Fonction principale

def main():
    """On teste les fonctions"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
        k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
