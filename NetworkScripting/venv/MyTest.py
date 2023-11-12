#### 
#Tim Hood
#Creating Packages and Modules
####
print()
#import 3rd-party packages 
import numpy as np
#import tools from learning 235 package 
import Learning_Package.Tools as cm
import sys #import system package
import logging  #import logging package

#WEEK 6 Create debug file, encode in utf-8, at a debug level. file wii be saved in same directory as MyTest. append is default filemode
logging.basicConfig(filename = 'DebugFile.log', encoding = 'utf-8', level=logging.DEBUG, format = '%(asctime)s: %(levelname)s: %(name)s: %(message)s') 
#WEEK 6 logging start of program.
logging.info('Start of MyTest script program.')

#combine the imported list data from the Tools.py file into a variable
combinedList = cm.mySubList1 + cm.mySubList2 + cm.mySubList3

#WEEK 6 log if combined list not a list, log as error, and exit

try:
	if not type(combinedList) is list: #if combined list is not equal to list
		logging.error('The combinedList  object is not a list type')
		logging.info('MyTest.py exited at sys.exit(1). line 21.')
		value= 'The combined list is not a list type. Sys.exit(1)' #marker reference with sys.exit(x)
		sys.exit(1)

	else:
		logging.info('Combined list is a list type. MyTest.py continues')
		pass #pass over except line. 
except: #to get out out try loop
	sys.exit(value) #can only be raise on main or cleanup of try, except, finally lines. 
	

#make list for later in code
listArray = (cm.mySubList1, cm.mySubList2, cm.mySubList3)

#print the combined list
print('The combined list is: ')
print(combinedList)
print()

#New section 
# make an array with the combined list and store in a new variable matrix (Taulien, 2020)
nparrayCombinedList = np.array(combinedList)
#print(nparrayCombinedList)
#print()

#break out array min, max, unique values and print them
print('The minimum value from the combined array is:', np.min(nparrayCombinedList))
print()
print('The maximum value from the combined array is:', np.max(nparrayCombinedList))
print()
print('The unique values from the combined array are:\n', np.unique(nparrayCombinedList))
print()
    
#loop over listArray variable to get this section work array, shape, dimension
for list in listArray:
    print('*************************** Array, Shape, Dimension *********************************')
    print('The array is: ') 
    listA= np.array(list) #convert sublist into an array
    print(listA) #print the list array
    print('The dimension of the array is ', np.ndim(list))#numpy.ndim dimension 2 list
    print('The data shape ', np.shape(list)) #numpy.shape shape of array 2 set, 12 data
    #print('The data shape is ',np.shape(cm.mySublist1))
    print()
    print('*************************** Slice array *********************************************')
    #arrayList = np.array(list) #put list in array of two dimensions and assign variable (Telusko, 2018) (Ramalho, 2022) (Noureddin Sadawi, 2016)
    print('The last item is', listA[1,11])
    columnValue = listA[0,0], listA[1,0]
    print('Column 0 numbers of the array', columnValue)
    print('The second row is', listA[1]) #get the second row of the 2-d array
    print()
print('*************************** Week1 End ***********************************************')
print()#space
print('*************************** Week2 Append and Start ***********************************')

#import NetworkCheck class
import Learning_Package.NetworkCheck as nc 
#list variable is object and a list built from sublist from Tools file import 
list = [cm.mySubList1, cm.mySubList2, cm.mySubList3]
print()
print('************************ This is a listing of the sublists *************************** \n')
print(list)
print()

#assign object listArray to class NetworkCheck
listArray2 = nc.NetworkCheck()

#WEEK 6 Log when NetworkCheck object created 
logging.info('The NetworkCheck class object is created')

#WEEK 6 print and log an error message and exit the program when your object is not an instance of the NetworkCheck class.
try:
	if isinstance(listArray2, type(listArray2)):#type(listArray2)):
		logging.info('Object listArray2 is an instance of NetworkCheck. MyTest.py continues')
		pass
		
	else:
		logging.error('The listArray2 object is not an instance of the NetworkCheck')
		logging.info('MyTest.py exited at sys.exit(2). Line 92')
		value = 'The listArray2 object is not an instance of the NetworkCheck. Sys.exit(2)'
		sys.exit(2)
