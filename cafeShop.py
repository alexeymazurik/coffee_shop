import os
import storehouse
import datetime
from abc import ABCMeta, abstractmethod

	

class Manager(object):
  	
      def __init__(self):
  		  super(Manager, self).__init__()
  			

      def checkStorage(self):
        for x in self.Store:
          x.printSupply()  			

      Store = []


class Cooker(Manager):

  		def __init__(self):
  			super(Cooker, self).__init__()


  		def cookAmericanoWithMilk(self,count):
  			for x in xrange(1,count+1):
  				Milk(Water(Espresso())).create()
  				print('Your Americano with milk is ready')

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
  			super(Cashier, self).__init__()
  			for x in storehouse.StoreKeeper.Store:
  				y = {'id':x.id,'name':x.name,'price':x.price}
  				self.menu.append(y)

  			self.menu.append({'id':10,'name':'IrishCoffee','price':9})
  			self.menu.append({'id':11,'name':'Cappuccino','price':8})
  			self.menu.append({'id':12,'name':'Americano with milk','price':10})

  		cook = Cooker()
		task = []
		menu = []
		checkEstimates = []
		sum = 0

  		def getTask(self):
  			self.task = []
  			c = 'y'
  			for y in self.menu:
  				print(y)
  			while (c!='n'):
  				id = int(raw_input('Enter id '))
  				count = int(raw_input('Enter count '))
  				for x in self.menu:
  					if (x['id'] == id):	
  						self.task.append({'id':x['id'],'name':x['name'],'count':count,'price':x['price']})


  				c = raw_input('More?');
  			self.makeTask()


  		def makeTask(self):
  			for x in self.task:
  				if(x['id'] == 11):
  					self.cook.cookCappuccino(x['count'])
  				elif(x['id'] == 10):
  					self.cook.cookIrishCoffee(x['count'])
  				elif(x['id'] == 12):
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
  			for x in self.checkEstimates:
  				print(str(x['time']).rpartition(':')[0] +'  '+str(x['sum']))
  			




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




    




  			
  			
  		

