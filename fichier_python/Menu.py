import pygame

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------Ce module Python contient une fonction qui affiche à l'utilisateur le menu du jeu sur lequel il peut choisir son niveau, regarder les règles du jeu ou encore quitter le jeu---------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#Début de la fonction menu
def menu():
    showtouche = 0
    nvchoisie = 0

    #Initialisation du menu / Chargement de toutes les images du menu
    pygame.init()

    screen = pygame.display.set_mode((1000,602))
    pygame.display.set_caption("Soko BN menu")

    background_image = pygame.image.load("images/menu/fontmenufin.png")
    background_image1 = pygame.image.load("images/menu/fondmenu602.png")
    titre = pygame.image.load("images/menu/Titre.png")
    niveausanshover = pygame.image.load("images/menu/NiveauSansHover.png")
    testhoverniveau = 0
    niveauavechover = pygame.image.load("images/menu/NiveauAvecHover.png")
    optionsanshover = pygame.image.load("images/menu/OptionSansHover.png")
    testhoveroption = 0
    optionavechover = pygame.image.load("images/menu/OptionAvecHover.png")
    quitteravechover = pygame.image.load("images/menu/QuitterAvecHover.png")
    testquitterhover = 0
    quittersanshover = pygame.image.load("images/menu/QuitterSansHover.png")

    facilesanshover = pygame.image.load("images/menu/FacileSansHover.png")
    facileavechover = pygame.image.load("images/menu/FacileAvecHover.png")
    normalsanshover = pygame.image.load("images/menu/NormalSansHover.png")
    normalavechover = pygame.image.load("images/menu/NormalAvecHover.png")
    difficilesanshover = pygame.image.load("images/menu/DifficileSansHover.png")
    difficilesavechover = pygame.image.load("images/menu/DifficileAvecHover.png")
    flècheretour = pygame.image.load("images/menu/flècheSansHover.png")
    ropt = pygame.image.load("images/menu/ropt.png")
    esc = pygame.image.load("images/menu/esc.png")
    fleche = pygame.image.load("images/menu/touche.png")
    regles = pygame.image.load("images/menu/Regles.png")

    menuniveau = 0
    choixniveau = 0
    pygame.display.update()
    menu = True

    #Début de l'interaction avec le menu
    while menu:
        # Attente d'appui sur une touche
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    pygame.quit()
                # Regarde la position du déplacement de la souris afin d'afficher un hover sur les zones cliquables du menu
                if event.type == pygame.MOUSEMOTION:
                    posSouris = pygame.mouse.get_pos()
                    if 325 < posSouris[0] < 675 and 215 < posSouris[1] < 280:
                        testhoverniveau = 1
                    else :
                        testhoverniveau = 0
                    if 325 < posSouris[0] < 675 and 315 < posSouris[1] < 380:
                        testhoveroption = 1
                    else:
                        testhoveroption = 0
                    if 325 < posSouris[0] < 675 and 415 < posSouris[1] < 480:
                        testquitterhover = 1
                    else:
                        testquitterhover = 0
                #Regarde la position d'appui de la souris pour effectuer différentes actions
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posSouris = pygame.mouse.get_pos()
                    #Action fermer le menu
                    if 325 < posSouris[0] < 675 and 415 < posSouris[1] < 480 and menuniveau == 0:
                        jeu = False
                        pygame.quit()
                    #Action aller dans le sous menu "choix de la difficulté"
                    elif 325 < posSouris[0] < 675 and 215 < posSouris[1] < 280 and menuniveau == 0:
                        menuniveau = 1
                    elif 60 < posSouris[0] < 250 and 500 < posSouris[1] < 600 and (menuniveau == 1 or menuniveau == 2):
                        menuniveau = 0
                    #Action choix de la difficulté
                    elif 325 < posSouris[0] < 675 and 215 < posSouris[1] < 280 and menuniveau == 1:
                        choixniveau = 1
                    elif 25 < posSouris[0] < 675 and 315 < posSouris[1] < 380 and menuniveau == 1:
                        choixniveau = 3
                    elif 325 < posSouris[0] < 675 and 415 < posSouris[1] < 480 and menuniveau == 1:
                        choixniveau = 5
                    #Action option
                    elif 325 < posSouris[0] < 675 and 315 < posSouris[1] < 380 and menuniveau == 0:
                        menuniveau = 2

        #Rafraîchissement de la page avec les différentes actions effectuées précédemment
        screen.blit(background_image, [0, 0])
        screen.blit(titre, [190, 20])
        if testhoverniveau == 0 and menuniveau == 0:
            screen.blit(niveausanshover, [325,200])
        if testhoverniveau == 1 and menuniveau == 0:
            screen.blit(niveauavechover, [325,200])
        if testhoveroption == 0 and menuniveau == 0:
            screen.blit(optionsanshover, [325,300])
        if testhoveroption == 1 and menuniveau == 0:
            screen.blit(optionavechover, [325,300])
        if testquitterhover == 0 and menuniveau == 0:
            screen.blit(quittersanshover, [325,400])
        if testquitterhover == 1 and menuniveau == 0:
            screen.blit(quitteravechover, [325,400])

        if testhoverniveau == 0 and menuniveau == 1:
            screen.blit(facilesanshover, [325,200])
        if testhoverniveau == 1 and menuniveau == 1:
            screen.blit(facileavechover, [325,200])
        if testhoveroption == 0 and menuniveau == 1:
            screen.blit(normalsanshover, [325,300])
        if testhoveroption == 1 and menuniveau == 1:
            screen.blit(normalavechover, [325,300])
        if testquitterhover == 0 and menuniveau == 1:
            screen.blit(difficilesanshover, [325,400])
        if testquitterhover == 1 and menuniveau == 1:
            screen.blit(difficilesavechover, [325,400])
        if menuniveau == 2 :
            screen.blit(background_image1, [0, 0])
            screen.blit(ropt, [840,100])
            screen.blit(fleche, [580,300])
            screen.blit(esc, [540,97])
            screen.blit(regles, [15,50])
        if menuniveau == 1 or menuniveau == 2 :
            screen.blit(flècheretour, [50,420])
        if choixniveau != 0:
            return(choixniveau)
            menu = False
            pygame.quit()

        pygame.display.update()
