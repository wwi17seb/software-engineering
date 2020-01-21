class DoorState(object):

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print('Current:',self,' => switched to new state',state.name)
         self.__class__ = state
      else:
         print ('Current:',self,' => switching to',state.name,'not possible.')

   def __str__(self):
      return self.name

class Open(DoorState):
   """ State of the door being open """
   name = "open"
   allowed = ['closed']

class Closed(DoorState):
   """ State of the door being closed """
   name = "closed"
   allowed = ['open', 'locked']

class Locked(DoorState):
   """ State of the door being locked """
   name = "locked"
   allowed = ['closed']

class Door(object):
   
   def __init__(self):
      self.state = Closed()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   frontdoor = Door()
   frontdoor.change(Open)
   frontdoor.change(Closed)
   frontdoor.change(Open)
   frontdoor.change(Locked)
   frontdoor.change(Closed)
   frontdoor.change(Locked)