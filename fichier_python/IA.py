import pygame
import fichier_python.NV as NV
import fichier_python.Menu as Menu
import fichier_python.dossier_IA.algoAPrince as algoAPrince
import fichier_python.dossier_IA.algoACookie as algoACookie

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------Ce module permet de faire intervenir l'IA suite à la partie de l'utilisateur-------------------------------------------------------------------#
#-----------La partie INITIALISATION de ce module est très similaire à celui du programme principal car il s'agit du même principe de jeu sauf que c'est une IA qui joue à la place du joueur.---------------#
#--------------------------------------------Nous avons donc décidé de ne pas ajouter tous les commentaires car ils sont déjà expliqués dans le programme principal.-----------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def IA(nvchoisie,difficulte):

    # Début du programme
    finprog = True
    testemenuprincipal = 0
    pygame.init()
    while finprog:
        menuchoix = 0

# (1/2) --------------INITIALISATION DES VARIABLES, IMAGES, SONS, CLASSES, ETC... DONT NOUS AVONS BESOIN POUR NOTRE JEU ---------------------------#

    #---------------------------------- Choix du niveau et de ses caractéristiques ----------------------------------------------------------------#

        if nvchoisie == 1:
            murnv = NV.murnv1()
            position = NV.positionnv1()
            display = NV.displaynv1()
            positionplacé = NV.positionplacénv1()
        elif nvchoisie == 2:
            murnv = NV.murnv2()
            position = NV.positionnv2()
            display = NV.displaynv2()
            positionplacé = NV.positionplacénv2()
        elif nvchoisie == 3:
            murnv = NV.murnv3()
            position = NV.positionnv3()
            display = NV.displaynv3()
            positionplacé = NV.positionplacénv3()
        elif nvchoisie == 4:
            murnv = NV.murnv4()
            position = NV.positionnv4()
            display = NV.displaynv4()
            positionplacé = NV.positionplacénv4()
        elif nvchoisie == 5:
            murnv = NV.murnv5()
            position = NV.positionnv5()
            display = NV.displaynv5()
            positionplacé = NV.positionplacénv5()
        elif nvchoisie == 6:
            murnv = NV.murnv6()
            position = NV.positionnv6()
            display = NV.displaynv6()
            positionplacé = NV.positionplacénv6()

    #--------------------------------------------------------------------------------------------------------------------------------------------------#

        p=True
        while p: # La boucle sur p correspond à l'initialisation du terrain de jeu.
            testenvgagne = 0

            pygame.display.set_caption("Soko BN")
            screen = pygame.display.set_mode((display[0],display[1]))

            #--------------------------------------------------------images / sons--------------------------------------------------------------------#

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

            ImgPrince = pygame.image.load("images/cookies/king50.png")
            ImgCookie = pygame.image.load("images/cookies/cookie.png")

            #------------------------------------------------------------------------------------------------------------------------------------------#

            #-------------------------------------------------------classes, variables et fonctions----------------------------------------------------#

            class Cookie:
                def __init__(self,name,position,ImgCookie):
                    self.name = name
                    self.position = position
                    self.image = ImgCookie

                def movecook(self):
                    screen.blit(self.image,self.position)

            class Prince:
                def __init__(self,name,position,ImgPrince):
                    self.name = name
                    self.position = position
                    self.image = ImgPrince

                def moveprince(self):
                    screen.blit(self.image,self.position)

            # On crée les objets de type Cookie.
            Cookie1 = Cookie("Cookie1",ImgCookie.get_rect(),ImgCookie)
            Cookie2 = Cookie("Cookie2",ImgCookie.get_rect(),ImgCookie)
            Cookie3 = Cookie("Cookie3",ImgCookie.get_rect(),ImgCookie)
            Cookie4 = Cookie("Cookie4",ImgCookie.get_rect(),ImgCookie)
            Cookie5 = Cookie("Cookie5",ImgCookie.get_rect(),ImgCookie)
            Cookie6 = Cookie("Cookie6",ImgCookie.get_rect(),ImgCookie)
            Cookie7 = Cookie("Cookie7",ImgCookie.get_rect(),ImgCookie)

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

            # Nous utlisons le tableau 'position' pour placer les cookies sur leur emplacement de départ :
            for i in range(position[0][0]):
                tabcookie[i].position = tabcookie[i].position.move(position[i + 2][0],position[i+2][1])
                tabcookie[i].movecook()

            # la varibale "reste" correspond au temps passé depuis le pygame.init().
            reste = round((pygame.time.get_ticks() * 0.001))

            testegagne = []
            for i in range(13):
                testegagne.append(0)

            # La fonction ci-dessous permet d'afficher un timer en fonction du temps écoulé durant un niveau.
            def affichetemps(temps):
                loop = 0
                for char in str(temps):
                    if loop == 0:
                        if char== "0":
                            screen.blit(img0, [300,0])
                        if char== "1":
                            screen.blit(img1, [300,0])
                        if char== "2":
                            screen.blit(img2, [300,0])
                        if char== "3":
                            screen.blit(img3, [300,0])
                        if char== "4":
                            screen.blit(img4, [300,0])
                        if char== "5":
                            screen.blit(img5, [300,0])
                        if char== "6":
                            screen.blit(img6, [300,0])
                        if char== "7":
                            screen.blit(img7, [300,0])
                        if char== "8":
                            screen.blit(img8, [300,0])
                        if char== "9":
                            screen.blit(img9, [300,0])
                    if loop == 1:
                        if char== "0":
                            screen.blit(img0, [350,0])
                        if char== "1":
                            screen.blit(img1, [350,0])
                        if char== "2":
                            screen.blit(img2, [350,0])
                        if char== "3":
                            screen.blit(img3, [350,0])
                        if char== "4":
                            screen.blit(img4, [350,0])
                        if char== "5":
                            screen.blit(img5, [350,0])
                        if char== "6":
                            screen.blit(img6, [350,0])
                        if char== "7":
                            screen.blit(img7, [350,0])
                        if char== "8":
                            screen.blit(img8, [350,0])
                        if char== "9":
                            screen.blit(img9, [350,0])
                    if loop == 2:
                        if char== "0":
                            screen.blit(img0, [400,0])
                        if char== "1":
                            screen.blit(img1, [400,0])
                        if char== "2":
                            screen.blit(img2, [400,0])
                        if char== "3":
                            screen.blit(img3, [400,0])
                        if char== "4":
                            screen.blit(img4, [400,0])
                        if char== "5":
                            screen.blit(img5, [400,0])
                        if char== "6":
                            screen.blit(img6, [400,0])
                        if char== "7":
                            screen.blit(img7, [400,0])
                        if char== "8":
                            screen.blit(img8, [400,0])
                        if char== "9":
                            screen.blit(img9, [400,0])
                    loop = loop + 1

            #------------------------------------------------------------------------------------------------------------------------------------------#

            pygame.display.update()
            jeu = True

