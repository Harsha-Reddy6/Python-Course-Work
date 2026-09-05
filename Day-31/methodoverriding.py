class Hotstar:
    def __init__(self,name):
        print(f" Welcome to the hotstsar,{name}")
    def login(self):
        print("you can login to the hotstar")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def palycontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("you can see the recent vedio")
    def ads(self):
        print("ads will run")
    def quality(self):
        print("quality is low")
    def access(self):
        print(" you have limited access")
    def download(self):
        print("you can't download the vedio with high quality")
class premiumhotstar(Hotstar):
    def ads(self):
        print("ads will not run")
    def quality(self):
        print("quality is high")
    def access(self):
        print(" you have unlimited access")
    def download(self):
        print("you can download the vedio with high quality")
harsha=Hotstar("harsha")
harsha.login()
harsha.dashboard()
harsha.search()
harsha.palycontrollers()
harsha.history()
harsha.ads()
harsha.quality()
harsha.access()
harsha.download()

varsha=premiumhotstar("varsha")
varsha.login()
varsha.dashboard()
varsha.search()
varsha.palycontrollers()
varsha.history()
varsha.ads()
varsha.quality()
varsha.access()
varsha.download()