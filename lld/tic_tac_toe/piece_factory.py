from piece import PieceO, PieceX


class FactoryPiece:
    @staticmethod
    def create_piece(symbol):
        if symbol == "X":
            return PieceX()
        elif symbol == "O":
            return PieceO()
        else:
            raise ValueError("No symbol found")
