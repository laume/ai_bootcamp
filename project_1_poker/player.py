class Player:

    def __init__(self, name: str, buy_in: int) -> None:
        self.chips = buy_in
        self.name = name

    def bet(self, amount: int) -> bool:
        """

        :param amount: amount player wishes to bet
        :return: True if bet was successful, False otherwise
        """
        if amount > self.chips:
            print("Sorry, your bet can't exceed", self.chips)
            return False
        else:
            self.chips -= amount
            print("{} has {} chips remaining".format(self.name, self.chips))
            return True

    def credit(self, amount: int) -> None:
        self.chips += amount
