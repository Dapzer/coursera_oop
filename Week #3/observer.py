class ObservableEngine(Engine):
    def __init__(self):
         self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achive:dict):
        for subscriber in self.__subscribers:
            subscriber.update(achive)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achive:dict):
        self.achievements.add(achive['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achive:dict):
        if achive not in self.achievements:
            self.achievements.append(achive)
