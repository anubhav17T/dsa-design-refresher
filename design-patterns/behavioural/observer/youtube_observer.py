"""CREATE SUBJECT"""
from abc import ABC, abstractmethod


class YoutubeChannel:

    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.subscribers = []

    def add_subscriber(self, subscribers):
        self.subscribers.append(subscribers)

    def remove_subscriber(self, subscribers):
        self.subscribers.remove(subscribers)

    def notify(self):
        print("---Sending Notifications to all subscribers---")
        for subs in self.subscribers:
            subs.update()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class EmailObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print("Sending email to {} ".format(self.name))


class SMSObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print("Sending sms to {}".format(self.name))


if __name__ == "__main__":
    channel = YoutubeChannel(channel_name="Techno")
    sub1 = EmailObserver(name="Anubhav")
    sub2 = SMSObserver(name="Swati")
    channel.add_subscriber(sub1)
    channel.add_subscriber(sub2)
    channel.notify()