class TransferService:
    def __init__(self):
        pass

    def buy_player(self, buying_club, selling_club, player):
        if buying_club.budget < player.value:
            return False, "Not enough money."

        # Transfer money
        buying_club.budget -= player.value
        selling_club.budget += player.value

        # Move player
        if player in selling_club.players:
            selling_club.players.remove(player)

        buying_club.players.append(player)

        return True, f"{player.name} has signed for {buying_club.name}!"
