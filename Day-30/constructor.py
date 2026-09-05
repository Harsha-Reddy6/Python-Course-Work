'''class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30
    @classmethod
    def display(cls):
        print(cls.products)
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name}, Welcome to the Flipkart")
    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on,grab the products..")
harsha=Flipkart()
harsha.userinfo('harsha',2345678876,'hyd')
harsha.displaydiscount()
harsha.display()
Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)
'''
'''varsha=Flipkart()
varsha.userinfo('varsha',2345678876,'ong')
varsha.displaydiscount()
varsha.display()
harshi=Flipkart()
harshi.userinfo('harshi',2345678876,'knl')
harshi.displaydiscount()
harshi.display()'''

class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"Hello {self.name}, Welcome to the Flipkart")
harsha=Flipkart('harsha',2345678876)
varsha=Flipkart('varsha',2345678876)
harshi=Flipkart('harshi',2345678876)



