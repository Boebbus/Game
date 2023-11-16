from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def use(self):
        pass


class Schwert(Item):
    def use(self):
        print("Zing!!!")


class GoldenesSchwert(Item):
    def use(self):
        print("Zing!! Zing!!")


class MegaBoom(Item):
    def use(self):
        print("WUUUUUNNNSCH!!!!!!")


class Bogen(Item):
    def use(self):
        print("Fffffffff Zack!")


class Ritter:
    def __init__(self, name: str):
        self.name = name
        self.item = None

    def pickupItem(self, item: Item):
        self.item = item
        print(f"Ich nehme auf {item}")

    def useItem(self):
        if self.item != None:
            self.item.use()
        else:
            print("Ich trage gerade kein Item")


schwert = Schwert()
bogen = Bogen()
kunibert = Ritter("Kunibert")
kunibert.pickupItem(bogen)
kunibert.useItem()
