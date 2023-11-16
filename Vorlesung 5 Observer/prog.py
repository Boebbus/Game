from __future__ import annotations
from abc import abstractmethod, ABC

class Observer(ABC):
    @abstractmethod
    def notification():
        pass

class Observable:
    def __init__(self):
        self.observers = []

    def register(self, follower):
        if follower not in self.observers:
            self.observers.append(follower)

    def unregister(self, follower):
        if follower in self.observers:
            self.observers.remove(follower)

    def notify(self):
        for follower in self.observers:
            follower.notification(self)

class InstaAccount(Observer, Observable):
    def __init__(self, username: str):
        Observable.__init__(self)
        self.profilbild = None
        self.username = username
        self.status = "privat"
        self.posts = []

    def show_follower(self):
        for follower in self.observers:
            print(f"{follower.username} folgt {self.username}")

    def notification(self, observable: InstaAccount):
        print(f"Ich {self.username} habe eine Nachricht von {observable.username} erhalten:")
        observable.show_last_post()

    def post(self, message: str):
        self.posts.append(message)
        self.notify()

    def show_last_post(self):
        print(f"{self.username}: {self.posts[-1]}")

sebi = InstaAccount("Sebastian")
martin = InstaAccount("Martin")
lisa = InstaAccount("Lisa")

lisa.register(sebi)
lisa.register(martin)
lisa.show_follower()

sebi.post("Hurra - ich bin bei Insta!")
sebi.post("Sitze gerade in einer langweiligen Vorlesung.")

lisa.post("Mal ausprobieren, was die App so kann...")
lisa.unregister(martin)
lisa.post("Ich sollte vorne die Vorlesung machen. Oh mann oh mann.")


