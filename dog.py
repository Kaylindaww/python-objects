class Dog:
       def __init__(self,name,age,gender,breed) :
         self.name=name
         self.age=age
         self.gender=gender
         self.breed=breed
       def protect(self):
           
          return f"I have a {self.gender} dog called {self.name}, {self.age} years old and it is {self.breed} "

       def barks(self):

         return f"My {self.gender} ,{self.breed} dog called {self.name} is now {self.age} years old."       
           
