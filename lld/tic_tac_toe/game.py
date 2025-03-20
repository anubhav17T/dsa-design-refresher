from board import Board
from player import Player


class Game:
    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player = 0


    def switch_player(self):
        self.current_player = (self.current_player+1) % len(self.players)

    def start(self):
        while True:
            self.board.display()
            player = self.players[self.current_player]

            # Ask player for their move
            try:
                row, col = map(int, input(
                    f"{player.name} ({player.get_symbol()}) - Enter row and col (0-{self.board.size - 1}): ").split())
            except ValueError:
                print("Invalid input! Enter two numbers separated by space.")
                continue

            # Make the move if it's valid
            if self.board.make_move(row, col, player.get_symbol()):
                # Check if the player won
                if self.board.check_winner(player.get_symbol()):
                    self.board.display()
                    print(f"🎉 {player.name} wins! 🎉")
                    break

                # Check if the game is a draw
                elif self.board.is_draw():
                    self.board.display()
                    print("🤝 It's a draw! 🤝")
                    break

                # Switch to the next player
                self.switch_player()
            else:
                print("❌ Invalid move! Try again.")


# Start the game
game = Game()
game.start()
