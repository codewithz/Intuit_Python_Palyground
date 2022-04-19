from abc import  ABC,abstractmethod

# abc --> abstract base class
# abc.ABC --> Abstract Base Class
# abc.@abstractmethod --> when we need to make a method abstract

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass


# -----------------------------------------------------------

class HondaCity(Car):
    def start(self):
        print("Start of Honda City")

    def stop(self):
        print("Stop of Honda City")

# ------------------------------------------------------------

h=HondaCity()
h.start()
h.stop()
