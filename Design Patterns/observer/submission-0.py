class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observers = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def updateStock(self, newStock: int) -> None:
        oldStock = self.stock
        self.stock = newStock
        if oldStock == 0 and newStock > 0:
            for o in self.observers:
                o.notify(self.itemName)
