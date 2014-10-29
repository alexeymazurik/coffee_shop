import cafeShop

class StoreKeeper(cafeShop.Manager):
        
        def __init__(self):
            super(StoreKeeper, self).__init__()
            s = Supply('Cake',15,4)
            self.Store.append(s);
            s = Supply('IceCream',23,2)
            self.Store.append(s);


        def addToStorage(self,name,count,price):
            s = Supply(name,count,price)
            self.Store.append(s)
            return s

        def removeFromStorage(self,id):
            for x in self.Store:
                if(x.id == id):
                    self.Store.remove(x)
            

        def editSupplyFromStorage(self,id):
            name = raw_input('Enter name \n')
            count = int(input('Enter count \n'))
            price = float(input('Enter price \n'))
            self.removeFromStorage(id);
            self.addToStorage(name,count,price)
               

        



class Supply(object):
        
        ID = 3

        def __init__(self, name, count, price):
            super(Supply, self).__init__()
            self.id = Supply.ID
            self.name = name
            self.count = count
            self.price = price
            Supply.ID = Supply.ID + 1

        def  getPrice():
            pass

        def  setPrice():
            pass

        def getCount():
            pass

        def setCount():
            pass

        def printSupply(self):
            print("ID: " + str(self.id) + "  Name: " + self.name + "  Count: " + str(self.count) + "  Price: " + str(self.price))

