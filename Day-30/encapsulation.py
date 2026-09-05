'''class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]

    def getpassword(self):
        return self.__password
    
    @property
    def accesspost(self):
        return self._post
    def display(self):
        print(self.username,self.__password,self._post)
harsha=Instagram('harsha','harsha@123')
harsha.display()
print(harsha.username)
print(harsha.getpassword())
print(harsha.accesspost)
'''
#update
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._post=[]

    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
    
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

    def display(self):
        print(self.username,self.__password,self._post)
harsha=Instagram('harsha','harsha@123')
harsha.display()
print(harsha.username)
print(harsha.getpassword())
print(harsha.accesspost)

harsha.username='varsha'
harsha.setpassword('varsha@123')
harsha.accesspost="Sunrise.png"
harsha.accesspost="Sunset.png"
harsha.accesspost="sunshines.png"

print(harsha.username)
print(harsha.getpassword())
print(harsha.accesspost)