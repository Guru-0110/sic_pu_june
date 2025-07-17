#  A class is said to be a singleton class if there is only one object that can be created through out the class 
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance
    
obj1 = Singleton()
obj2 = Singleton()
print(obj1==obj2)