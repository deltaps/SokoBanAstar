import fichier_python.NV as NV

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------ Ce module a pour but, à l'aide d'un algorithme a étoile, de trouver le chemin le plus court que le Prince doit empreinter pour atteindre sa destination ---------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#La classe pour créer un objet de type noeud qui représente une case avec sa position, son coût de déplacement et son heuristique
class noeud :
    def __init__(self,position = None, parent = None):
        self.parent = parent
        self.position = position
        self.cout = 0
        self.heuristique = 0
        self.somme = 0

    # Quand on compare deux classes (par exemple si on fait "if(classe1 == classe2") et bien cela appelle la fonction __eq__ qui va retourner le test suivant)
    def __eq__(self, other) :
        return self.position == other.position # Donc ici, quand on compare deux classes, en fait on compare leurs positions.



def a_etoile_prince(dep,arr,colision):
    openlist = [] #liste des noeuds à analyser
    closelist = [] #liste des noeuds déjà analysés
    noeuddepart = noeud(dep,None)
    noeudfin = noeud(arr,None)
    openlist.append(noeuddepart)

    # On fait une boucle tant que l'openlist n'est pas vide (si l'openlist est vide, alors il n'y a donc pas de possibilités)
    while len(openlist) > 0 :
        index = 0
        indexfinal = 0
        currentnode = openlist[0]
        # On choisit le meilleur noeud dans l'openlist, c'est à dire le noeud qui a le plus petite valeure "somme".
        for i in openlist:
            if (i.somme < currentnode.somme) :
                currentnode = i
                indexfinal = index
            index = index + 1
        # Une fois le meilleur noeud trouvé, on le retire de l'openlist et on le met dans la closelist :
        openlist.pop(indexfinal)
        closelist.append(currentnode)

        # Si on est arrivé au noeud de fin, alors il suffit simplement de retrouver le chemin inverse en remontant le parent du parent du parent... etc.
        #  Et nous avons le chemin le plus court :
        if (currentnode.position == noeudfin.position) :
            listefinal = []
            valeur = currentnode
            while (valeur.parent is not None) :
                listefinal.append(valeur.position)
                valeur = valeur.parent
            listefinal2 = []
            for i in range(len(listefinal)) : # Ici nous faisons une boucle pour inverser totalement la liste car en remontant les parents, les coordonnées sont dans l'ordre inverse.
                listefinal2.append(listefinal[len(listefinal) - 1 - i])
            return(listefinal2)

        # trouver les possibilités de déplacement
        listeposs = []
        for i in ([[50,0],[0,50],[0,-50],[-50,0]]) : # Les possibilités de déplacement pour notre jeu sont soit au dessus, en dessous, à gauche ou à droite.
            position = [currentnode.position[0] + i[0] ,currentnode.position[1] + i[1]]
            if (position not in colision) :
                listeposs.append(noeud(position,currentnode))

        # On vérifie si les possibilités ne sont pas déjà dans la closeliste ou dans l'openlist.
        # Si la condition est respectée, on met la possibilité dans l'openlist.
        for i in listeposs :
            testcontinue = 0
            testcontinue2 = 0
            for j in closelist :
                if j == i :
                    testcontinue = 1
            if testcontinue == 1 :
                continue
            i.heuristique = abs(i.position[0]-noeudfin.position[0]) + abs(i.position[1]-noeudfin.position[1])
            i.cout = currentnode.cout + 1
            i.somme = i.heuristique + i.cout
            for j in openlist :
                if (j == i) and (i.cout >= j.cout) :
                    testcontinue2 = 1
            if testcontinue2 == 1 :
                continue
            openlist.append(i)
