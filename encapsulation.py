class Tree:
   def __init__(self, height):
       self.height = height

pine = Tree(20)
print(pine.height)


# using protected member ->preciding single underscore 
class Tree:
   def __init__(self, height):
       self._height = height

pine = Tree(20)
pine._height


# using private  member ->preciding double underscore 
class Tree:
   def __init__(self, height):
       self.__height = height


pine = Tree(20)
pine.__height

# if someone wants to aceess the attribute 
class Tree:
   def __init__(self, height):
       self.__height = height

   def get_height(self):
       return self.__height

   def set_height(self, new_height):
       if not isinstance(new_height, int):
           raise TypeError("Tree height must be an integer")
       if 0 < new_height <= 40:
           self.__height = new_height
       else:
           raise ValueError("Invalid height for a pine tree")


pine = Tree(20)
pine.get_height()
  

# Using @property decorator 
class Tree:
   def __init__(self, height):
       # First, create a private or protected attribute
       self.__height = height

   @property
   def height(self):
       return self.__height

pine = Tree(17)
pine.height
