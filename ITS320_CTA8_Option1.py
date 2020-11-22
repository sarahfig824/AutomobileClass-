#------------------------------------------------------------------------
# Program Name: Automobile Class 
# Author:Sarah Figueroa
# Date:12/1/2019
#------------------------------------------------------------------------
# Pseudocode: This program will allow a car dealership to add, remove, update or view iventory for the dealership.
# Class Automobile- constructor that defines what is in an automobile including make, model, color, year and mileage. 
# defset and def getmake allows for the different parameters to be define and returned 
# Class AutomobileDealership- class represents one automobile dealership and may contain many automobiles. The automobile list is empty until user adds automobile to the inventory
# Sample Inventory- populates sample cars into the inventory data to test the functionality
# def add, remove and update will define what will happen if the user selects that option
# if choice==1- addSampleAutomobiles(automobiles). Will add the sample inventory list to inventory
# elif choice==2:automobiles.printAutomobileList(). Will print the inventory list
# elif choice==3: addAutomobile(automobiles). Will add automobile to inventory after user enters automobile details
# elif choice == 4:removeAutomobile(automobiles). Will remove the selected car from the inventory list 
# elif choice == 5:updateAutomobile(automobiles). Will update selected automobile information
# elif choice == 6:  f = open('AutomobileList.txt', 'w')
# f.write((str(automobiles)))
# f.close() allows the user to export the inventory list to a text file 
#-----------------------------------------------------------------------
# Program Inputs: make, model, color, year, mileage, car number in inventory 
# Program Outputs: automobiles in inventory 
#------------------------------------------------------------------------
class Automobile:
    # constructor, it takes parameters make, model, year and mileage
    def __init__(self,aMake,aModel,aColor,aYear,aMileage):
        # assign passed values to instance variables
        self.setMake(aMake)  # string
        self.setModel(aModel)  # string
        self.setColor(aColor) # string
        self.setYear(aYear)   # int
        self.setMileage(aMileage)  # int

    # setter of make
    # it takes 1 parameter make
    # it doesn't returns anything
    def setMake(self, aMake):
        self.__make = aMake

    # getter of make
    # it doesn't take any parameters
    # it returns make
    def getMake(self):
        return self.__make

    # setter of model
    # it takes 1 parameter model
    # it doesn't returns anything
    def setModel(self, aModel):
        self.__model = aModel

    # getter of model
    # it doesn't take any parameters
    # it returns model
    def getModel(self):
        return self.__model

    # setter of color
    # it takes 1 parameter color
    # it doesn't returns anything
    def setColor(self, aColor):
        self.__color = aColor
        return True

    # getter of color
    # it doesn't take any parameters
    # it returns color
    def getColor(self):
        return self.__color

    # setter of year
    # it takes 1 parameter year
    # it doesn't returns anything
    def setYear(self, aYear):
        self.__year = aYear

    # getter of year
    # it doesn't take any parameters
    # it returns year
    def getYear(self):
        return self.__year

    # setter of mileage
    # it takes 1 parameter year
    # it doesn't returns anything
    def setMileage(self, aMileage):
        self.__mileage = aMileage

    # getter of mileage
    # it doesn't take any parameters
    # it returns mileage
    def getMileage(self):
        return self.__mileage

    # string representation of the instance variables
    # it doesn't take any parameters
    # it returns string form of object
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.getMake(),self.getModel(),self.getColor(),self.getYear(),self.getMileage())

