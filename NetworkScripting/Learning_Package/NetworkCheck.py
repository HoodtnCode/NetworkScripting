
#Tim Hood
#Creating Packages and Modules
####

#import 3rd party packages
import numpy as np 

#import scapy udp and ether for week 3 assignment (Giles, 2022)
from scapy.layers.inet import UDP 
from scapy.layers.l2 import Ether

import pandas as pd
from multipledispatch import dispatch
import Learning_Package.Tools as cm
  
#****WEEK 2 ****************WEEK 2**************************WEEK 2********

#create NetworkCheck class to build methods(functions) to convert list to array, max/min/unique value of array and dictionary keys = dimension:shape:lastItem:columnZero:second row. values usig numpy module for keys
class NetworkCheck:
    #method to convert list to an array 
    def convertList2NpArray(self, list):
        return np.array(list)

    #method to get the maximum value from the array
    def maxValue (self, npArray):
        return np.max(npArray)
    
    #method to get the minimum value from the array
    def minValue (self, npArray):
        return np.min(npArray)

    #method to get the unique value from the array
    def uniqueValue(self, npArray):
        return np.unique(npArray)

    #method to get description values for each array dimension, shape, and slice last item, column zero value, the second array 
    def getDescriptiveInfo (self, list):
        myDict ={} #establishes a dictionary with variable 
        count = 1 # set initial count value
        #loop over array to get dimension, shape, last item, column zero, 2nd row each list place in a dictionary
        for listForLoop in list: 
            listA = np.array(listForLoop) #convert listForLoop list to array and assign to listA variable
            colmZero = listA[0,0], listA[1,0] #assign first item (zero) of each array shape 0 & 1 to colmZero variable
        
            strCount = str(count) #convert count # to string assign to variable
            myDict["Dimension" + strCount] = listA.ndim #get dim of list & append count#
            myDict['Shape' + strCount] = listA.shape #get shape of list & append count#
            myDict['LastItem' + strCount] = listA[1,-1] #get lastitem list & append count#
            myDict['Column0' + strCount] = colmZero #colum zeros and count#
            myDict['SecoundRow' + strCount] = listA[1:] # secound row

            count += 1 #increment count # and assign to count variable

        return myDict #return with dictionary value


#***WEEK 3******************** WEEK 3 *******************WEEK 3*******


#Edit the NetworkCheck.py module, in the constructor add private, protected, and public attributes, and outside the constructor add four getters and two setter methods: 
    def __init__(self):
       self.__ipCount = 0 #private
       self.__sportCount = 0 #private
       self.__message1 = "Welcome to message 1" # private
       self._message2 = 'Welcome to message 2' #restricted
       self.message3 = 'Welcome to message 3'
    
    #getter message1 private attribute
    def getmessage1(self):
        return self.__message1

    #getter message2 protected attribtue
    def getmessage2(self):
        return self._message2

    #Create both a getter and setter method for sport.  Consider naming these setSourcePortCount and getSourcePortCount.

    #setSource port method (Giles, 2022)
    def setSourcePortCount (self, packets, readPort): #attribute packets and readport
        self.packets = packets #set atrribute to passed in values
        for packet in packets: #loop over packets in packet file
            if packet.haslayer(UDP): #condition statment looking for UPD in packet
                if (packet.sport == readPort):#condition looking for passed in port
                    self.__sportCount += 1 # if found increment counter assign to private attribute

    def getSourcePortCount(self):# callable outside of class
        return(self.__sportCount) # return the value of private attribute

#Create both a getter and setter method for ip_count.  Consider naming these setSourceIPCount and getSourceIPCount.

    #setIP method (Giles, 2022)
    def setSourceIPCount (self, packets, macAddr): #attribute packets and readport
        self.packets = packets #set atrribute to pass in pcap values
        for packet in packets: #loop over packets in packet file
            if (packet[Ether].src == macAddr): #condition statment looking for MAC string in ETHERNET packets
                self.__ipCount += 1 # if found increment counter assign to private attribute

    def getSourceIPCount(self):# callable outside of class
        return(self.__ipCount) # return the value of private attribute

#******************************************* WEEK 4 ***************************************
#Demonstrate an understanding of overloading , where you have two or more functions (checkCounts) with the same name but different parameters.
#   Edit the module NetworkCheck.py.  Within the class create the following two overloaded      functions:
#       checkCounts(csv_data, feature)
#           Read the file and return value_counts Links to an external site.for the feature.
#       checkCounts(csv_data, feature1, feature2, feature3)
#           Similar to checkCounts with one feature, however instead of returning        values_counts for one feature, return a dictionary of key:value pairs for value_counts of feature1, 2, and 3.


    
    csvD = cm.csv_data
    feat1 = cm.feature1
    feat2 = cm.feature2
    feat3 = feature_3 = cm.feature3
    

    #OVERLOAD AREA Start
    #show understnding
    def checkCounts(csvD, feat3):
        csvData = pd.read_csv(csvD) #read in csv data -MAYBE CAN DELETE
        value1 =  csvData[feat1].value_counts()
        return (value1)
    #show understanding
    @dispatch(object, object, object)
    def checkCounts(feature1, feature2, feature3):
        csvDict = {} #dictionary to add in key value pairs
        countOver = 1
        strCountOver = str(countOver)
        for feature in checkCounts:
            csvDict['Feature' + strCountOver] = pd[feature].value_count()
            countOver += 1
        return csvDict 
    #myTest
    @dispatch(object,object)
    def checkCounts(csvFile, feature_3):
        csvData = pd.read_csv(csvFile) #read in csv data -MAYBE CAN DELETE
        value1 =  csvData[feature_3].value_counts()
        return value1
    #myTest
    @dispatch(object, object, object, object)
    def checkCounts(csvFile, feature1, feature2, feature3):
        csvData = pd.read_csv(csvFile)
        csvOverDict = {} #dictionary to add in key value pairs
        countOver = 1
        checkFeatures = cm.feature1, cm.feature2, cm.feature3
        #strCountOver = str(countOver) -MAYBE DELETE
        for feature in checkFeatures:
            #colFeature = feature + strCountOver
            csvOverDict[feature] = csvData[feature].value_counts()
            countOver += 1
            print() #space
        return csvOverDict 


    #OVERLOAD AREA END
#*****************************  END WEEK 4 ************************************************
        
        
