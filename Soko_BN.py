import pygame
import fichier_python.NV as NV
import fichier_python.Menu as Menu
import fichier_python.IA as IA

finprog = True
testemenuprincipal = 0
pygame.init()

# On charge la musique de fond et définit son volume et ses caractéristiques.
musicfond = pygame.mixer.music.load("son/fond.mp3")
volume = pygame.mixer.music.get_volume()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.fadeout(300)
pygame.mixer.music.play(loops=-1, start=0.0)

# Début du programme
while finprog:
    menuchoix = 0
    if testemenuprincipal == 0: # Si c'est le cas, on ouvre le module menu.py qui va afficher le Menu du Jeu.
        nvchoisie = Menu.menu()
    else: # Sinon, on passe au niveau suivant.
        nvchoisie = nvchoisie + 1


# (1/3) --------------INITIALISATION DES VARIABLES, IMAGES, SONS, CLASSES, ETC... DONT NOUS AVONS BESOIN POUR NOTRE JEU---------------------------#

    #---------------------------------- Choix du niveau et de ses caractéristiques ----------------------------------------#

    # Dans un autre fichier nous avons crée des tableaux de valeurs spécifiques à chaque niveau correspondant
    # aux positions des cookies au départ, de la position du Prince au départ, aux emplacements des murs, à la taille de la fenêtre etc...
    if nvchoisie == 1: # Si le niveau choisi est le niveau 1 :
        murnv = NV.murnv1() # tableau des coordonnées des murs/colisions
        position = NV.positionnv1() # tableau comportant le nombre de cookies du niveau et la position de départ du Prince et des Cookies.
        display = NV.displaynv1() # tableau correspondant à la taille de la fenêtre.
        positionplacé = NV.positionplacénv1() # tableau comportant les coordonnées des paniers où les cookies doivent aller.
    elif nvchoisie == 2: # Si le niveau choisi est le niveau 2 :
        murnv = NV.murnv2()
        position = NV.positionnv2()
        display = NV.displaynv2()
        positionplacé = NV.positionplacénv2()
    elif nvchoisie == 3: # Si le niveau choisi est le niveau 3 :
        murnv = NV.murnv3()
        position = NV.positionnv3()
        display = NV.displaynv3()
        positionplacé = NV.positionplacénv3()
    elif nvchoisie == 4: # Si le niveau choisi est le niveau 4 :
        murnv = NV.murnv4()
        position = NV.positionnv4()
        display = NV.displaynv4()
        positionplacé = NV.positionplacénv4()
    elif nvchoisie == 5: # Si le niveau choisi est le niveau 5 :
        murnv = NV.murnv5()
        position = NV.positionnv5()
        display = NV.displaynv5()
        positionplacé = NV.positionplacénv5()
    elif nvchoisie == 6: # Si le niveau choisi est le niveau 6 :
        murnv = NV.murnv6()
        position = NV.positionnv6()
        display = NV.displaynv6()
        positionplacé = NV.positionplacénv6()

    #-----------------------------------------------------------------------------------------#
    p=True
    while p : # La boucle sur p correspond à l'initialisation du terrain de jeu.

        screen = pygame.display.set_mode((display[0],display[1]))

        pygame.display.set_caption("Soko BN")

        #---------------------------------- images / sons ----------------------------------------#

        # Chargement de toutes les images dont nous avons besoin pour le jeu :
        reprendresanshover = pygame.image.load("images/menujeux/reprendresanshover.png")
        reprendreavechover = pygame.image.load("images/menujeux/reprendreavechover.png")
        optionsanshover = pygame.image.load("images/menujeux/optionsanshover.png")
        optionavechover = pygame.image.load("images/menujeux/optionavechover.png")
        menusanshover = pygame.image.load("images/menujeux/retoursanshover.png")
        menuavechover = pygame.image.load("images/menujeux/retouravechover.png")
        background_image1 = pygame.image.load("images/menu/fondmenu602.png").convert()
        ropt = pygame.image.load("images/menu/ropt.png")
        esc = pygame.image.load("images/menu/esc.png")
        fleche = pygame.image.load("images/menu/touche.png")
        flècheretour = pygame.image.load("images/menu/flècheSansHover2.png")
        jou = pygame.image.load("images/fin/jougagne.png")
        ord = pygame.image.load("images/fin/ordgagne.png")
        if nvchoisie == 1 or nvchoisie == 2:
            sousmenu = pygame.image.load("images/menu/SousMenu500500.png")
        if nvchoisie == 3 or nvchoisie == 4:
            sousmenu = pygame.image.load("images/menu/SousMenu600600.png")
        if nvchoisie == 5 or nvchoisie == 6:
            sousmenu = pygame.image.load("images/menu/SousMenu650650.png")

        # Chargement du terrain en fonction du niveau choisi.
        if nvchoisie == 1:
            background_image = pygame.image.load("images/niveau/FORETniv1.jpg").convert()
        elif nvchoisie == 2:
            background_image = pygame.image.load("images/niveau/FORETniv2.jpg").convert()
        elif nvchoisie == 3:
            background_image = pygame.image.load("images/niveau/FORETniv3.jpg").convert()
        elif nvchoisie == 4:
            background_image = pygame.image.load("images/niveau/FORETniv4.jpg").convert()
        elif nvchoisie == 5:
            background_image = pygame.image.load("images/niveau/FORETniv5.jpg").convert()
        elif nvchoisie == 6:
            background_image = pygame.image.load("images/niveau/FORETniv6.jpg").convert()

        # Images dont nous avons besoin pour afficher un 'timer' durant la partie :
        img0 = pygame.image.load("images/timer/0.png")
        img1 = pygame.image.load("images/timer/1.png")
        img2 = pygame.image.load("images/timer/2.png")
        img3 = pygame.image.load("images/timer/3.png")
        img4 = pygame.image.load("images/timer/4.png")
        img5 = pygame.image.load("images/timer/5.png")
        img6 = pygame.image.load("images/timer/6.png")
        img7 = pygame.image.load("images/timer/7.png")
        img8 = pygame.image.load("images/timer/8.png")
        img9 = pygame.image.load("images/timer/9.png")

        # Tous les sons/musiques dont nous avons besoins :
        sonfinniveau = pygame.mixer.Sound("son/finniveau.wav")
        sonpas = pygame.mixer.Sound("son/pas.wav")
        sonpas2 = pygame.mixer.Sound("son/pas2.wav")
        sonpanier = pygame.mixer.Sound("son/panier.wav")
        sonrestart = pygame.mixer.Sound("son/restart.wav")
        sonpause = pygame.mixer.Sound("son/pause.wav")
        sonvictoire = pygame.mixer.Sound("son/victoire.wav")
        sondefaite = pygame.mixer.Sound("son/defaite.wav")

        # Chargement de l'image du Prince et l'image des Cookies :
        ImgPrince = pygame.image.load("images/cookies/king50.png")
        ImgCookie = pygame.image.load("images/cookies/cookie.png")

        #------------------------------------------------------------------------------------------------#

        #--------------------------------- classes et variables------------------------------------------#

        # Classe pour créer chaque Cookie
        class Cookie:
            def __init__(self,name,position,ImgCookie,compteur):
                self.name = name
                self.position = position
                self.compteurson = compteur
                self.image = ImgCookie

            def movecook(self): # Fonction qui permet d'afficher le cookie.
                screen.blit(self.image,self.position)

        # Classe pour créer le Prince
        class Prince:
            def __init__(self,name,position,ImgPrince):
                self.name = name
                self.position = position
                self.image = ImgPrince

            def moveprince(self): # Fonction qui permet d'afficher le Prince.
                screen.blit(self.image,self.position)

        # On crée les objets de type Cookie.
        Cookie1 = Cookie("Cookie1",ImgCookie.get_rect(),ImgCookie,0)
        Cookie2 = Cookie("Cookie2",ImgCookie.get_rect(),ImgCookie,0)
        Cookie3 = Cookie("Cookie3",ImgCookie.get_rect(),ImgCookie,0)
        Cookie4 = Cookie("Cookie4",ImgCookie.get_rect(),ImgCookie,0)
        Cookie5 = Cookie("Cookie5",ImgCookie.get_rect(),ImgCookie,0)
        Cookie6 = Cookie("Cookie6",ImgCookie.get_rect(),ImgCookie,0)
        Cookie7 = Cookie("Cookie7",ImgCookie.get_rect(),ImgCookie,0)

        tabcookie = [] # On crée un tableau dans lequel nous mettons tous les objets de types cookies afin de pouvoir faire des boucles pour vérifier chaque cookie.
        tabcookie.append(Cookie1)
        tabcookie.append(Cookie2)
        tabcookie.append(Cookie3)
        tabcookie.append(Cookie4)
        tabcookie.append(Cookie5)
        tabcookie.append(Cookie6)
        tabcookie.append(Cookie7)

        Prince = Prince("Prince",[50,50],ImgPrince) # On Crée l'objet Prince.

        testehoverreprendre = 0
        testehoveroption = 0
        testehovermenu = 0

        # Cette nouvelle variable va nous servir pour le 'timer' durant la partie :
        tempsasoustraire = pygame.time.get_ticks() * 0.001

        # Nous utlisons le tableau 'position' pour placer les cookies sur leur emplacement de départ :
        for i in range(position[0][0]):
            tabcookie[i].position = tabcookie[i].position.move(position[i + 2][0],position[i+2][1])
            tabcookie[i].movecook()

        # Le tableau 'testgagne' nous sert à vérifier si le joueur a placé tous les cookies ou non. Au départ nous le remplissons de '0'.
        #  Mais dès qu'un cookie rentre dans un panier nous remplaçons un '0' par un '1' ce qui nous permet de savoir quand est-ce que le joueur a placé tous les cookies.
        testegagne = []
        for i in range(13):
            testegagne.append(0)

        #---------------------------------------------------------------------------------------------------------#

        # Cette commande pygame nous sert à déplacer le personnage en restant appuyer sur une touche au lieu d'appuyer plusieurs fois d'affilé sur la même touche :
        pygame.key.set_repeat(220,80)

        pygame.display.update()
        jeu = True

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# (2/3) ----------------------------------------------------------------DEBUT DE LA PARTIE-----------------------------------------------------------------#
        while jeu:
            testepaslancementia = 0
            for event in pygame.event.get(): # Vérification des interactions de l'utilisateur
                if event.type == pygame.QUIT: # Si l'utilisateur appuie sur la croix de fermeture, le jeu se ferme.
                    jeu = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN: # si l'utilisateur enfonce une touche
                    if menuchoix == 0:

                        #--------------------------------- Déplacement vers la gauche------------------------------------------#

                        if event.key == pygame.K_LEFT: # si la touche enfoncée est la flèche de gauche
                            sonpas.play()
                            colisionperso = 0
                            colisioncookie = 0
                            colisioncookiecookie = 0
                            for i in murnv : # on vérifie si l'emplacement où le joueur veut aller est un mur ou non. Si c'est un mur, le déplacement dans cette direction est impossible.
                                if i[0] == Prince.position[0] - 50 and i[1] == Prince.position[1]:
                                    colisionperso = 1
                            for i in murnv:  # on vérifie si un cookie est à côté du Joueur et qu'à côté de ce cookie il y a un mur. Si c'est le cas, le déplacement dans cette direction est impossible.
                                for j in range(position[0][0]):
                                    if i[0] == tabcookie[j].position[0] - 50 and i[1] == tabcookie[j].position[1] and Prince.position[0] == tabcookie[j].position[0] + 50 and Prince.position[1] == tabcookie[j].position[1]:
                                        colisioncookie = 1
                            for i in range(position[0][0]): # on vérifie si un cookie est à côté du Joueur et qu'à côté de ce cookie il y a un autre cookie. Si c'est le cas, le déplacement dans cette direction est impossible.
                                for j in range(position[0][0]):
                                    if j != i:
                                        if Prince.position[0] - 50 == tabcookie[i].position[0] and Prince.position[1] == tabcookie[i].position[1] and  tabcookie[i].position[0] - 50 == tabcookie[j].position[0] and tabcookie[i].position[1] == tabcookie[j].position[1] or Prince.position[0] - 50 == tabcookie[j].position[0] and Prince.position[1] == tabcookie[j].position[1] and tabcookie[j].position[0] - 50 == tabcookie[i].position[0] and tabcookie[j].position[1] == tabcookie[i].position[1]:
                                            colisioncookiecookie = 1
                            if colisionperso == 0 and colisioncookie == 0 and colisioncookiecookie == 0:  # Si toutes les conditions précédentes sont respectées, le déplacement est donc possible.
                                testecookiemove = 0
                                for i in range(position[0][0]): # On déplace le Prince de 50 pixels vers la gauche et un cookie si cela est nécéssaire.
                                    if Prince.position[0] == tabcookie[i].position[0] + 50  and Prince.position[1] == tabcookie[i].position[1]:
                                        Prince.position[0] = Prince.position[0] - 50
                                        tabcookie[i].position = tabcookie[i].position.move(-50,0)
                                        testecookiemove = 1
                                if testecookiemove == 0:
                                    Prince.position[0] = Prince.position[0] - 50

                        #---------------------------------------------------------------------------------------------------------#

                        # On effectue les mêmes vérifications pour chaque direction choisies par l'utilisateur

                        #--------------------------------- Déplacement vers la droite---------------------------------------------#

                        if event.key == pygame.K_RIGHT : # si la touche enfoncée est la flèche de droite
                            sonpas.play()
                            colisionperso = 0
                            colisioncookie = 0
                            colisioncookiecookie = 0
                            for i in murnv:
                                if i[0] == Prince.position[0] + 50 and i[1] == Prince.position[1]:
                                    colisionperso = 1
                            for i in murnv:
                                for j in range(position[0][0]):

                                    if i[0] == tabcookie[j].position[0] + 50 and i[1] == tabcookie[j].position[1] and Prince.position[0] == tabcookie[j].position[0] - 50 and Prince.position[1] == tabcookie[j].position[1]:
                                        colisioncookie = 1
                            for i in range(position[0][0]):
                                for j in range(position[0][0]):
                                    if j != i:
                                        if Prince.position[0] + 50 == tabcookie[i].position[0] and Prince.position[1] == tabcookie[i].position[1] and  tabcookie[i].position[0] + 50 == tabcookie[j].position[0] and tabcookie[i].position[1] == tabcookie[j].position[1] or Prince.position[0] + 50 == tabcookie[j].position[0] and Prince.position[1] == tabcookie[j].position[1] and tabcookie[j].position[0] + 50 == tabcookie[i].position[0] and tabcookie[j].position[1] == tabcookie[i].position[1]:
                                            colisioncookiecookie = 1
                            if colisionperso == 0 and colisioncookie == 0 and colisioncookiecookie == 0:
                                testecookiemove = 0
                                for i in range(position[0][0]):
                                    if Prince.position[0] + 50 == tabcookie[i].position[0] and Prince.position[1] == tabcookie[i].position[1]:
                                        Prince.position[0] = Prince.position[0] + 50
                                        tabcookie[i].position = tabcookie[i].position.move(50,0)
                                        testecookiemove = 1
                                if testecookiemove == 0:
                                    Prince.position[0] = Prince.position[0] + 50

                        #---------------------------------------------------------------------------------------------------------#

                        #--------------------------------- Déplacement vers le haut-----------------------------------------------#

                        if event.key == pygame.K_UP: # si la touche enfoncée est la flèche du haut
                            sonpas2.play()
                            colisionperso = 0
                            colisioncookie = 0
                            colisioncookiecookie = 0
                            for i in murnv:
                                if i[0] == Prince.position[0] and i[1] == Prince.position[1] - 50:
                                    colisionperso = 1
                            for i in murnv:
                                for j in range(position[0][0]):

                                    if i[0] == tabcookie[j].position[0] and i[1] == tabcookie[j].position[1] - 50 and Prince.position[0] == tabcookie[j].position[0] and Prince.position[1] == tabcookie[j].position[1] + 50:
                                        colisioncookie = 1
                            for i in range(position[0][0]):
                                for j in range(position[0][0]):
                                    if j != i:
                                        if Prince.position[1] - 50 == tabcookie[i].position[1] and Prince.position[0] == tabcookie[i].position[0] and  tabcookie[i].position[1] - 50 == tabcookie[j].position[1] and tabcookie[i].position[0] == tabcookie[j].position[0] or Prince.position[1] - 50 == tabcookie[j].position[1] and Prince.position[0] == tabcookie[j].position[0] and tabcookie[j].position[1] - 50 == tabcookie[i].position[1] and tabcookie[j].position[0] == tabcookie[i].position[0]:
                                            colisioncookiecookie = 1
                            if colisionperso == 0 and colisioncookie == 0 and colisioncookiecookie == 0:
                                testecookiemove = 0
                                for i in range(position[0][0]):

                                    if Prince.position[1] == tabcookie[i].position[1] + 50 and Prince.position[0] == tabcookie[i].position[0]:
                                        Prince.position[1] = Prince.position[1] - 50
                                        tabcookie[i].position = tabcookie[i].position.move(0,-50)
                                        testecookiemove = 1
                                if testecookiemove == 0 :
                                    Prince.position[1] = Prince.position[1] - 50

                        #---------------------------------------------------------------------------------------------------------#

                        #--------------------------------- Déplacement vers le bas------------------------------------------------#

                        if event.key == pygame.K_DOWN: # si la touche enfoncée est la flèche du bas
                            sonpas2.play()
                            colisionperso = 0
                            colisioncookie = 0
                            colisioncookiecookie = 0
                            for i in murnv:
                                if i[0] == Prince.position[0] and i[1] == Prince.position[1] + 50:
                                    colisionperso = 1
                            for i in murnv:
                                for j in range (position[0][0]):

                                    if i[0] == tabcookie[j].position[0] and i[1] == tabcookie[j].position[1] + 50 and Prince.position[0] == tabcookie[j].position[0] and Prince.position[1] == tabcookie[j].position[1] - 50:
                                        colisioncookie = 1
                            for i in range(position[0][0]):
                                for j in range(position[0][0]):
                                    if j != i:
                                        if Prince.position[1] + 50 == tabcookie[i].position[1] and Prince.position[0] == tabcookie[i].position[0] and  tabcookie[i].position[1] + 50 == tabcookie[j].position[1] and tabcookie[i].position[0] == tabcookie[j].position[0] or Prince.position[1] + 50 == tabcookie[j].position[1] and Prince.position[0] == tabcookie[j].position[0] and tabcookie[j].position[1] + 50 == tabcookie[i].position[1] and tabcookie[j].position[0] == tabcookie[i].position[0]:
                                            colisioncookiecookie = 1
                            if colisionperso == 0 and colisioncookie == 0 and colisioncookiecookie == 0:
                                testecookiemove = 0
                                for i in range(position[0][0]):

                                    if Prince.position[1] == tabcookie[i].position[1] - 50 and Prince.position[0] == tabcookie[i].position[0]:
                                        Prince.position[1] = Prince.position[1] + 50
                                        tabcookie[i].position = tabcookie[i].position.move(0,50)
                                        testecookiemove = 1
                                if testecookiemove == 0 :
                                    Prince.position[1] = Prince.position[1] + 50

                        #---------------------------------------------------------------------------------------------------------#

                        if event.key == pygame.K_r: # si la touche enfoncée est la touche 'r' on reinitialise le niveau
                            jeu = False
                            sonrestart.play()
                            testepaslancementia = 1
                        if event.key == pygame.K_ESCAPE: # si la touche enfoncée est la touche 'esc' cela va entraîner l'ouverture du menu pause.
                            sonpause.play()
                            menuchoix = 1 # la variable menuchoix vaut maintenant 1 et plus loins dans le programme (ligne 423) nous faisons le test pour ouvrir ou non le menu pause.

                    elif menuchoix == 1: # Si la variable menuchoix vaut déjà 1 et que l'utilisateur rappuie sur 'esc' le jeu reprend.
                        if event.key == pygame.K_ESCAPE:
                            menuchoix = 0


            #------------On met à jour l'affichage des images en fonction de ce qu'a fait l'utilisateur----------------#

            # On regarde si il y a des cookies dans des paniers, si oui on change l'image du panier et du cookie pour le transformer en l'image du cookie dans le panier.
            # De plus, il y a "compteurson" pour chaque cookie pour qu'il fasse un bruit quand il rentre dans un panier
            for i in range(position[0][0]):
                nombreinter = 0
                testecookienoir = 0
                for j in range(position[0][0]):

                    if (tabcookie[i].position == (positionplacé[j][0], positionplacé[j][1], 50, 50)):
                        tabcookie[i].image = pygame.image.load("images/cookies/cookieNoir.png")
                        testegagne[i] = 1
                        testecookienoir = 1
                        if tabcookie[i].compteurson == 0 :
                            tabcookie[i].compteurson = 1
                    elif(testecookienoir == 0):
                        tabcookie[i].image = pygame.image.load("images/cookies/cookie.png")
                        testegagne[i] = 0
                        nombreinter = nombreinter + 1
                    if nombreinter == position[0][0] :
                        tabcookie[i] == 0
                        tabcookie[i].compteurson = 0
            for i in range(position[0][0]) :
                if tabcookie[i].compteurson == 1 :
                    sonpanier.play()
                    tabcookie[i].compteurson = 2

            # On regarde si tous les cookies sont dans un panier différent, si oui, le joueur a gagné, on arrête la partie et on lance le niveau d'après.
            # Sinon, On utilise la fonction "movecook()" de la classe cookie pour mettre à jour la position de tous les cookies, ensuite on affiche un nouveau terrain sur lequel on affiche les cookies avec leurs nouvelles positions.
            compteur = 0
            for honda in testegagne :
                if honda == 1 :
                    compteur = compteur + 1
            if compteur == position[0][0]:
                sonfinniveau.play()
                if nvchoisie == 6:
                    testemenuprincipal = 0
                else:
                    testemenuprincipal = 1
                jeu = False
                p = False
            else :
                testemenuprincipal = 0

            # On affiche le terrain
            screen.blit(background_image, [0, 0])

            #On place les cookies avec leurs nouvelles positions
            for m in range(len(positionplacé)) :
                tabcookie[m].movecook()

            #On place le Prince avec aussi sa nouvelle position
            Prince.moveprince()

            #---------------------------------------------------------------------------------------------------------#

            #------------------------------------------Menu Pause-----------------------------------------------------#

            # affichage du menu/pause en pleine partie quand on appuie sur la touche echap.
            if menuchoix == 1:
                if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                    screen.blit(sousmenu, [0,0])
                    if testehoverreprendre == 0:
                        screen.blit(reprendresanshover, [75,70])
                    if testehoverreprendre == 1:
                        screen.blit(reprendreavechover, [75,70])
                    if testehoveroption == 0:
                        screen.blit(optionsanshover, [75,170])
                    if testehoveroption == 1:
                        screen.blit(optionavechover, [75,170])
                    if testehovermenu == 0:
                        screen.blit(menusanshover, [75,270])
                    if testehovermenu == 1:
                        screen.blit(menuavechover, [75,270])
                if nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                    screen.blit(sousmenu, [0,0])
                    if testehoverreprendre == 0:
                        screen.blit(reprendresanshover, [125,120])
                    if testehoverreprendre == 1:
                        screen.blit(reprendreavechover, [125,120])
                    if testehoveroption == 0:
                        screen.blit(optionsanshover, [125,220])
                    if testehoveroption == 1:
                        screen.blit(optionavechover, [125,220])
                    if testehovermenu == 0:
                        screen.blit(menusanshover, [125,320])
                    if testehovermenu == 1:
                        screen.blit(menuavechover, [125,320])
                if nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                    screen.blit(sousmenu, [0,0])
                    if testehoverreprendre == 0:
                        screen.blit(reprendresanshover, [150,145])
                    if testehoverreprendre == 1:
                        screen.blit(reprendreavechover, [150,145])
                    if testehoveroption == 0:
                        screen.blit(optionsanshover, [150,245])
                    if testehoveroption == 1:
                        screen.blit(optionavechover, [150,245])
                    if testehovermenu == 0:
                        screen.blit(menusanshover, [150,345])
                    if testehovermenu == 1:
                        screen.blit(menuavechover, [150,345])

            # Affichage de la page après avoir appuyé sur "echap" puis sur le bouton "regle"
            if menuchoix == 2 :
                screen.blit(sousmenu, [0,0])
                if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                    screen.blit(ropt, [320,35])
                    screen.blit(fleche, [100,200])
                    screen.blit(esc, [100,32])
                    screen.blit(flècheretour, [20,400])
                if nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                    screen.blit(ropt, [370,85])
                    screen.blit(fleche, [150,250])
                    screen.blit(esc, [150,82])
                    screen.blit(flècheretour, [70,450])
                if nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                    screen.blit(ropt, [395,110])
                    screen.blit(fleche, [175,275])
                    screen.blit(esc, [175,107])
                    screen.blit(flècheretour, [95,475])

            if menuchoix == 1 or menuchoix == 2 : # Si menuchoix vaut 1 ou 2 on active l'interaction avec menupause avec des hover et des endroits cliquables.
                if event.type == pygame.MOUSEMOTION:
                    posSouris = pygame.mouse.get_pos()
                    if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                        if 75 < posSouris[0] < 425 and 70 < posSouris[1] < 130 and menuchoix == 1:
                            testehoverreprendre = 1
                        else:
                            testehoverreprendre = 0
                        if 90 < posSouris[0] < 400 and 170 < posSouris[1] < 230 and menuchoix == 1:
                            testehoveroption = 1
                        else:
                            testehoveroption = 0
                        if 75 < posSouris[0] < 425 and 270 < posSouris[1] < 330 and menuchoix == 1:
                            testehovermenu = 1
                        else:
                            testehovermenu = 0
                    elif nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                        if 125 < posSouris[0] < 475 and 120 < posSouris[1] < 180 and menuchoix == 1:
                            testehoverreprendre = 1
                        else:
                            testehoverreprendre = 0
                        if 140 < posSouris[0] < 450 and 220 < posSouris[1] < 280 and menuchoix == 1:
                            testehoveroption = 1
                        else:
                            testehoveroption = 0
                        if 125 < posSouris[0] < 475 and 320 < posSouris[1] < 380 and menuchoix == 1:
                            testehovermenu = 1
                        else:
                            testehovermenu = 0
                    elif nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                        if 150 < posSouris[0] < 500 and 145 < posSouris[1] < 205 and menuchoix == 1:
                            testehoverreprendre = 1
                        else:
                            testehoverreprendre = 0
                        if 165 < posSouris[0] < 475 and 245 < posSouris[1] < 305 and menuchoix == 1:
                            testehoveroption = 1
                        else:
                            testehoveroption = 0
                        if 150 < posSouris[0] < 500 and 345 < posSouris[1] < 405 and menuchoix == 1:
                            testehovermenu = 1
                        else:
                            testehovermenu = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posSouris = pygame.mouse.get_pos()
                    if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                        if 75 < posSouris[0] < 425 and 70 < posSouris[1] < 130 and menuchoix != 2:
                            menuchoix = 0
                        if 90 < posSouris[0] < 400 and 170 < posSouris[1] < 230 and menuchoix != 2:
                            menuchoix = 2
                        if 20 < posSouris[0] < 150 and 300 < posSouris[1] < 450 :
                            menuchoix = 1
                        if 75 < posSouris[0] < 425 and 270 < posSouris[1] < 330 and menuchoix != 2:
                            testepaslancementia = 1
                            jeu = False
                            p = False
                    elif nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                        if 125 < posSouris[0] < 475 and 120 < posSouris[1] < 180 and menuchoix != 2:
                            menuchoix = 0
                        if 140 < posSouris[0] < 450 and 220 < posSouris[1] < 280 and menuchoix != 2:
                            menuchoix = 2
                        if 70 < posSouris[0] < 200 and 350 < posSouris[1] < 500 :
                            menuchoix = 1
                        if 125 < posSouris[0] < 475 and 320 < posSouris[1] < 380 and menuchoix != 2:
                            testepaslancementia = 1
                            jeu = False
                            p = False
                    elif nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                        if 150 < posSouris[0] < 500 and 145 < posSouris[1] < 205 and menuchoix != 2:
                            menuchoix = 0
                        if 165 < posSouris[0] < 475 and 245 < posSouris[1] < 305 and menuchoix != 2:
                            menuchoix = 2
                        if 95 < posSouris[0] < 225 and 375 < posSouris[1] < 525 :
                            menuchoix = 1
                        if 150 < posSouris[0] < 500 and 345 < posSouris[1] < 405 and menuchoix != 2:
                            testepaslancementia = 1
                            jeu = False
                            p = False

            #---------------------------------------------------------------------------------------------------------#

            #-------------------------------------------------Timer---------------------------------------------------#

            # Boucle que nous avons crée pour afficher le "timer" au fil du temps.
            temps = round((pygame.time.get_ticks() * 0.001) - tempsasoustraire)
            j = 0
            for i in str(temps): # En fonction du temps, on affiche les chiffres correspondants.
                if j == 0 and menuchoix == 0:
                    if i == "0":
                        screen.blit(img0, [300,0])
                    if i == "1":
                        screen.blit(img1, [300,0])
                    if i == "2":
                        screen.blit(img2, [300,0])
                    if i == "3":
                        screen.blit(img3, [300,0])
                    if i == "4":
                        screen.blit(img4, [300,0])
                    if i == "5":
                        screen.blit(img5, [300,0])
                    if i == "6":
                        screen.blit(img6, [300,0])
                    if i == "7":
                        screen.blit(img7, [300,0])
                    if i == "8":
                        screen.blit(img8, [300,0])
                    if i == "9":
                        screen.blit(img9, [300,0])
                if j == 1 and menuchoix == 0:
                    if i == "0":
                        screen.blit(img0, [350,0])
                    if i == "1":
                        screen.blit(img1, [350,0])
                    if i == "2":
                        screen.blit(img2, [350,0])
                    if i == "3":
                        screen.blit(img3, [350,0])
                    if i == "4":
                        screen.blit(img4, [350,0])
                    if i == "5":
                        screen.blit(img5, [350,0])
                    if i == "6":
                        screen.blit(img6, [350,0])
                    if i == "7":
                        screen.blit(img7, [350,0])
                    if i == "8":
                        screen.blit(img8, [350,0])
                    if i == "9":
                        screen.blit(img9, [350,0])
                if j == 2 and menuchoix == 0:
                    if i == "0":
                        screen.blit(img0, [400,0])
                    if i == "1":
                        screen.blit(img1, [400,0])
                    if i == "2":
                        screen.blit(img2, [400,0])
                    if i == "3":
                        screen.blit(img3, [400,0])
                    if i == "4":
                        screen.blit(img4, [400,0])
                    if i == "5":
                        screen.blit(img5, [400,0])
                    if i == "6":
                        screen.blit(img6, [400,0])
                    if i == "7":
                        screen.blit(img7, [400,0])
                    if i == "8":
                        screen.blit(img8, [400,0])
                    if i == "9":
                        screen.blit(img9, [400,0])
                j = j + 1

                #---------------------------------------------------------------------------------------------------------#

            pygame.display.update()

