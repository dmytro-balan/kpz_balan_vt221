from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Netbook(ABC):
    @abstractmethod
    def display_info(self):
        pass

class EBook(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def display_info(self):
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass

    @abstractmethod
    def create_netbook(self) -> Netbook:
        pass

    @abstractmethod
    def create_ebook(self) -> EBook:
        pass

    @abstractmethod
    def create_smartphone(self) -> Smartphone:
        pass

# Конкретні класи для фабрик
class TechFactory(AbstractFactory):
    def create_laptop(self) -> Laptop:
        return IProneLaptop()

    def create_netbook(self) -> Netbook:
        return XiaomiNetbook()

    def create_ebook(self) -> EBook:
        return BalaxyEBook()

    def create_smartphone(self) -> Smartphone:
        return IPhoneSmartphone()

# Конкретні класи пристроїв
class IProneLaptop(Laptop):
    def display_info(self):
        print("This is an IPhone laptop")

class IPhoneNetbook(Netbook):
    def display_info(self):
        print("This is an IPhone netbook")

class IPhoneEBook(EBook):
    def display_info(self):
        print("This is an IPhone ebook")

class IPhoneSmartphone(Smartphone):
    def display_info(self):
        print("This is an IPhone smartphone")

class XiaomiLaptop(Laptop):
    def display_info(self):
        print("This is a Xiaomi laptop")

class XiaomiNetbook(Netbook):
    def display_info(self):
        print("This is a Xiaomi netbook")

class XiaomiEBook(EBook):
    def display_info(self):
        print("This is a Xiaomi ebook")

class XiaomiSmartphone(Smartphone):
    def display_info(self):
        print("This is a Xiaomi smartphone")

class BalaxyLaptop(Laptop):
    def display_info(self):
        print("This is a Balaxy laptop")

class BalaxyNetbook(Netbook):
    def display_info(self):
        print("This is a Balaxy netbook")

class BalaxyEBook(EBook):
    def display_info(self):
        print("This is a Balaxy ebook")

class BalaxySmartphone(Smartphone):
    def display_info(self):
        print("This is a Balaxy smartphone")

factory = TechFactory()

laptop1 = factory.create_laptop()
laptop1.display_info()

netbook1 = factory.create_netbook()
netbook1.display_info()

ebook1 = factory.create_ebook()
ebook1.display_info()

smartphone1 = factory.create_smartphone()
smartphone1.display_info()
