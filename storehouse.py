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
            for x in self.Store:
                if(x.id == id):
                    x.printSupply()
            name = raw_input('Enter name ')
            count = int(input('Enter count '))
            price = float(input('Enter price '))
            self.removeFromStorage(id);
            self.addToStorage(id,name,count,price)
               

        



class Supply(object):
        
        ID = 0

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
            print('id ' + str(self.id))
            print('name '+ self.name)
            print('count '+str(self.count))
            print('price'+ str(self.price))

