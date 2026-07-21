class TransferService:

    def __init__(self):
        pass


    def buy_player(self, buying_club, player):

        if player in buying_club.players:
            return False, "Player already in squad"


        if buying_club.budget < player.value:
            return False, "Not enough money"


        buying_club.budget -= player.value

        buying_club.add_player(player)

        return True, f"{player.name} signed for {buying_club.name}!"


    def sell_player(self, club, player):

        if player not in club.players:
            return False, "Player is not in squad"


        club.players.remove(player)

        club.budget += player.value

        return True, f"{player.name} sold for ${player.value:,}!"
