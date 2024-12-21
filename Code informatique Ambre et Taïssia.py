
import matplotlib.pyplot as plt
import math


#ouverture du fichier
fIN  = open('data_real.csv', 'r')
fOUT = open('separationFecal.csv', 'w')


# Saut de la première ligne
ligne = fIN.readline()

# Lecture des lignes
while ligne != '':
    ligne = fIN.readline()
    #  Si il recontre du vide il s'arrête
    if ligne == '':
        # arrêt de la boucle
        return
    # On sépare les éléments pour pouvoir travailler sur certains éléments précis
    valueList=line.split(';')
    
    # On définie le bloc 2 comme étant str, donc le bloque avec les types étudiés
    echantillon=str(valueList[2])
    #On récupère dans un premier temps que les fécals
    if echantillon=='fecal':
        ligne2=';'.join(valueList) #Les données sont collés
        fOUT.write(ligne2) #Elles sont écrites dans le document csv

fOUT.close()
fIN.close()
#On ferme les documents pour pourvoir reprendre à 0

#GRAPHIQUE avec droites
figure, axes = plt.subplots()

#On fait définie les axes
axes.set_title('Graphique représentant la concentration des bactérie selon leur jours de la semaine')
axes.set_xlabel('day')
axes.set_ylabel('nb bacterias')



graph = 'fecal'
#On range les souris qui les caractéristiques recherchée donc celle de 17 à 33 selon leur nom
for souris in range(17, 33):
    xVal = []
    yVal = []

    # on ouvre le fichier pour pouvoir exploiter les données
    fIN = open('separationFecal.csv', 'r')
    line = fIN.readline()
#Tant que les qu'il n'y à pas de vide il continue de lire
    while line != '':
        line = fIN.readline()
        if line == '':    #Sinon il arrête de lire
            break 
        # Séparations des données pour pouvoir les exploiter
        valueList = line.split(';')
        # Définition des lignes
        typeechantillon = valueList[2]
        sourisID    = int(valueList[4].replace('ABX', ''))
        traitement  = valueList[5]    
        jours        = int(valueList[7])
        bacterie   = math.log(float(valueList[8]))/math.log(10)


        "Filtration des lignes
        if sourisID == souris and typeechantillon == graph :
            xVal.append(jour) #Ranger dans les coordonnées abscisse
            yVal.append(bacterie)   #Ranger dans les coordonnées ordonnée     

    fIN.close()

    axes.plot(xVal, yVal)


#Formation du graphique fécal

figure.savefig('Graphique fécal.png', dpi=300)

#ouverture du fichier
fIN  = open('data_real.csv', 'r')
fOUT = open('separationIleal.csv', 'w')


# Saut de la première ligne
ligne = fIN.readline()

# Lecture des lignes
while ligne != '':
    ligne = fIN.readline()
    # Si il recontre un espace il arrête de lire
    if ligne == '':
        # exit the loop
        break
    #Séparation
    valueList=ligne.split(';')
    
    #Convertition des données en chaine de caractère
    echantillon=str(valueList[2])
    #Séparation des donnée Iléal
    if echantillon=='ileal':
        ligne3=';'.join(valueList)
        fOUT.write(ligne3)
        
#Fermeture des fichier ouvert
fIN.close()
fOUT.close()

#Deinition des listes pour les axes et ordonnées du graphique
xVal = []
yVal = []
xVal2= []
yVal2= []

# Ouverture du fichier 
fIN = open('separationIleal.csv', 'r')
ligne = fIN.readline()

count = 0
while ligne != '':
    ligne = fIN.readline()
    if ligne == '':
        break 
    valueList = ligne.split(';') #Séparation
    traitement = valueList[5] #Définition des zones d'interêt
    bacterie = math.log(float(valueList[8]))/math.log(10)
    #Si rencontre ABX Le traitement est égal à 1 et rentre dans la catégoris des liste une
    if traitement == 'ABX':
        traitement = 1
        xVal.append(traitement)
        yVal.append (bacterie)
        #Si ne rencontre pas ABX mis dans les secondes liste et traitement est égal à 2
    else:
        traitement = 2
        xVal2.append(traitement)
        yVal2.append (bacterie)
    count = count+1       
# traitement =1 ou =2 pour éviter de les avoir sur la même colonne

fIN.close()

# Formation du graphique

figure, axes = plt.subplots()

#Nommée les axes et le titre

axes.set_title('Concetration des bactérie dans le Ileal')
axes.set_xlabel('Traitement')
axes.set_ylabel('Contration des bactéries(bactérie log(10))')

#Mise en lien des axes les uns avec les autres
axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Graphique Ileal.png', dpi=300)

#Graphique Violon

figure, axes = plt.subplots()

axes.set_title('Concetration des bactérie dans le Ileal')
axes.set_ylabel('Contration des bactéries(bactérie log(10))')

#Définie axes violon
axes.violinplot([yVal, yVal2])

figure.savefig('Graphique Ileal.png', dpi=300)

#Ouverture dossier
fIN  = open('data_real.csv', 'r')
fOUT = open('separationCecal.csv', 'w')


# Lecture
line = fIN.readline()

while ligne != '':
    # Passe à la ligne suivante
    ligne = fIN.readline()
    # Si recontre vide
    if ligne == '':
        #Arrêt
        break
        
    valueList=line.split(';') #Séparation
    
    echantillon=str(valueList[2])
    #Récupération données spécifique
    if echantillon=='cecal':
        ligne3=';'.join(valueList)
        fOUT.write(linge3)
        

fIN.close()
fOUT.close()

#Création liste pour les axes
xVal = []
yVal = []
xVal2= []
yVal2= []

# Ouverture dossier
fIN = open('separationCecal.csv', 'r')
ligne = fIN.readline()

#Lecture du dossier
count = 0
while ligne != '':
    ligne = fIN.readline()
    if line == '':
        break 
    valueList = ligne.split(';') #Séparation
    traitement = str(valueList[5]) #Définition
    bacterie = math.log(float(valueList[8]))/math.log(10)
    #Si rencontre ABX Le traitement est égal à 1 et rentre dans la catégoris des liste une
    if traitement == 'ABX':
        traitement = 1
        xVal.append(traitement)
        yVal.append (bacterie)
        #Si ne rencontre pas ABX mis dans les secondes liste et traitement est égal à 2
    else:
        traitement = 2
        xVal2.append(traitement)
        yVal2.append (bacterie)
    count = count+1       

fIN.close()


# Graphique

figure, axes = plt.subplots()
#Définition des axes
axes.set_title('Concetration des bactérie dans le Cecal')
axes.set_xlabel('Traitement')
axes.set_ylabel('Contration des bactéries(bactérie log(10))')

axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Graphique Cecal.png', dpi=300)

#Graphique Violon

figure, axes = plt.subplots()

#Définis axes
axes.set_title('Concetration des bactérie dans le Cecal')
axes.set_ylabel('Y values')
#Défini acex violon
axes.violinplot([yVal, yVal2])

figure.savefig('Graphique Cecal.png', dpi=300)
