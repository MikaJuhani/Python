#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
import copy

print "Ohjelman avulla voidaan ratkaista kolmen yhtälön avulla kolme eri tuntematonta tekijää: x, y ja z"
print "Anna ensimmäisen rivin kolmen muuttujan arvot ja tulos eli jos 2x + 8y -7z = 4, niin aina kehtotteen"
print "jälkeen: 2.0 / enter, 8.0 / enter, -7.0 / enter ja 4.0/ enter. Annat siis luvut reaalilukuina.\n"

aX = raw_input("Ensimmäisen rivin x: ")
aY = raw_input("Ensimmäisen rivin y: ")
aZ = raw_input("Ensimmäisen rivin z: ")
aT = raw_input("Ensimmäisen rivin tulos: ")
bX = raw_input("Toisen rivin x: ")
bY = raw_input("Toisen rivin y: ")
bZ = raw_input("Toisen rivin z: ")
bT = raw_input("Toisen rivin tulos: ")
cX = raw_input("Kolmannen rivin x: ")
cY = raw_input("Kolmannen rivin y: ")
cZ = raw_input("Kolmannen rivin z: ")
cT = raw_input("Kolmannen rivin tulos: ")

lineA = [aX,aY,aZ,aT]
lineB = [bX,bY,bZ,bT]
lineC = [cX,cY,cZ,cT]

print "\n"
print "Kirjoitit seuraavat yhtälöt:\n"
print lineA[0] + "x " + lineA[1] + "y " + lineA[2] + "z = " + lineA[3]
print lineB[0] + "x " + lineB[1] + "y " + lineB[2] + "z = " + lineB[3]
print lineC[0] + "x " + lineC[1] + "y " + lineC[2] + "z = " + lineC[3]

#Tästä saadaan kertoja yläriviä varten B-riviltä
lineB_zVal = float(lineB[2]) * -1.0
multiplier_lineB_NewzVal = copy.deepcopy(lineB_zVal)
# * * * *

lineA_xVal = float(lineA[0]) * multiplier_lineB_NewzVal
#A0
lineA_NewxVal = copy.deepcopy(lineA_xVal)

lineA_yVal = float(lineA[1]) * multiplier_lineB_NewzVal
#A1
lineA_NewyVal = copy.deepcopy(lineA_yVal)

lineA_zVal = float(lineA[2]) * multiplier_lineB_NewzVal
#A2
lineA_NewzVal = copy.deepcopy(lineA_zVal)

lineA_tVal = float(lineA[3]) * multiplier_lineB_NewzVal
#A3
lineA_NewtVal = copy.deepcopy(lineA_tVal)

#Lasketaan ylin ja toinen rivi yhteen, jotta saadaan uusi B(2)
countNewBx = lineA_NewxVal + float(lineB[0])
#New B0
newLineBx = copy.deepcopy(countNewBx)

countNewBy = lineA_NewyVal + float(lineB[1])
#New B1
newLineBy = copy.deepcopy(countNewBy)

countNewBz = lineA_NewzVal + float(lineB[2])
#New B2
newLineBz = copy.deepcopy(countNewBz)

countNewBt = lineA_NewtVal + float(lineB[3])
#New B3
newLineBt = copy.deepcopy(countNewBt)

#Tässä on uusi B2-rivi
#print newLineBx
#print newLineBy
#print newLineBz
#print newLineBt

#Tästä saadaan kertoja yläriviä varten C-riviltä
lineC_zVal = float(lineC[2]) * -1.0
multiplier_lineC_NewzVal = copy.deepcopy(lineC_zVal)
# * * * *

lineA_xValbyC = float(lineA[0]) * multiplier_lineC_NewzVal
#A0byB
lineA_NewxValbyC = copy.deepcopy(lineA_xValbyC)

lineA_yValbyC = float(lineA[1]) * multiplier_lineC_NewzVal
#A1byB
lineA_NewyValbyC = copy.deepcopy(lineA_yValbyC)