except: #to get out out try loop
	sys.exit(value)

#object variables to call methods in the NetworkCheck class 
  #call class NetworkCheck and convert list to array and assign to npArray value
npArray = listArray2.convertList2NpArray(list) 


#call class NetworkCheck and get max value from entire array assign to max variable 
max = listArray2.maxValue(list)

#WEEK 6 Update this code to raise an exception when: The maximum value is greater than 100
try:
	if max > 100:
		logging.error('The max value is %{max} greater than 100')
		logging.info('MyTest.py exited at Sys.exit(3). Line 117')
		value = 'The max value is greater than 100. Sys exit(3).'
		sys.exit(3)
	else:
		logging.info('The max value is good')
		pass
except:
	sys.exit(value)



#call class NetworkCheck and get min value from entire array assign to min variable 
min = listArray2.minValue(list)

#WEEK 6 Update this code to raise an exception when: The minimum value is less than -100.
try:
	if min < -100:
		logging.error('The min value is less than -100')
		logging.info('MyTest.py exited at Sys.exit(4). Line 135')
		value = 'The min value is less than 100. Sys exit(4). Line 140'
		sys.exit(4)
	else:
		logging.info('The min value is good')
		pass
except:
	sys.exit(value)


#call class NetworkCheck and get unique value from array assign to unique variable 
unique = listArray2.uniqueValue(list)

#call class NetworkCheck and get description values from each array build in a dictionary 
myDict = listArray2.getDescriptiveInfo(list)

#WEEK 6 Update this code to print and log an error message and exit the program when your dictionary (i.e. myDict) is not of type dict.
try:
	if not type(myDict) is dict:
		logging.error('The object MyDict is not of type dictionary. Sys exit(5). Line 158')
		logging.info('MyTest.py exited at Sys.exit(5). Line 155')
		value = 'The object MyDict is not of type dictionary. Sys exit(5)'
		sys.exit(5)
	else:
		logging.info('The object MyDict is of the type dictionary')
		pass
except:
	sys.exit(value)


#print OOP return for converting list to array method
print('******************** The list array is**************************\n\n',npArray)
print() #space

#print OOP return for max value method
print('******************** The list maximum value is *****************\n\n',max )
print() #space

#print OOP return for min value method
print('******************** The list minimum value is *****************\n\n', min)
print() #space

#print OOP return for unique value method
print('******************** The unique numbers are ********************\n\n', unique)
print() #space

#print OOP return for min value method
print('******************** The description dictionary tuple ***********\n\n', myDict)


print('*************************** END WEEK 2 ***********************************************')
print() #space

print('*************************** START WEEK 3 *********************************************')
#Edit MyTest.py module

#from scapy.all import * #import all scapy module
from scapy.utils import rdpcap
from scapy.layers.inet import UDP #import Layer UPD from scapy

print() #space
print('********************************** Message Print ***************************************')
print() #space
#Try to directly get the private message1 attribute. Be sure to use a TRY/EXCEPT.
try:
    print(listArray2.message1)
    print()#space
except:
    print('Could not get private attribute message1 of class NetworkCheck directly. This is an except return when failed')
    print()#space

#Use the getter method to get the private message1 attribute.
try:
    m1 = listArray2.getmessage1()
    print('Message 1 private class data accuried')
    print()#space
except:
    print('Could not get private attribute message1 of class NetworkCheck directly. This is an except return when failed')
    print()#space

#Try to directly get the protected message2 attribute. Be sure to use a TRY/EXCEPT.
try:
    print(listArray2.message2)
    print()#space
except:
    print('Could not get protected attribute message2 of class NetworkCheck directly. This is an except return when failed')
    print()#space

#Use the getter method to get the protected message2 attribute.
try:
    m2 = listArray2.getmessage2()
    print('Message2 private class data accuried')
    print()#space
