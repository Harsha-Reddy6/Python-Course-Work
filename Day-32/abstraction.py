from abc import ABC,abstractmethod
class phonepay(ABC):
    def sendinginfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("you can enter amount")
    def pin(self):
        print("you can enter the pin")
    @abstractmethod
    def transaction(self):
          pass
class HDFC(phonepay):
      def transaction(self):
        print("payment using hdfc bank")
class SBI(phonepay):
      def transaction(self):
        print("payment using sbi bank")
class UNION(phonepay):
      def transaction(self):
        print("payment using union bank")
class AXIS(phonepay):
      def transaction(self):
        print("payment using axis bank")
class ICIC(phonepay):
      def transaction(self):
        print("payment using icic bank")

harsha=HDFC()
harsha.sendinginfo()
harsha.amount()
harsha.pin()
harsha.transaction()

varsha=SBI()
varsha.sendinginfo()
varsha.amount()
varsha.pin()
varsha.transaction()

harshi=UNION()
harshi.sendinginfo()
harshi.amount()
harshi.pin()
harshi.transaction()

varshi=AXIS()
varshi.sendinginfo()
varshi.amount()
varshi.pin()
varshi.transaction()

harsh=ICIC()
harsh.sendinginfo()
harsh.amount()
harsh.pin()
harsh.transaction()