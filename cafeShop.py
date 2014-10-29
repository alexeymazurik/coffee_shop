import os
import datetime
import inputter
from abc import ABCMeta, abstractmethod

	

class Manager(object):
  	
      def __init__(self):
  		  super(Manager, self).__init__()
  			

      def checkStorage(self):
      	print('__________________________________________________________________')
        for x in self.Store:
          x.printSupply()
          print('__________________________________________________________________')  			

      Store = []


class StoreKeeper(Manager):
        
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




class Cooker(Manager):

  		def __init__(self):
  			super(Cooker, self).__init__()


  		def cookAmericanoWithMilk(self,count):
  			for x in xrange(1,count+1):
  				Milk(Water(Espresso())).create()
  				print('Your Americano with milk is ready.')

  		def cookCappuccino(self,count):
  			for x in xrange(1,count+1):
  				Cream(Milk(Espresso())).create()
  				print('Your cappuccino is ready')
  		def cookIrishCoffee(self,count):
  			for x in xrange(1,count+1):	
  				Whiskey(Sugar(Cream(Espresso()))).create()
  				print 'Your Irish coffee is ready'

class Cashier(object):
					
			def __init__(self):
				#super(Cashier, self).__init__()
				self.menu.append({'id':0,'name':'IrishCoffee','price':9,'type':'drink'})
				self.menu.append({'id':1,'name':'Cappuccino','price':8,'type':'drink'})
				self.menu.append({'id':2,'name':'Americano with milk','price':10,'type':'drink'})
				for x in StoreKeeper.Store:
					y = {'id':x.id,'name':x.name,'price':x.price,'type':'supply'}
					self.menu.append(y)

			cook = Cooker()
			task = []
			menu = []
			checkEstimates = []
			sum = 0

			def  addToMenu(self,s):
				self.menu.append({'id':s.id,'name':s.name,'price':s.price})
			
			def getTask(self):
				self.task = []
				c = 'y'
				print('__________________________________________________________________')
				for y in self.menu:
					print("ID: " + str(y['id']) + "  Name: " + str(y['name']) + "  Price: " + str(y['price']))
					print('__________________________________________________________________')
				while (c!='n'):
					id = int(inputter.checkInput('Enter id '))
					count = int(inputter.checkInput('Enter count '))
					
					for x in self.menu:
						if(id not in (0,1,2)):
							for y in StoreKeeper.Store:
								if (x['id'] == id) and (y.id == id) :
									if(y.count!=0):
										if(count<=y.count):
											y.count=y.count - count
											self.task.append({'id':x['id'],'name':x['name'],'count':count,'price':x['price']})
										else:
											print('We have only ' + str(y.count) + ' of ' + y.name)
											self.task.append({'id':x['id'],'name':x['name'],'count':y.count,'price':x['price']})
											y.count = 0
									else:
										print("This supply is over")
						else:
							if x['id'] == id:
								self.task.append({'id':x['id'],'name':x['name'],'count':count,'price':x['price']})

							

					c = raw_input('More?');
					self.makeTask()


			def makeTask(self):
				for x in self.task:
					if(x['id'] == 1):
						self.cook.cookCappuccino(x['count'])
					elif(x['id'] == 0):
						self.cook.cookIrishCoffee(x['count'])
					elif(x['id'] == 2):
						self.cook.cookAmericanoWithMilk(x['count'])
  				else:
  					print('Take your '+str(x['count']) +' '+ x['name']+" ,please")

					self.finanse()




			def finanse(self):
				print('Your bill : ')
				self.sum = 0
				for x in self.task:
					self.sum = self.sum + x['price']*x['count']
					print(x["name"] + ' count:'+str(x["count"])+ ' price: '+ str(x['price']))

				print('Sum : = '+str(self.sum))
				self.printCheck()
				self.checkEstimates.append({'time':datetime.datetime.now() ,'sum':self.sum})


			def printCheck(self):
				f = open('bill.txt', 'w')
				sum = 0
				for x in self.task:
					f.write(x["name"] + ' count: '+str(x["count"])+ ' price: '+ str(x['price'])+'\n')
				f.write('Sum  = '+str(self.sum))
				f.close()


			def checkOut(self):
				os.system('clear')
				print('time     sum')
				print('----------------------------------------')
				print("|        Time         |       Sum       ")
				print('----------------------------------------')
				for x in self.checkEstimates:
					print("  " + str(x['time']).rpartition(':')[0] +'    |  '+str(x['sum']) )
					print('----------------------------------------')




class IOperator(object):
  
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def create(self):
        pass
 
 
class Espresso(IOperator):
    
  def __init__(self):
      pass


  def create(self):
    print('Add Coffee')

     
class Water(IOperator):
    
    
    def __init__(self, obj):
        self.obj = obj
        
 
    def create(self):
        self.obj.create()
        print("Add Water")


class Milk(IOperator):
    
    
    def __init__(self, obj):
        self.obj = obj
        
 
    def create(self):
        self.obj.create()
        print("Add Milk")

class Sugar(IOperator):
    
    def __init__(self, obj):
        self.obj = obj
        
 
    def create(self):
        self.obj.create()
        print("Add Sugar")


class Whiskey(IOperator):

    def __init__(self, obj):
        self.obj = obj
 
    def create(self):
        self.obj.create()
        print("Add whiskey")

class Cream(IOperator):
    
    def __init__(self, obj):
        self.obj = obj

    def create(self):
        self.obj.create()
        print("Add Cream")




    




  			
  			
  		

