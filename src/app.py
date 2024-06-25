import os

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
    name1 = os.environ.get("NAME1")
    obj = Dummy(name=name1)
    print(obj.name)
    name2 = os.environ.get("NAME2")
    obj.name = name2
    print(obj.name)
    if obj.name not in ["Abir","Sankhadip"]:
        raise Exception("Name error")