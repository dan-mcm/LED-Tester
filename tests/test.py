'''
Created on Feb 27, 2017

@author: Daniel McMahon
'''
import unittest
import src.main

class Test(unittest.TestCase):


    def test_turnOn(self):
        self.assertEqual(src.main.turnOn(1,1,2,2,[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]), [[False,False,False,False],[False,True,True,False],[False,True,True,False],[False,False,False,False]])
        
    def test_turnOff(self):
        self.assertEqual(src.main.turnOff(1,1,2,2,[[False,False,False,False],[False,True,True,False],[False,True,True,False],[False,False,False,False]]), [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]])
        
    def test_Switch(self):
        self.assertEqual(src.main.switch(1,1,2,2,[[False,False,False,False],[False,True,False,False],[False,False,True,False],[False,False,False,False]]), [[False,False,False,False],[False,False,True,False],[False,True,False,False],[False,False,False,False]])

    def test_fileReadL(self):
        self.assertEqual(src.main.fileReadL(file="100"),100)
        
    def test_plotMap(self):
        self.assertEqual(src.main.plotMap(2),[[False,False],[False,False]])
        
    def test_applyChanges_standardInput(self):
        self.assertEqual(src.main.applyChanges("turn on 1,1 through 2,2",[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]),[[False,False,False,False],[False,True,True,False],[False,True,True,False],[False,False,False,False]])
    
    #Hmm this is broken........... takes all as false....
    def test_applyChanges_minusInput(self):
        self.assertEqual(src.main.applyChanges("turn on -1,-1 through 1,1",[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]),[[True,True,False,False],[True,True,False,False],[False,False,False,False],[False,False,False,False]])
                                               
    #Hmm this is broken........... takes all as false....   
    def test_applyChanges_surplusInput(self):
        self.assertEqual(src.main.applyChanges("turn on 1,1 through 5,5",[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]),[[False,False,False,False],[False,True,True,True],[False,True,True,True],[False,True,True,True]])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()