#------------------------------------------------------------------------------------------------------------------------------------------------------#

# (2/2) -------------------------------------------------------- DEBUT DE L'IA ---------------------------------------------------------------------#

            while jeu:

                #------------ On fait une boucle pour s'occuper de chaque cookie un par un dans lequel on va créer un tableau contenant les coordonnées du -----------#
                #------------------------------------------------- chemin que le cookie doit empreinter pour atteindre son panier ---------------------------------------#

                for i in range(len(positionplacé)) : # On fait une boucle pour chaque cookie un par un.
                    colisionaveccookie = []
                    colisionaveccookie = [i for i in murnv] # On crée une COPIE de murnv.

                    #Dans colisionaveccookie on ajoute les positions des autres cookies car on ne peut pousser plusieurs cookies en même temps et donc il faut considérer les autres cookies comme des murs :
                    for f in range(len(positionplacé)) :
                        if f != i :
                            colisionaveccookie.append([tabcookie[f].position[0],tabcookie[f].position[1]])

                    #On appelle la fonction "a_etoile_cookie" du module 'algoACookie.py' qui retourne un tableau de coordonnées qui correspond au chemin que le cookie doit empreinter pour atteindre son panier :
                    tableaucookie = algoACookie.a_etoile_cookie(tabcookie[i].position,positionplacé[i],colisionaveccookie)


                    # ------------------------------------------------------------------------------------------------------------------------------------- #


                    #--------------- On s'occupe maintenant du déplacement du Prince. En fonction du chemin que le cookie doit empreinter, on déplace le Prince ----------------#
                    # ---------------------------------------------------------- vers la position où il doit pousser le cookie. ------------------------------------------------#

                    for k in tableaucookie: # On fait une boucle dans les coordonnées du chemin du cookie.
                        colisionaveccookie2 = []
                        colisionaveccookie2 = [i for i in murnv]  # On crée à nouveau une COPIE de murnv.

                        #Dans colisionaveccookie2 on ajoute les positions de tous les cookies car le Prince doit arriver à sa destination sans bouger de cookies et donc doit les considérer comme des murs :
                        for f in range(0,len(positionplacé)) :
                            colisionaveccookie2.append([tabcookie[f].position[0],tabcookie[f].position[1]])

                        positiondepartCookie = tabcookie[i].position #On crée une variable contenant la position du cookie.
                        positionsuivante = k #On crée une variable contenant la position suivante que doit suivre le cookie.

                        # En fonction de la position du cookie et de sa position suivante, nous en déduisons la position où doit se rendre le Prince afin de pousser le cookie dans la bonne direction :
                        tableau = [positionsuivante[0] - positiondepartCookie[0], positionsuivante[1] - positiondepartCookie[1]]
                        positionsupPrince = [positiondepartCookie[0] - tableau[0],positiondepartCookie[1] - tableau[1]] #Ce tableau correspond à la position où le Prince doit se rendre.

                        #On appelle la fonction "a_etoile_prince" du module 'algoAPrince.py' qui retourne un tableau de coordonnées qui correspond au chemin que le Prince doit empreinter pour atteindre sa destination.
                        CheminPrince = algoAPrince.a_etoile_prince(Prince.position, positionsupPrince,colisionaveccookie2)

                        # ------------------------------------------------------------------------------------------------------------------------------------- #

                        #-------------------------- Maintenant, on parcourt les coordonnées des positions que doit suivre le Prince pour atteindre le cookie -------------------#

                        for j in CheminPrince :
                            pygame.time.wait(300) # On fait une pause dans le programme pour que l'IA ai une vitesse raisonnable entre chaque mouvement comparé au joueur.

                            #On affiche le terrain :
                            screen.blit(background_image, [0, 0])

                            #On utilise la fonction "movecook()" de la classe cookie pour mettre à jour la position de tous les cookies :
                            for m in range(len(positionplacé)) :
                                tabcookie[m].movecook()

                            # On met à jour la position du Prince et le place sur le nouveau terrain :
                            Prince.position = j
                            Prince.moveprince()

                            #On regarde si il y a des cookies dans des paniers, si oui on change l'image du panier et du cookie pour le transformer en l'image du cookie dans le panier.
                            testecookienoir = 0
                            for bla in range(position[0][0]):
                                for ji in range(position[0][0]):
                                    if (tabcookie[bla].position == [positionplacé[ji][0], positionplacé[ji][1]]):
                                        tabcookie[bla].image = pygame.image.load("images/cookies/cookieNoir.png")
                                        testegagne[bla] = 1
                                        testecookienoir = 1
                                        pygame.display.update()
                                    elif(testecookienoir == 0):
                                        tabcookie[bla].image = pygame.image.load("images/cookies/cookie.png")
                                        testegagne[bla] = 0

                            temps = round((pygame.time.get_ticks() * 0.001) - reste)
                            affichetemps(temps) # On affiche le timer à l'aide de la fonction 'affichetemps'.
                            pygame.display.update()

                        # ------------------------------------------------------------------------------------------------------------------------------------- #

                        # ----------------- Une fois que le Prince a atteint le cookie, il faut pousser le cookie dans la bonne direction ----------------------#

                        pygame.time.wait(300)  # On fait une pause dans le programme pour que l'IA ai une vitesse raisonnable entre chaque mouvement comparé au joueur.

                        #On affiche le terrain :
                        screen.blit(background_image, [0, 0])

                        Prince.position = [Prince.position[0] + tableau[0],Prince.position[1] + tableau[1]] #Le Prince prend la position du Cookie
                        tabcookie[i].position = k #Le cookie quant à lui va à sa position suivante car le Prince pousse le cookie.
                        Prince.moveprince() # On met à jour la position du Prince.

                        #On utilise la fonction "movecook()" de la classe cookie pour mettre à jour la position de tous les cookies :
                        for m in range(len(positionplacé)) :
                            tabcookie[m].movecook()

                        temps = round((pygame.time.get_ticks() * 0.001) - reste)
                        affichetemps(temps) # On affiche le timer à l'aide de la fonction 'affichetemps'.
                        pygame.display.update()

                        # ------------------------------------------------------------------------------------------------------------------------------------- #

                        # On répète ce système jusqu'a ce que le cookie soit dans son panier.


                    if len(tableaucookie) == 0 : #Si tous les cookies sont placés, l'IA se termine et la fonction retourne le temps que l'IA a pris pour faire le niveau.
                        jeu = False
                        p = False
                        return(round((pygame.time.get_ticks() * 0.001) - reste))


#------------------------------------------------------------------------------------------------------------------------------------------------------#
