#### 
#Tim Hood
#Assignment Creating Packages and Modules
####

#************************************** WEEK 4 *************************************
#####
#Edit the module NewNetworkCheck.py
#Import NetworkCheck from Learning_Package.NetworkCheck
#Import the numpy package as np
#Create a new Python Class named NewNetworkCheck which inherits from the NetworkCheck class.  Within the class:
#Create a constructor which calls the constructor in the parent. 
#Create one new method getDescriptiveInfo which will override the getDescriptiveInfo method in the NetworkCheck class.  getDescriptiveInfo will return a dictionary of key:value pairs for the number of dimensions, shape, mean, median, and standard deviation for of each list.  If there are three lists, and five values for each list, then the returned dictionary would contain 15 key value pairs. This should take all three lists as input.
####

#import Network check
from Learning_Package.NetworkCheck import NetworkCheck

#import numpy
import numpy as np

#create class (Numpy.Std — NumPy v1.23 Manual, n.d.)
class NewNetworkCheck(NetworkCheck):
    
    def getDescriptiveInfo(self, list):
        newDict= {} #establish the dicionary for new descriptive info
        newCount = 1 #iterate over the key value pairs
        for newList in list:
            listB = np.array(newList)
            #newColumZero = listB[0,0], listB[1,0] =DELETE NOT NEEDED
            mean = np.mean(listB) #produce mean for the array
            median = np.median(listB)
            stddev = np.std(listB)

            newStrCount = str(newCount)

            newDict["Dimension" + newStrCount] = listB.ndim #get dim of list & append count#
            newDict['Shape' + newStrCount] = listB.shape #get shape of list & append count#
            newDict['Mean' + newStrCount] = mean #get mean of array
            newDict['Median' + newStrCount] = median #get median of array
            newDict['Standard Deviation' + newStrCount] = stddev #get standrad deviation

            newCount += 1

        return newDict

#WEEK7 In the NewNetworkCheck class:
#          Create a method called callSuper which takes an array as a parameter.
#          Call the parent of NewNetworkCheck’s getMin method.
#          Print the minimum value result.
    def callSuper(self, npArray):
        parentMinValue = super().minValue(npArray)
        print(parentMinValue)

    


#Reference
####
#numpy.std—NumPy v1.23 Manual. (n.d.). Retrieved November 27, 2022, from https://numpy.org/doc/stable/reference/generated/numpy.std.html
#####

