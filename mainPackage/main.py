'''
Created on Feb 24, 2017

@author: danie
'''
# a = first set of co-ords
# b = second set of co-ords
def turnOn(a,b,c,d):
    '''Function intended to handle turnOn feature'''
    output = []
    #for elem in range (a,b+1):
        #if element is in range, make it True i.e. Turn on light
        #ignroing if light is already on
        #elem == True;
        #output += elem
    return output;


def switch(a,b):
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
        L = int(x)
        #return L
        for line in file:
            
            if line.startswith("turn on"):
                print("Turn on detected")
                print(line.split(" ")[2])
                print(line.split(" ")[4])
                print()
                #a = 
                #c =
                #c =
                #d =
                #turnOn(a,b,c,d)
                
                
            elif line.startswith("switch"):
                print("Switch detected")
                print(line.split(" ")[1])
                print(line.split(" ")[3])
                print()
                #a = (w,x); #where w and x are the first two int values on the line
                #b = (y,z); #where y and z are the second two in values on the line
                #switch(a,b)
                
                
            elif line.startswith("turn off"):
                print("Turn off detected")
                print(line.split(" ")[2])
                print(line.split(" ")[4])
                print()
                #a = (w,x); #where w and x are the first two int values on the line
                #b = (y,z); #where y and z are the second two in values on the line
                #turnOff(a,b)
                
    
        
        
        #for line in file:
        #   print(line)


def plotMap(L):
    '''function to plot the map for testing purposes'''
    line = [False] * (L-1)
    output = []
    for i in range(0,L-1):
        output.append(line)
    
    for elem in output:
        print(elem)
     
    return output
    
def main():
    '''main function'''
    q = fileRead("input_assign3.txt")

    
    
if __name__ == '__main__':
    main()