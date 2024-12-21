
import matplotlib.pyplot as plt
import math


#ouverture du fichier
fIN  = open('data_real.csv', 'r')
fOUT = open('separationFecal.csv', 'w')


# Saut de la première ligne
line = fIN.readline()

# Lecture des lignes
while line != '':
    line = fIN.readline()
    # iSi il recontre du vide il s'arrête
    if line == '':
        # arrêt de la boucle
        break
    
    valueList=line.split(';')
    

    sample=str(valueList[2])
    
    if sample=='fecal':
        line2=';'.join(valueList)
        fOUT.write(line2)

fOUT.close()
fIN.close()


figure, axes = plt.subplots()

axes.set_title('Mouse (fecal)')
axes.set_xlabel('day')
axes.set_ylabel('nb bacterias')



graph = 'fecal'

for mouse in range(17, 33):
    xVal = []
    yVal = []

    # fill data from file
    fIN = open('separationFecal.csv', 'r')
    line = fIN.readline()

    while line != '':
        line = fIN.readline()
        if line == '':
            break 
        # split line
        valueList = line.split(';')
        # retrieve data
        sampleType = valueList[2]
        mouseID    = int(valueList[4].replace('ABX', ''))
        treatment  = valueList[5]    
        day        = int(valueList[7])
        bacteria   = math.log(float(valueList[8]))/math.log(10)


        # filter lines
        if mouseID == mouse and sampleType == graph :
            xVal.append(day)
            yVal.append(bacteria)        

    fIN.close()

    axes.plot(xVal, yVal)




figure.savefig('result2.png', dpi=300)

#open files (input + output)
fIN  = open('data_real.csv', 'r')
fOUT = open('separationIleal.csv', 'w')


# skip first line
line = fIN.readline()

# browse all other lines
while line != '':
    # get next line
    line = fIN.readline()
    # if we encountered the last line
    if line == '':
        # exit the loop
        break
    #split
    valueList=line.split(';')
    
    #convert one column into a variable
    sample=str(valueList[2])
    #keep only mice for cecal
    if sample=='ileal':
        line3=';'.join(valueList)
        fOUT.write(line3)
        

fIN.close()
fOUT.close()


xVal = []
yVal = []
xVal2= []
yVal2= []

# manual filling
#for i in range(101):
#    xVal.append(i)
#    yVal.append( math.cos(math.pi*i/50) )
#    yVal2.append( math.sin(math.pi*i/50) )

# fill data from file
fIN = open('separationIleal.csv', 'r')
line = fIN.readline()

count = 0
while line != '':
    line = fIN.readline()
    if line == '':
        break 
    valueList = line.split(';')
    traitement = valueList[5]
    bacterie = math.log(float(valueList[8]))/math.log(10)
    if traitement == 'ABX':
        traitement = 1
        xVal.append(traitement)
        yVal.append (bacterie)
    else:
        traitement = 2
        xVal2.append(traitement)
        yVal2.append (bacterie)
    count = count+1       

fIN.close()

# ---------------------------------------------------
# LINE PLOT
# ---------------------------------------------------
figure, axes = plt.subplots()

axes.set_title('Concetration des bactérie dans le Ileal')
axes.set_xlabel('X values')
axes.set_ylabel('Y values')

axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Graphique Ileal.png', dpi=300)

# ---------------------------------------------------
#VIOLIN PLOT
# ---------------------------------------------------

figure, axes = plt.subplots()

axes.set_title('Concetration des bactérie dans le Ileal')
axes.set_ylabel('Y values')

axes.violinplot([yVal, yVal2])

figure.savefig('Graphique Ileal.png', dpi=300)

#open files (input + output)
fIN  = open('data_real.csv', 'r')
fOUT = open('separationCecal.csv', 'w')


# skip first line
line = fIN.readline()

# browse all other lines
while line != '':
    # get next line
    line = fIN.readline()
    # if we encountered the last line
    if line == '':
        # exit the loop
        break
    #split
    valueList=line.split(';')
    
    #convert one column into a variable
    sample=str(valueList[2])
    #keep only mice for cecal
    if sample=='cecal':
        line3=';'.join(valueList)
        fOUT.write(line3)
        

fIN.close()
fOUT.close()

xVal = []
yVal = []
xVal2= []
yVal2= []

# manual filling
#for i in range(101):
#    xVal.append(i)
#    yVal.append( math.cos(math.pi*i/50) )
#    yVal2.append( math.sin(math.pi*i/50) )

# fill data from file
fIN = open('separationCecal.csv', 'r')
line = fIN.readline()

count = 0
while line != '':
    line = fIN.readline()
    if line == '':
        break 
    valueList = line.split(';')
    traitement = str(valueList[5])
    bacterie = math.log(float(valueList[8]))/math.log(10)
    if traitement == 'ABX':
        traitement = 1
        xVal.append(traitement)
        yVal.append (bacterie)
    else:
        traitement = 2
        xVal2.append(traitement)
        yVal2.append (bacterie)
    count = count+1       

fIN.close()

# ---------------------------------------------------
# LINE PLOT
# ---------------------------------------------------
figure, axes = plt.subplots()

axes.set_title('Concetration des bactérie dans le Cecal')
axes.set_xlabel('X values')
axes.set_ylabel('Y values')

axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Graphique Cecal.png', dpi=300)

# ---------------------------------------------------
#VIOLIN PLOT
# ---------------------------------------------------

figure, axes = plt.subplots()

axes.set_title('Concetration des bactérie dans le Cecal')
axes.set_ylabel('Y values')

axes.violinplot([yVal, yVal2])

figure.savefig('Graphique Cecal.png', dpi=300)
