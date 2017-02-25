'''
Created on Feb 24, 2017

@author: danie
'''
# a = first set of co-ords
# b = second set of co-ords
def turnOn(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOn feature'''
    output = []
    #x refers to column
    for x in range(0,3):
        #y refers to row
        for y in range (1,5):
            LEDgrid[x][y] = True
        
    return LEDgrid;


def switch(a,b,c,d,LEDgrid):
    '''Function intended to switch on or off lights'''
    output = []
    for elem in range (a,b+1):
        #if elem is True (on) make False (off) or vice versa
        if elem == True:
            elem == False;
            output += elem
        else:
            elem == True;
            output += elem
    return output


def turnOff(a,b,c,d,LEDgrid):
    '''Function intended to handle turnOff feature'''
    output = []
    #for elem in range (a,b+1):
        #if element is in range, make it False i.e. Turn off light
        #ignoring if light is already off
        #elem = False;
        #output += elem
    return output


def fileReadL(file):
    with open(file) as file:
        x = file.readline()
        L = int(x)
        L = 10
        return L
    
def fileRead(file,L):
    '''Function intended to read key data from file'''
    '''initial testing without command line input'''
    with open(file) as file:
        for line in file:
            if line.startswith("turn on"):
                ac = line.split(" ")[2]
                bd = line.split(" ")[4]
                
                #a = int(ac.split(",")[0])
                #c = int(ac.split(",")[1])
                
                #b = int(bd.split(",")[0])
                #d = int(bd.split(",")[1])
                
                a,b,c,d = 5,6,7,8
                
                turnOn(a,b,c,d,L)
                
                
            elif line.startswith("switch"):
                ac = line.split(" ")[1]
                bd = line.split(" ")[3]
            
                a = int(ac.split(",")[0])
                c = int(ac.split(",")[1])
                
                b = int(bd.split(",")[0])
                d = int(bd.split(",")[1])
                #switch(a,b,c,d)
                
                
            elif line.startswith("turn off"):
                
                ac = line.split(" ")[2]
                bd = line.split(" ")[4]
                
                a = int(ac.split(",")[0])
                c = int(ac.split(",")[1])
                
                b = int(bd.split(",")[0])
                d = int(bd.split(",")[1])
                #turnOff(a,b,c,d)


def plotMap(L):
    '''function to plot the map for testing purposes'''
    ## encountered functional error by using variable...
    ## line = [False] * (L-1)
    plottedMap = []
    for i in range(0,L-1):
        plottedMap.append([False] * (L-1))
        
    return plottedMap
    
def main():
    '''main function'''
    L = fileReadL("input_assign3.txt")
    LEDgrid = plotMap(L)
    
    for item in LEDgrid:
        print( item )
    print()
    
    fileRead("input_assign3.txt",LEDgrid)
    
    for item in LEDgrid:
        print(item)
    
if __name__ == '__main__':
    main()