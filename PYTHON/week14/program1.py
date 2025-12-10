# a demo of implementaion oop in python
# creating a class named shoeFactory with a few attributes and methods
# This includes creating objects(instances) of shoefactory

class shoeFactory:

    def __init__(self,type,code,quant): # initlizing attributes to values
        self.__shoesType__ = type
        self.__shoesCode__ = code # assigning the values to attributes
        self.__shoesquant__ = quant

    def description(self):
        return str(self.__shoesCode__) + ':' + self.__shoesType__ + ':' + str(self.__shoesquant__)

    def cost(self):
        unit_price = 100.99
        return round(unit_price * self.__shoesquant__,2)

    def main():
        shoes1 = shoeFactory('Ladies', 10394, 3)
        print(shoes1.description)
        print(shoes1.cost())
main()

'''
study oop slides up to slides 15
'''
