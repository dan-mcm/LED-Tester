'''
Created on Feb 24, 2017

@author: Daniel McMahon
'''

import argparse

def turnOn(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOn feature. Turns lights on (or 'true') regardless of their current state'''
    for column in range(a,c):
        for row in range (b,d):
            LEDgrid[column][row] = True
        
    return LEDgrid

def switch(a,b,c,d,LEDgrid):
    '''Function intended to switch on or off lights depending on their current state. If light on - switch off and vice versa.'''   
    for column in range(a,c):
        for row in range (b,d):
            
            if LEDgrid[column][row] == True:
                LEDgrid[column][row] = False
            else:
                LEDgrid[column][row] = True
                
    return LEDgrid

def turnOff(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOff feature.  Turns lights off (or 'false') regardless of their current state'''
    for column in range(a,c):
        for row in range (b,d):
            LEDgrid[column][row] = False
        
    return LEDgrid;

def fileReadL(file):
    '''Function that reads the value of L from a text file - this will determine size of LEDgrid'''
    with open(file) as file:
        x = file.readline()
        L = int(x)
        return L
    
def applyChanges(file,L):
    '''Function that parses input from file and carries out various functions according to strings starting values'''
    
    with open(file) as file:
        for line in file:
            if line.startswith("turn on"):
                ac = line.split(" ")[2]
                bd = line.split(" ")[4]
                
                a = int(ac.split(",")[0])
                c = int(ac.split(",")[1])
                
                b = int(bd.split(",")[0])
                d = int(bd.split(",")[1])
                
                turnOn(a,b,c,d,L)
                
                
            elif line.startswith("switch"):
                ac = line.split(" ")[1]
                bd = line.split(" ")[3]
            
                a = int(ac.split(",")[0])
                c = int(ac.split(",")[1])
                
                b = int(bd.split(",")[0])
                d = int(bd.split(",")[1])
                
                switch(a,b,c,d,L)
                
                
            elif line.startswith("turn off"):
                
                ac = line.split(" ")[2]
                bd = line.split(" ")[4]
                
                a = int(ac.split(",")[0])
                c = int(ac.split(",")[1])
                
                b = int(bd.split(",")[0])
                d = int(bd.split(",")[1])
                
                turnOff(a,b,c,d,L)
    
def plotMap(L):
    '''function to create the starting LEDgrid'''
    plottedMap = []
    for i in range(0,L-1):
        plottedMap.append([False] * (L-1))
        
    return plottedMap
    
def main(): 
    '''main function - reads console input and passes it through various functions and outputs total lights left on'''
    
    #parsing the user file...
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    
    #setting value L from file
    L = fileReadL(filename)
    
    #setting up grid based on L value
    LEDgrid = plotMap(L)
    
    #applying changes with turnOn,Switch,turnOff functions called in applyChanges function
    applyChanges(filename,LEDgrid)
    
    #note: functions called within applyChanges return the updated LEDgrid
    #the below prints out total number of lights on by iterating through values of a list inside a list
    counter = 0
    for line in LEDgrid:
        for value in line:
            if value == True:
                counter += 1
    
    print("Total number of lights on =", counter)
    
    
if __name__ == '__main__':
    main()