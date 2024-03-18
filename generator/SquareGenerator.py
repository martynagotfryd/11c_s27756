#3 and 5 and 10

from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def generate_squares(self, start, end):
        pass

