class Base:
    def __init__(self, name, player_symbol):
        self.name = name
        self.player_symbol = player_symbol

    def print_board(self):
        print(f"Coming from the base {self.name}, {self.player_symbol}")
