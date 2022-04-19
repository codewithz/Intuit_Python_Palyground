class Product:
    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        print("Set Price invoked")
        if (value<=0):
            raise ValueError("Price of the product cannot be zero or less")
        else:
            self.__price=value

    def get_price(self):
        print("Get Price invoked")
        return  self.__price;

    def __str__(self):
        return f"Product Name:{self.name} || Price : {self.__price}"

    price=property(get_price,set_price);

# -------------------------------------------------------
print('--------------------- pr1 ------------------------')
try:
    pr1=Product("Earphones",-400)
    print(pr1)
    pr1.price=-500
    print(pr1.price)
except ValueError as ex:
    print(ex)
# print(pr1.__price)
# 'Product' object has no attribute '__price'
print("--------------------- pr2 ----------------------")
pr2=Product("Keyboard",700)
print(pr2)