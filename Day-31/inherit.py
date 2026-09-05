#single inheritance
'''class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and vedio calls")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()'''
#multilevel inheritance
'''class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and vedio calls")

class whatsappv3(whatsappv2):
    def status(self):
        print("you can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status()
'''
#multiple inheritance
'''class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def calls(self):
        print("you can audio and vedio calls")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        print("you can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status()
'''
#hierarchy inheritance
'''class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and vedio calls")

class whatsappv3(whatsappv1):
    def status(self):
        print("you can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.status()
'''
#hybrid inheritance  
#[multiple,multilevel]
'''class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def extramessage(self):
        print("you can add emojis,stickers and gifs")

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("you can audio and vedio calls")

class whatsappv4(whatsappv3):
    def status(self):
        print("you can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extramessage()

c=whatsappv3()
c.messaging()
c.extramessage()
c.calls()

d=whatsappv4()
d.messaging()
d.extramessage()
d.calls()
d.status()'''

#super()-in multilevel
'''class whatsappv1:
    def status(self):
        print("you can add images and vedios")
class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can add music and stickers")
class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("you can like and you can  add reaction")
a=whatsappv3()
a.status()'''
#super() does not works in multiple inheritance, we want to access the properties by using a classname
'''class whatsappv1:
    def status(self):
        print("you can add images and vedios")
class whatsappv2:
    def status(self):
        print("you can add music and stickers")
class whatsappv3(whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can like and you can  add reaction")
a=whatsappv3()
a.status()'''
