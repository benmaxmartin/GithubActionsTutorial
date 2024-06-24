class Dummy(object):
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name  

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self.__name = value
        else:
            raise ValueError("name can only be a string")

if __name__ == "__main__":
    obj = Dummy(name="Abir")
    print(obj.name)
    obj.name = "Sankhadip"
    print(obj.name)