import os
#import storehouse
import cafeShop 
import inputter

class consoleManager(object):

    keeper = cafeShop.StoreKeeper()
    cashier = cafeShop.Cashier()

    def __init__(self):
		super(consoleManager, self).__init__()


    

    def mainMenu(self):
        os.system('clear')
        print(' 1.Storehouse \n 2.Check Estimates  \n 3.Make an order \n 4.Exit ')
        a = int(inputter.checkInput('Enter number of command:' ))

    	if a == 1:
            os.system('clear')
            self.storehouseMenu()
            self.cashier.checkStorage()
        	

    	elif a == 2:
            os.system('clear')
            self.cashier.checkOut()
            a = raw_input('Press b key for back ')
            if (a == 'b'):
                self.mainMenu()

    	elif a == 3:
            self.cashier.getTask()
            a = raw_input('Press b key for back ')
            if (a == 'b'):
                self.mainMenu()
        elif a == 4:
            os.system('exit')


    def storehouseMenu(self):
            self.printStoreHouseMenu()
            a = int(input('Enter number of command:' ))
            while 1:
                if a == 1:
                    name = raw_input('Enter name: ')
                    count = int(inputter.checkInput('Enter count: '))
                    price = float(inputter.checkInput('Enter price: '))
                    s = self.keeper.addToStorage(name,count,price)
                    self.keeper.checkStorage()
                    self.cashier.addToMenu(s)
                    self.printStoreHouseMenu()
                    a = int(input('Enter number of command:' ))
                elif a == 2:
                    id = int(inputter.checkInput('Enter id '))
                    self.keeper.editSupplyFromStorage(id)
                    self.keeper.checkStorage()
                    self.printStoreHouseMenu()
                    a = int(inputter.checkInput('Enter number of command:' ))
                elif a == 3:
                    id = int(inputter.checkInput('Enter id '))
                    self.keeper.removeFromStorage(id)
                    self.keeper.checkStorage()
                    self.printStoreHouseMenu()
                    a = int(inputter.checkInput('Enter number of command:' ))
                elif a == 4:
                    os.system('clear')
                    self.mainMenu()

    def printStoreHouseMenu(self):
        os.system('clear')
        print('OUR STORE HOUSE:')
        self.keeper.checkStorage()
        print('\n')
        print(' 1.Add Supply \n 2.Edit Supply  \n 3.Delete Supply  \n 4.Back to main menu  ')
   



consoleManager().mainMenu()