# this class represents one automobile dealership and may contain many automobiles
class Automobiledealership:

    # constructor
    # it initializes the empty automobile list
    def __init__(self):
        self.__automobilelist = []

    # adds automobile to dealership
    # it takes automobile class object as parameter
    # it doesn't returns anything
    def addAutomobile(self, automobile):
        self.__automobilelist.append(automobile)

    # removes automobile from dealership
    # it takes index of automobile in the list as parameter
    # it doesn't returns anything
    def removeAutomobile(self, index):
        del self.__automobilelist[index-1]

    # returns automobile from dealership
    # it takes index of automobile in the list as parameter
    # it returns automobile object located at that index
    def getAutomobile(self, index):
        return self.__automobilelist[index-1]

    # prints the list of automobiles
    # it doesn't take any parameters
    # it doesn't returns anything
    def printAutomobileList(self):
        if len(self.__automobilelist)==0:
            print("No automobiles in dealership")
        else:
            for i in range(len(self.__automobilelist)):
                print("{}. {}".format(i+1,self.__automobilelist[i]))

    # defines the _st_ for the user to export to file
    def __str__(self):
      return str(self.__automobilelist)

    

# add some automobiles to the dealership for Sample Inventory
def addSampleAutomobiles(automobiles):
    automobiles.addAutomobile(Automobile("Ford", "Focus", "Red", 2019, 8000))
    automobiles.addAutomobile(Automobile("Toyota","Corolla","White",2007,65000))
    automobiles.addAutomobile(Automobile("Ford","Endura","Black",2019,5000))
    automobiles.addAutomobile(Automobile("Audio","A1","White",2016,23000))
    automobiles.addAutomobile(Automobile("Toyota", "Camry", "Red", 2000, 25000))
    automobiles.addAutomobile(Automobile("Ford","Everest","Black",2017,16000))
    automobiles.addAutomobile(Automobile("Mazda","MX5","Red",2015,33000))
    automobiles.addAutomobile(Automobile("Ford","Escape","Grey",2018,15000))
    automobiles.addAutomobile(Automobile("Toyota", "Prius", "Red", 2010, 35000))

def addAutomobile(automobiles):
    make = input("Please enter Make >> ")
    model = input("Please enter Model >> ")
    color = input("Please enter Color >> ")
    year = int(input("Please enter Year >> "))
    mileage = int(input("Please enter Mileage >> "))
    automobiles.addAutomobile(Automobile(make,model,color,year,mileage))

def removeAutomobile(automobiles):
    index = int(input("Please enter number of the automobile to be removed >> "))
    automobiles.removeAutomobile(index)

def updateAutomobile(automobiles):
    index = int(input("Please enter number of the automobile to be updated >> "))
    automobile = automobiles.getAutomobile(index)
    make = input("Please enter Make (enter 0 to skip) >> ")
    model = input("Please enter Model (enter 0 to skip) >> ")
    color = input("Please enter Color (enter 0 to skip) >> ")
    year = int(input("Please enter Year (enter 0 to skip) >> "))
    mileage = int(input("Please enter Mileage (enter -1 to skip) >> "))
    if make!='0':
        automobile.setMake(make)
        print("Automobile make is updated")
    if model!='0':
        automobile.setModel(model)
        print("Automobile model is updated")
    if color!='0':
        automobile.setColor(color)
        print("Automobile color is updated")
    if year!=0:
        automobile.setYear(year)
        print("Automobile year is updated")
    if mileage!=-1:
        automobile.setMileage(mileage)
        print("Automobile mileage is updated")

# create automobile dealership object
automobiles = Automobiledealership()
choice = -1
# start loop
while choice!=0:
    print()
    print("1. Add sample automobiles to dealership")
    print("2. Display automobiles in the dealership")
    print("3. Add automobile to dealership")
    print("4. Remove automobile from dealership")
    print("5. Update automobile at dealership")
    print("6. Export Inventory List")
    print("0. Exit program")

    choice = int(input("Your choice >> "))
    print()

    if choice==1:
        addSampleAutomobiles(automobiles)
    elif choice==2:
        automobiles.printAutomobileList()
    elif choice==3:
        addAutomobile(automobiles)
    elif choice == 4:
        removeAutomobile(automobiles)
    elif choice == 5:
        updateAutomobile(automobiles)
    elif choice == 6:
      f = open('AutomobileList.txt', 'w')
      f.write((str(automobiles)))
      f.close()