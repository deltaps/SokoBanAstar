# ---------------Niveau 1----------------#

# fonction qui retourne un tableau de coordonnées correspondant aux murs du niveau #
def murnv1():
    i=0
    tabl=[[300,100],[300,150],[250,100],[50,300],[100,300],[150,300],[150,250],[300,50]]
    while i<450:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([450,i])
        tabl.append([i,450])
        i = i+50
    return(tabl)

# fonction qui retourne un tableau de coordonnées correspondant, dans l'ordre, au nombres de cookies, à la position du personnages puis aux coordonnées des cookies au départ #
def positionnv1():
    return([[4],[50,50],[400,200],[250,350],[200,100],[100,100]])

# fonction qui retourne la taille du niveau en pixel#
def displaynv1():
    return([500,500])

# fonction qui retourne un tableau de coordonnées correspondant aux paniers du niveau #
def positionplacénv1():
    return([[400,50],[50,400],[350,300],[250,250]])

# ---------------Niveau 2----------------#

def murnv2():
    i=0
    tabl=[[50,250],[100,250],[150,250],[200,250],[250,250],[300,250],[300,200],[300,300],[300,150],[150,300]]
    while i<450:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([450,i])
        tabl.append([i,450])
        i = i+50
    return(tabl)

def positionnv2():
    return([[4],[50,50],[100,150],[150,150],[200,150],[250,150]])
def displaynv2():
    return([500,500])
def positionplacénv2():
    return([[400,50],[400,400],[50,300],[250,300]])

# ---------------Niveau 3----------------#

def murnv3():
    i=0
    tabl=[[250,50],[50,150],[250,150],[300,150],[350,150],[400,150],[250,200],[400,200],[250,250],[150,300],[200,300],[250,300],[300,300],[350,300],[400,300],[450,300],[500,300],[350,350],[50,450],[100,450],[350,450],[300,500],[350,500],[400,500],[500,500]]
    while i<550:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([550,i])
        tabl.append([i,550])
        i = i+50
    return(tabl)
def positionnv3():
    return([[4],[50,50],[100,100],[150,250],[150,350],[250,400]])
def displaynv3():
    return([600,600])
def positionplacénv3():
    return([[300,50],[300,250],[50,500],[450,500]])

# ---------------Niveau 4----------------#

def murnv4():
    i=0
    tabl=[[50,150],[50,400],[50,450],[100,150],[150,150],[150,200],[150,250],[200,250],[200,350],[250,250],[250,300],[250,350],[250,400],[300,500],[350,150],[350,200],[350,500],[400,50],[400,100],[400,150],[400,200],[400,500],[450,50],[450,350],[450,400],[450,500],[500,50],[500,100],[500,350],[500,400],[500,450],[500,500]]
    while i<550:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([550,i])
        tabl.append([i,550])
        i = i+50
    return(tabl)
def positionnv4():
    return([[5],[50,50],[350,250],[350,300],[200,450],[250,100],[200,100]])
def displaynv4():
    return([600,600])
def positionplacénv4():
    return([[450,100],[450,450],[50,500],[200,300],[100,200]])

# ---------------Niveau 5----------------#

def murnv5():
    i=0
    tabl=[[250,50],[450,100],[500,100],[300,150],[350,150],[450,150],[100,200],[150,200],[300,200],[350,200],[450,200],[150,250],[300,250],[50,300],[250,300],[300,300],[50,350],[100,350],[300,350],[350,350],[450,350],[450,400],[50,450],[150,450],[200,450],[350,450],[450,450],[200,500],[300,500],[350,500],[450,500],[500,500]]
    while i<600:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([600,i])
        tabl.append([i,600])
        i = i+50
    return(tabl)
def positionnv5():
    return([[4],[50,50],[200,100],[200,150],[100,100],[450,300]])
def displaynv5():
    return([650,650])
def positionplacénv5():
    return([[350,50],[100,300],[150,550],[350,550]])

# ---------------Niveau 6----------------#

def murnv6():
    i=0
    tabl=[[250,50],[300,50],[350,50],[400,50],[450,50],[500,50],[550,50],[300,100],[350,100],[550,100],[550,200],[50,250],[100,250],[250,250],[300,250],[350,250],[400,250],[550,250],[50,300],[200,300],[250,300],[400,300],[500,300],[550,300],[50,350],[550,350],[50,400],[150,400],[200,400],[200,450],[250,450],[300,450],[400,450],[450,450],[300,500],[350,500],[400,500],[150,550],[200,550],[250,550],[300,550],[350,550]]
    while i<600:
        tabl.append([0,i])
        tabl.append([i,0])
        tabl.append([600,i])
        tabl.append([i,600])
        i = i+50
    return(tabl)

def positionnv6():
    return([[7],[50,50],[450,150],[450,400],[100,400],[200,150],[150,150],[150,100],[100,100]])
def displaynv6():
    return([650,650])
def positionplacénv6():
    return([[400,100],[450,500],[250,500],[500,500],[350,300],[300,300],[50,550]])