except:
    print('Could not get private attricture message1 of class NetworkCheck directly. This is an excpet retrun when failed')
    print()#space

#Get the public message3 attribute.
m3 = listArray2.message3

#separate out message x 
message1Word = m1[11:]
message2Word = m2[11:]
message3Word = m3[11:]

#print(message1Word, message2Word, message3Word, " DELETE ") #can delete before turnin

#capitals first letter of messages 1, 2, & 3
capitalM1 = message1Word[0].upper() + message1Word[1:7] + message1Word[8]
capitalM2 = message2Word[0].upper() + message2Word[1:7] + message2Word[8]
capitalM3 = message3Word[0].upper() + message3Word[1:]

#Print the three messages on one line using f-strings.  Right justify the message output by 25
print(f"{capitalM1:>26}  {m1 + ' ' + capitalM2}  {m2 +' '+ capitalM3}  {m3}")

print()
print('************************************** End of Messages *********************************')
print()#space
print('************************************** Network Space ***********************************')
print()


#WEEK 6: Update this code to print and log an error message and exit the program when the pcap file read fails.
try:
#Week 3 Read in the packet capture file using the pcap variabe.
	packets = rdpcap(cm.pcap) #cm is import for tools module (Giles, 2022)
	logging.info('Pcap file read: %s', cm.pcap)
except Exception as err:
	logging.error('Unable to read pcap file: %s. Sys exit(6)', err)
	logging.info('MyTest.py exited at Sys.exit(6), Line 266')
	sys.exit(err)


#Use the setter and getter for sport

readPort = cm.sport # get port number from CM235 Tools

#call the set function and pass in PCAP file read and port number
listArray2.setSourcePortCount(packets,readPort)

#call getter and set output to varialbe
sourceCount = listArray2.getSourcePortCount()

#WEEK 6: Update this code to print and log an error message and exit the program for the following two conditions: Source port count is of not of type int
try:
	if not type(sourceCount) is int:
		logging.error('The sourceCount value %s is not of type int. Sys exit(7).',sourceCount)
		logging.info('MyTest.py exited at Sys.exit(7). Line 279')
		value = 'The sourceCount value ',sourceCount,' is not of type interger'
		sys.exit(7)
	else:
		logging.info('The sourceCount value %s is an interger',sourceCount)
		pass
except:
	sys.exit(value)

#print out the number of ports found. 
print('Number of UPD packets where the source port =',readPort, 'is', sourceCount)
print()#space

#Use the setter and getter for ip address

macAddr = cm.mac_address # get IP address from Tools module

#call the set function and pass PCAP file and IP address into method
listArray2.setSourceIPCount(packets, macAddr)

#call getter method and set IP count to variable
macCount = listArray2.getSourceIPCount()

#WEEK 6: Update this code to print and log an error message and exit the program for the following two conditions: MAC address count is of not of type int
try:
	if not type(sourceCount) is int:
		logging.error('The macCount value %s is not of type int. Sys exit(8).',macCount)
		logging.info('MyTest.py exited at Sys.exit(8). Line 303')
		value = 'The macCount value ',macCount,' is not of type interger'
		sys.exit(8)
	else:
		logging.info('The MAC address value %s is an interger',macCount)
		pass
except:
	sys.exit(value)

print('Number of Ethernet packets that contain MAC =', macAddr, 'is', macCount)
print()#spacing
print('**************************** End of Network Space *************************************')
print()
print('**************************** END OF WEEK 3 ASSIGNMENT **********************************')
print()#spacing

print('**************************** START WEEK 4 *********************************************')

import Learning_Package.NewNetworkCheck as nnc
print()#spacing

#Check = Learning_Package.NewNetworkCheck()
newcheck = nnc.NewNetworkCheck()

#WEEK 6 Log when NewNetworkCheck object created 
logging.info('The NewNetworkCheck class object is created')


