'''
Created on Feb 24, 2017

@author: Daniel McMahon
'''

import argparse
import urllib.request

def turnOn(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOn feature. Turns lights on (or 'true') regardless of their current state'''
    
    #use a-1 and b-1: stumbled upon fix when testing against sample input answer provided of 400410
    #initially without the -1 answer was off by just under 1,500....
    #why this works? I believe its due to range function...
    #as its going from a to c-1 and b to d-1 in practice I have decremented the starting value
    #so the right number of lights are affected
    #initially tested a,c+1 and b,d+1 but index fell out of range..
    #concern here is if on other side of spectrum 0,0 same issue will apply
    
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
    #this feels a little cheaty.... returns after first line is iterated in loop!
    for line in file.split('\n'):
        x = line
        L = int(x)
        return L
    
def applyChanges(file,L):
    '''Function that parses input from file and carries out various functions according to strings starting values'''

    for line in file.split('\n'):
        if line.startswith("turn on"):
            ab = line.split(" ")[2]
            cd = line.split(" ")[4]
                
            a = int(ab.split(",")[0])
            b = int(ab.split(",")[1])
                
            c = int(cd.split(",")[0])
            d = int(cd.split(",")[1])

            x=turnOn(a,b,c,d,L)
            L=x
                
                
        elif line.startswith("switch"):
            ab = line.split(" ")[1]
            cd = line.split(" ")[3]
            
            a = int(ab.split(",")[0])
            b = int(ab.split(",")[1])
                
            c = int(cd.split(",")[0])
            d = int(cd.split(",")[1])
                
            y=switch(a,b,c,d,L)
            L=y
                
        elif line.startswith("turn off"):
                
            ab = line.split(" ")[2]
            cd = line.split(" ")[4]
                
            a = int(ab.split(",")[0])
            b = int(ab.split(",")[1])
                
            c = int(cd.split(",")[0])
            d = int(cd.split(",")[1])
                
            z=turnOff(a,b,c,d,L)
            L=z
    
    return L

def plotMap(L):
    '''function to create the starting LEDgrid'''
    plottedMap = []
    for i in range(0,L-1):
        plottedMap.append([False] * (L-1))
        
    return plottedMap
    
def main(): 
    '''main function - reads console input and passes it through various functions and outputs total lights left on'''
    
    #parsing the user input - expecting a link from the users input...
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    link = args.input #replace link with filename to read standard files
    
    #reading the link
    req=urllib.request.urlopen(link)
    buffer=req.read().decode('utf-8')
    
    #setting value L from file
    L = fileReadL(buffer)#replace buffer with filename to read standard files
    
    #setting up grid based on L value
    LEDgrid = plotMap(L)
    
    #applying changes with turnOn,Switch,turnOff functions called in applyChanges function
    changes=applyChanges(buffer,LEDgrid)#replace buffer with filename to read standard files
    LEDgrid=changes
    #note: functions called within applyChanges return the updated LEDgrid
    #the below prints out total number of lights on by iterating through values of a list inside a list
    counter = 0
    
    for line in LEDgrid:
        for value in line:
            if value == True:
                counter += 1
    
    print("Total number of lights on:", counter)
    
if __name__ == '__main__':
    main()