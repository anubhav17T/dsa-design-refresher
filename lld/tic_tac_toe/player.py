from piece_factory import FactoryPiece


class Player:
    def __init__(self, name, symbol_type):
        self.name = name
        self.symbol_type = FactoryPiece.create_piece(symbol=symbol_type)

    def get_symbol(self):
        return self.symbol_type.get_symbol()
