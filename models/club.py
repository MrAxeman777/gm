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

        # Club upgrades
        self.stadium_level = 1
        self.training_level = 1
        self.youth_level = 1

        # Season stats
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

        self.goals_for = 0
        self.goals_against = 0
        self.points = 0


    def add_player(self, player):

        self.players.append(player)


    def remove_player(self, player):

        if player in self.players:
            self.players.remove(player)


    def squad_rating(self):

        if not self.players:
            return 0

        total = sum(
            player.overall
            for player in self.players
        )

        return round(
            total / len(self.players)
        )


    def record_match(
        self,
        goals_scored,
        goals_conceded
    ):

        self.matches += 1

        self.goals_for += goals_scored

        self.goals_against += goals_conceded


        if goals_scored > goals_conceded:

            self.wins += 1
            self.points += 3


        elif goals_scored == goals_conceded:

            self.draws += 1
            self.points += 1


        else:

            self.losses += 1