lineA_zValbyC = float(lineA[2]) * multiplier_lineC_NewzVal
#A2byB
lineA_NewzValbyC = copy.deepcopy(lineA_zValbyC)

lineA_tValbyC = float(lineA[3]) * multiplier_lineC_NewzVal
#A3byB
lineA_NewtValbyC = copy.deepcopy(lineA_tValbyC)

#Tässä on uusi A2-rivi
#print " \n"
#print lineA_NewxValbyC
#print lineA_NewyValbyC
#print lineA_NewzValbyC
#print lineA_NewtValbyC

#Lasketaan ylin ja alin rivi yhteen, jotta saadaan uusi C(2)
countNewCx = lineA_NewxValbyC + float(lineC[0])
#New C0
newLineCx = copy.deepcopy(countNewCx)

countNewCy = lineA_NewyValbyC + float(lineC[1])
#New C0
newLineCy = copy.deepcopy(countNewCy)

countNewCz = lineA_NewzValbyC + float(lineC[2])
#New C0
newLineCz = copy.deepcopy(countNewCz)

countNewCt = lineA_NewtValbyC + float(lineC[3])
#New C0
newLineCt = copy.deepcopy(countNewCt)

#Tässä on uusi C2-rivi
#print "\n"
#print newLineCx
#print newLineCy
#print newLineCz
#print newLineCt

#Tästä saadaan kertoja y:n eliminointia varten
forEliminatingYseq = newLineBy / newLineCy
forEliminatingY = copy.deepcopy(forEliminatingYseq)
changedForEliminatingY = forEliminatingY * -1.0
multiplier_forEliminatingY = copy.deepcopy(changedForEliminatingY)

#print "\n"
#print multiplier_forEliminatingY

#C2x calculated to using for eliminating y
forCalculatedC2x = newLineCx * multiplier_forEliminatingY
calculatedC2x = copy.deepcopy(forCalculatedC2x)

#C2y calculated to use for eliminating y
forCalculatedC2y = newLineCy * multiplier_forEliminatingY
calculatedC2y = copy.deepcopy(forCalculatedC2y)

#C2t calculated to using for eliminating y
forCalculatedC2t = newLineCt * multiplier_forEliminatingY
calculatedC2t = copy.deepcopy(forCalculatedC2t)

#Calculated C2 without z
#print "\n"
#print calculatedC2x
#print calculatedC2y
#print calculatedC2t

#Solving x
forC3x = newLineBx + calculatedC2x
c3x = copy.deepcopy(forC3x)

forC3y = newLineBy + calculatedC2y
c3y = copy.deepcopy(forC3y)

forC3t = newLineBt + calculatedC2t
c3t = copy.deepcopy(forC3t)

#print "\n"
#print c3x
#print c3y
#print c3t

forX = c3t / c3x
x = copy.deepcopy(forX)
#print "\n"
#print x

#Solving y
forYbyX = newLineBx * x
changerY = copy.deepcopy(forYbyX)
forYbyXchanged = changerY * -1
yByX = copy.deepcopy(forYbyXchanged)

#It have to be added to t
forYbyAddingT = yByX + newLineBt
forYbyDividing = copy.deepcopy(forYbyAddingT)
forY = forYbyDividing / newLineBy
y = copy.deepcopy(forY)

#print "\n"
#print y

#Solving z
xFactorForCopy = x * float(lineA[0])
xFactor = copy.deepcopy(xFactorForCopy)

yFactorForCopy = y * float(lineA[1])
yFactor = copy.deepcopy(yFactorForCopy)

forXYFactorsTogether = xFactor + yFactor
xy = copy.deepcopy(forXYFactorsTogether)

forChangingXY = xy * -1
changedXY = copy.deepcopy(forChangingXY)

forZ = changedXY + float(lineA[3])
z = copy.deepcopy(forZ)

#print "\n"
#print z

print "\n"
print "X:"
print x

print "\n"
print "Y:"
print y

print "\n"
print "Z:"
print z