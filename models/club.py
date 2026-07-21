class Club:
    def __init__(
        self,
        name,
        league,
        budget,
        wage_budget,
        reputation
    ):
        self.name = name
        self.league = league

        self.budget = budget
        self.wage_budget = wage_budget

        self.reputation = reputation

        self.players = []

        self.manager = None

        self.trophies = []

        self.fans = 50000

        self.board_confidence = 80

        self.stadium_level = 1
        self.training_level = 1
        self.youth_level = 1
        self.medical_level = 1

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def squad_rating(self):
        if not self.players:
            return 0

        total = sum(player.overall for player in self.players)
        return round(total / len(self.players))
