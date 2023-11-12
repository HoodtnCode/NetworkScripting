#### 
#Tim Hood
#Part 2. Demonstrate an understanding of inheritance where one class (AddedNetworkCheck) inherits the attributes and methods from another class (NewNetworkCheck).
#####

#Edit the module AddedNetworkCheck
    
    #Import NewNetworkCheck from Learning_Package.NewNetworkCheck
from Learning_Package.NewNetworkCheck import NewNetworkCheck
import pandas as pd 
#from scapy.layers.l2 import Ether
#from scapy.layers import *
#from scapy.utils import rdpcap
from scapy.all import *



    #Create a new Python Class named AddedNetworkCheck which inherits from the NewNetworkCheck class.
class AddedNetworkCheck(NewNetworkCheck):
        #Within the class:
        #Create a constructor which calls the constructor in the parent. 

    def getPingCount(self,packets):
        self.packets = packets 
        countPing = 0
        #for tcpPacket in allPacket:
        for packet in packets:
            #fixed to remove packet.getlayer[TCP]???
            if (packet.haslayer(TCP)) and (packet[TCP].window) == 4095:
                        countPing += 1
            
        return(countPing) # fixed variable to use lower case 'c' 

#####WEEK 7 In the AddedNetworkCheck class:
#       Create a method called callGrandparent which takes an array as a parameter
#       Call the grandparent’s getMax method.
#       Print the maximum value result.##### 
    def callGrandparent(self, npArray):
        grandMaxValue = super().maxValue(npArray)
        print(grandMaxValue)