#WEEK 6 Update this code to print and log an error message and exit the program when your object is not an instance of the NewNetworkCheck class
try:
	if isinstance(newcheck, type(newcheck)): #newcheck inherits (chiled) from listArray2 (parent) class
	#if not str(type(newcheck)) == 'Learning_Package.NewNetworkCheck.NewNetworkCheck': #if newcheck object is not an instance of NetworkCheck
		logging.info('Object newcheck is an instance of NewNetworkCheck. MyTest.py continues')
		pass
		
	else:
		logging.error('The newcheck object is not an instance of the NewNetworkCheck. Sys exit(9). Line 331.')
		logging.info('MyTest.py exited at sys.exit(9) line 350')
		value = 'The newcheck object is not an instance of the NewNetworkCheck class. Sys.exit(9)'
		sys.exit(9)

except: #to get out out try loop
	sys.exit(value)

print()
print(newcheck.getDescriptiveInfo(list))
print()#space 
#*******************************************************************************************


# ******************  Edit MyTest.py *******************
#       Using the NetworkCheck object created from week two (listArray2)
#           Call checkCounts passing the the csv_data file and feature3.  Print the value  returned from the function call.

print('*******************  Print Protocol value count week4 ***************************************')
csvFile = cm.csv_data
feature_3 = cm.feature3

value1wk4 = listArray2.checkCounts(csvFile, feature_3)

print('*********************OVERRIDE TWO OBJECTS************************************')
print(value1wk4)
print()

#Call checkCounts passing the csv_data file and feature1, feature2, and feature3.   Print the value returned from the function call.


feature_2 = cm.feature2
feature_1 = cm.feature1
print()
print('***********************OVERRIDE 4 OBJECTS**************************************')
value2wk4 = listArray2.checkCounts(csvFile, feature_1, feature_2, feature_3)

print(value2wk4)

print()
print('**************************** END OF WEEK 4 ASSIGNMENT **********************************')
print()
print('**************************** START WEEK 5 *********************************************')
print()#space
#Edit MyTest.py program and append the following to your code from the previous week. 

#Using NewNetworkCheck class object
  #Call convertList2NpArray to convert the combined list to a nparray and store the array in a new variable.

#store the value
wk5Array = newcheck.convertList2NpArray(list)

print('-------- Print min, max, unique value using Inheratance ------------')

  #Using the newly created array variable and the object:
    #Get and then print the minimum value by calling getMin, passing the newly created array to the method.

wk5min = newcheck.minValue(wk5Array)

print(f'The array has a minimum value of {wk5min}.')

print()#space

#Get and then print the maximum value by calling getMax, passing the newly created array to the method.
wk5max = newcheck.maxValue(wk5Array)
print(f'The array has a maximum value of {wk5max}.')

print()#space
    
    #Get and then print the unique values by calling getUniqueValues, passing the newly created array to the method.
    
wk5Unique = newcheck.uniqueValue(wk5Array)
print(f'The array has a unique values of {wk5Unique}.')

print()#space
print('-------- End min, max, unique value using Inheratance ------------')
print()#space

#Edit MyTest.py program and append the following to your code from the previous week.
#Create an object of the AddedNetworkCheck class and using that object:

#import Learning_Package.AddedNetworkCheck as anc
import Learning_Package.AddedNetworkCheck as anc

#created object
ac = anc.AddedNetworkCheck() #intiated with a default response
print()#space

#WEEK 6 Log when AddedNetworkCheck object created 
logging.info('The AddedNetworkCheck class object is created')

##Call getPingCount passing the pcap file.  Set the return value to a variable,
testwk5 = ac.getPingCount(packets)

#WEEK 6 Update this code to print and log an error message and exit the program when the value returned from getPingCount is not of type int.
try:
	if not type(testwk5) is int:
		logging.error('The object testwk5 value of the getPingCount return in the AddedNetworkCheck class is of the type interger. Sys exit(10).')
		logging.info('MyTest.py exited at Sys.exit(10). Line 443')
		value = 'The testwk5 value is not of type interger. Sys exit(10)'
		sys.exit(10)
	else:
		logging.info('The object testwk5 value of the getPingCount return in the AddedNetworkCheck class is of the type interger')
		pass
