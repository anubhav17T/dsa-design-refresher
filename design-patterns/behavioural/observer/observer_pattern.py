""" STEP 1 - Define the Subject and its methods"""
from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self.observers = []

    def detach(self, observer):
        self.observers.remove(observer)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


"""STEP 2 :- Methods for receiving updates"""


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


""" STEP 3:- Concrete Method """


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print("{} has been notified".format(self.name))


if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver("Ram")
    observer2 = ConcreteObserver("Shyam")
    observer3 = ConcreteObserver("Mohan")

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    subject.notify()

