'''
Created on Feb 24, 2017

@author: danie
'''
# a = first set of co-ords
# b = second set of co-ords
def turnOn(a,b):
    '''Function intended to handle turnOn feature'''
    output = []
    for elem in range (a,b+1):
        #if element is in range, make it True i.e. Turn on light
        #ignroing if light is already on
        elem == True;
        output += elem
    return output;


def switch(a,b):
    '''Function intended to switch on lights off'''
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


def turnOff(a,b):
    '''Function intended to handle turnOff feature'''
    output = []
    for elem in range (a,b+1):
        #if element is in range, make it False i.e. Turn off light
        #ignoring if light is already off
        elem = False;
        output += elem
    return output


def fileRead(file):
    '''Function intended to read key data from file'''
    '''initial testing without command line input'''
    with open(file) as file:
        x = file.readline()
        #L = int(x)
        L = 10
        return L
        for line in file:
            
            if line.startswith("turn on"):
                #a = (w,x); #where w and x are the first two int values on the line
                #b = (y,z); #where y and z are the second two in values on the line
                #turnOn(a,b)
                print("Turn on detected")
                
            elif line.startswith("switch"):
                #a = (w,x); #where w and x are the first two int values on the line
                #b = (y,z); #where y and z are the second two in values on the line
                #switch(a,b)
                print("Switch detected")
                
            elif line.startswith("turn off"):
                #a = (w,x); #where w and x are the first two int values on the line
                #b = (y,z); #where y and z are the second two in values on the line
                #turnOff(a,b)
                print("Turn off detected")
    
        
        
        #for line in file:
        #   print(line)


def plotMap(L):
    '''function to plot the map for testing purposes'''
    line = [0] * (L-1)
    output = []
    for i in range(0,L):
        output.append(line)
    
    for elem in output:
        print(elem)
        
def main():
    '''main function'''
    q = fileRead("input_assign3.txt")
    plotMap(q)
    #print(plotMap(q))
    
    
if __name__ == '__main__':
    main()