except:
	sys.exit(value)

##Print the contents of the variable.
print(f'There are {testwk5}  Window=4095 in the file.')
print()#space

print('Call setSourceIPCount passing the pcap file and the ip address from Tools (i.e. aa:bb:cc:dd:ee:ff)')

wk5SourceIp = ac.setSourceIPCount(packets, macAddr)
wk5GetIPCount = ac.getSourceIPCount()
print(f'The MAC address aa:bb:cc:dd:ee:ff count is {wk5GetIPCount}.')

print()#space
print('Call checkCounts passing the the csv_data file and feature3.  Print the value returned from the function call.')
wk5CheckCounts = ac.checkCounts(csvFile, feature_3)
print()
print('The protocol count values equals') 
print(wk5CheckCounts,'.')
print()#space
print('**************************** END OF WEEK 5 ASSIGNMENT **********************************')
print()
print('**************************** START OF WEEK 6 ASSIGNMENT **********************************')
print('Week 6  ws error checking. See comments starting with "WEEK 6" ')
print()
print('**************************** START OF WEEK 7 ASSIGNMENT **********************************')
print()
#Using the NewNetworkCheck object from Week 4
#   call the “callSuper” method passing the list mySubList2
print("Week 4 object calling parent")

newcheck.callSuper(cm.mySubList2)

#Using a TRY/EXCEPTION statement
#   Check if NewNetworkCheck is a subclass of NetworkCheck.
#   If it is, print a message stating such.
#   If an error occurs, print, log, and exit.
print()
print('*************First Subclass Check NewNetworkCheck -> NetworkCheck**************')
try:
    if issubclass(type(newcheck), type(listArray2)):
        print()
        print('NewNetworkCheck class is a subclass of the NetworkCheck class')
        print()
        print('*******************************************************************************')

except:
    logging.error('NewNetworkCheck class is not a subclass of the NetworkCheck class. Sys exit(11)')
    logging.info('NewNetworkCheck is not a subclass of the NetworkCheck class. Sys exit(11) line 486')
    value = 'NewNetworkCheck class is not a subclass of the NetworkCheck class. Sys exit(11)'
    sys.exit(value)


#WORK ON LAMBDA SECTION
#a = type(newcheck)
#b = type(listArray2)
#yes1 = 'NewNetworkCheck class is a subclass of the NetworkCheck class'
#no1 = 'NewNetworkCheck is not a subclass of the NetworkCheck class. Sys exit(11) line 486' 

#print(a)
#print(b)

#compare = lambda a, b:  yes1 if issubclass(a, b) else logging.error(no1), print(no1), sys.exit(11)

#compare(a, b)

print()

#Using the AddedNetworkCheck object, call the “callGrandparent” method.
#   Pass mySubList3 from the tool module.

print("Week 5 object calling Grandparent")
ac.callGrandparent(cm.mySubList3)

print()

#Create an anonymous function that uses issubclass. Note, you may use the same one created above.
#   Using a TRY/EXCEPTION statement
#   Check if AddedNetworkCheck is a subclass of NetworkCheck
#   If it is, print a message stating such.
#   If an error occurs, print, log, and exit.

print('*************Second Subclass Check AddedNetworkCheck -> Networkcheck**************')
try:
    if issubclass(type(ac), type(listArray2)):
        print()
        print('AddedNetworkCheck class is a subclass of the NetworkCheck class')
        print('Non-lambda')
        print()
        print('*******************************************************************************')

except:
    logging.error('AddedNetworkCheck class is not a subclass of the NetworkCheck class. Sys exit(12)')
    logging.info('AddedNetworkCheck is not a subclass of the NetworkCheck class. Sys exit(12) line 524')
    value = 'AddedNetworkCheck class is not a subclass of the NetworkCheck class. Sys exit(12)'
    sys.exit(value)