# (3/3) ----------------------------------------------------------------PARTIE IA-----------------------------------------------------------------#

        # Après que le joueur ai fini le niveau nous faisons jouer l'IA, ensuite nous comparons les deux 'timer' et nous affichons le gagnant :
        if testepaslancementia == 0:

            tempsia = IA.IA(nvchoisie,3) # On utilise la fonction 'IA' du module "IA.py" pour faire jouer l'IA et la fonction retourne le temps qu'à pris l'IA pour faire le niveau.
            if temps < tempsia: # On compare les deux timers.
                if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                    screen.blit(jou,[125,150])
                    sonvictoire.play()
                if nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                    screen.blit(jou,[180,225])
                    sonvictoire.play()
                if nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                    screen.blit(jou,[200,250])
                    sonvictoire.play()
            else:
                if nvchoisie == 1 or nvchoisie == 2: #Si le niveau choisi est le niveau 1 ou 2
                    screen.blit(ord,[125,150])
                    sondefaite.play()
                if nvchoisie == 3 or nvchoisie == 4: #Si le niveau choisi est le niveau 3 ou 4
                    screen.blit(ord,[180,225])
                    sondefaite.play()
                if nvchoisie == 5 or nvchoisie == 6: #Si le niveau choisi est le niveau 5 ou 6
                    screen.blit(ord,[200,250])
                    sondefaite.play()

            pygame.display.update()

            # Nous marquons un temps d'arrêt entre la passage d'un niveau à un autre :
            pygame.time.wait(2500)

#----------------------------------------------------------------------------------------------------------------------------------------------------#
