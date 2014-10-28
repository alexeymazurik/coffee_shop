import os
import storehouse


	

class Manager(object):
  	
      def __init__(self):
  		  super(Manager, self).__init__()
  			

      def checkStorage(self):
        for x in self.Store:
          x.printSupply()
  			

      Store = []


class Cooker(Manager):
  		"""docstring for Cooker"""
  		def __init__(self, arg):
  			super(Cooker, self).__init__()
  			self.arg = arg

  		def cookCoffee():
  			pass

  		def cookTea():
  			pass





class Cashier(object):
  		
  		def __init__(self):
  			super(Cashier, self).__init__()
  			
		task = []

  		def getTask(self):
  			c = 'y'
  			while (c!='n'):
  				id = int(raw_input('Enter id '))
  				count = int(raw_input('Enter count '))
  				for x in storehouse.StoreKeeper.Store:
  					if (x.id == id):
  						for x in xrange(1,count):		
  							self.task.append(x)

  				c = raw_input('More?');

  		def makeTask():
  			pass

  		def finanse(self):
  			for x in self.task:
  				sum += self.task.price

  		def printCheck():
  			pass
  			


    




  			
  			
  		

