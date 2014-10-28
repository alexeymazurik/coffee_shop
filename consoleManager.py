import os
import storehouse
import cafeShop
import curses

class consoleManager(object):

    keeper = storehouse.StoreKeeper()
    cashier = cafeShop.Cashier()

    def __init__(self):
		super(consoleManager, self).__init__()
		

    def mainMenu(self):   
        print(' 1.Storehouse \n 2.Check Estimates  \n 3.Make an order  \n  ')
        a = int(input('Enter number of command:' ))

    	if a == 1:
            os.system('clear')
            self.storehouseMenu()
        	

    	elif a == 2:
            os.system('clear')
            self.cashier.checkOut()
            a = raw_input('Press b key for back ')
            if (a == 'b'):
                self.mainMenu()

    	elif a == 3:
            self.keeper.checkStorage()
            self.cashier.getTask()
            a = raw_input('Press b key for back ')
            if (a == 'b'):
                self.mainMenu()

    def storehouseMenu(self):
        
            print(' 1.Add Supply \n 2.Edit Supply  \n 3.Delete Supply  \n 4.Back to main menu  ')
            a = int(input('Enter number of command:' ))
            while 1:
                if a == 1:
                    id = int(input('Enter id '))
                    name = raw_input('Enter name ')
                    count = int(input('Enter count '))
                    price = float(input('Enter price '))
                    self.keeper.addToStorage(id,name,count,price)
                    self.keeper.checkStorage()
                    a = int(input('Enter number of command:' ))
                elif a == 2:
                    id = int(input('Enter id '))
                    self.keeper.editSupplyFromStorage(id)
                    self.keeper.checkStorage()
                    a = int(input('Enter number of command:' ))
                elif a == 3:
                    id = int(input('Enter id '))
                    self.keeper.removeFromStorage(id)
                    self.keeper.checkStorage()
                    a = int(input('Enter number of command:' ))
                elif a == 4:
                    os.system('clear')
                    self.mainMenu()

   



consoleManager().mainMenu()


