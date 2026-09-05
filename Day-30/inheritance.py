#single inheritance
class whatsappv1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp -v1 {self.name}")
    def messaging(self):
        print("You can send messages")

class whatsappv2(whatsappv1):
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp -v2 {self.name}")
    def calls(self):
        print("You can do audio and vedio calls")
         
harsha=whatsappv1('harsha')
harsha.messaging()
varsha=whatsappv2('varsha')
varsha.messaging()
varsha.calls()