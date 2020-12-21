# Project 1
# Name: Tarini Srikanth
# Instructor: Turner
# Section: CPE101-05
import math
def poundsToKG(pounds):
    #multiplying the user input by the given constant
    massSkater = pounds*0.453592
    return massSkater
def getMassObject(object):
    #checking if the user input is one of the 4 possible letters, else returning 0
    if(object=='t'):
        return 0.1
    if(object=='p'):
        return 1.0
    if(object=='r'):
        return 3.0
    if(object=='g'):
        return 5.3
    if(object=='l'):
        return 9.07
    else:
        return 0.0
def getVelocityObject(distance):
    #getting the user distance, multiplying it by the accerlation, 9.8, dividing by 2 and taking the square root. 
    insideValue =(9.8*distance)/2
    velocityObject = math.sqrt(insideValue)
    return velocityObject
def getVelocitySkater(massSkater, massObject, velObject):
    #getting the 3 variables and multiplying the object by the velocity, and dividing by the mass of the skater. 
    velocitySkater = (massObject*velObject)/massSkater
    return velocitySkater