#WORK ON LAMBDA SECTION
#a2 = type(ac)
#b2 = type(listArray2)
#yes2 = 'AddedNetworkCheck class is a subclass of the NetworkCheck class'
#no2 = 'AddedNetworkCheck is not a subclass of the NetworkCheck class. Sys exit(12) line 524' 

#print(a2)
#print(b2)

#compare = lambda a, b:  yes2 if False else logging.error(no2), print(no2), sys.exit(12)

#issubclass(compare(a2, b2))

print()

#Create function variables for NewNetworkCheck and AddedNetworkCheck..
#   Using a TRY/EXCEPTION statement
#   Using the function variables. check if AddedNetworkCheck is a subclass of NewNetworkCheck.
#   If it is, print a message stating such.
#   If an error occurs, print, log, and exit.

print('*************** Third SubClass Check Using Function as Variable*******************')
ancVariable = ac
nncVariable = newcheck
print()
try:
    if issubclass(type(ancVariable), type(nncVariable)):
        print('AddedNetworkCheck class is a subclass of the NewNetworkCheck class')
        print('Non-lambda')
        print()
        print('*******************************************************************************')

except:
    logging.error('AddedNetworkCheck class is not a subclass of the NewNetworkCheck class. Sys exit(13)')
    logging.info('AddedNetworkCheck is not a subclass of the NewNetworkCheck class. Sys exit(13) line 575')
    value = 'AddedNetworkCheck class is not a subclass of the NewNetworkCheck class. Sys exit(13)'
    sys.exit(value)

#WORK ON LAMBDA SECTION
#a2 = type(ac)
#b2 = type(listArray2)
#yes2 = 'AddedNetworkCheck class is a subclass of the NetworkCheck class'
#no2 = 'AddedNetworkCheck is not a subclass of the NetworkCheck class. Sys exit(12) line 524' 

#print(a2)
#print(b2)

#compare = lambda a, b:  yes2 if False else logging.error(no2), print(no2), sys.exit(12)

#issubclass(compare(a2, b2))

#Create a recursive method called “repeat”.
#   This will use the base case of:
#       If len(l) == 1.
#       Print the value in this portion.
#   The ELSE statement will:
#       Divide the list in half and get an index number.
#       Create two arrays using that middle index point.
#       Recursively call repeat with the first list.
#       Recursively call repeat with the second list.
#       Call the repeat method using mySubList1[0]. Note, that only uses the first sublist.

print('Can not make reccursive work at this stage.')
#def repeat(object):
#    #wk7List = cm.mySubList1[0] #get list
#    print(object)
#    l = len(object) // 2 #split in half and assign number to variable
#    print(l)
#    [firstListHalf, secondListHalf] = object[:l]#makes 2 list
#    wholeList = [firstListHalf, secondListHalf]# make a whole list
#    splitList = len(l) // 2 #split in half and assign to variable
#    for half in range(wholeList):
#        if len(1) == 1:
#            print(l)
#        else:
#            print(f'List values ',half[i])


#wk7List = cm.mySubList1[0] #get list
#l = len(wk7List) // 2 #split in half and assign number to variable
#firstList, secondList = wk7List[:l]
#recRepeat = repeat(cm.mySubList1[0])
    
print()

sys.exit('Thanks for running the code. The program has run to the end.')
#*************************************************************************

####
#References

#Noureddin Sadawi (Director). (2016, December 28). 7- Numpy: Indexing Multi Dimensional Arrays. https://www.youtube.com/watch?v=ktyW-kOqGpY
#
#Ramalho, L. (2022). Fluent Python: Clear, concise, and effective programming / Luciano Ramalho. Champlain College Library Catalog.
#
#Taulien, K. (2020). Python for Everybody: The Ultimate Python 3 Bootcamp [electronic resource] / Taulien, Kalob. Champlain College Library Catalog.
#
#Telusko (Director). (2018, July 24). #31 Python Tutorial for Beginners | Working with Matrix in Python. https://www.youtube.com/watch?v=Blzp9iuhZqo
####
