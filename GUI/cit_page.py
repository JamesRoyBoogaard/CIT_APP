from abc import ABC, abstractmethod

class CITPage(ABC):

    @abstractmethod
    def previous_page(self):
        pass

    @abstractmethod
    def home_page(self):
        pass
