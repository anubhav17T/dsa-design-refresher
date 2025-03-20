from abc import ABC,abstractmethod


class Piece(ABC):
    @abstractmethod
    def get_symbol(self):
        pass


class PieceX(Piece):
    def get_symbol(self):
        return "X"


class PieceO(Piece):
    def get_symbol(self):
        return "O"


