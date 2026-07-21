import random


class MatchService:

    def __init__(self):
        pass


    def team_strength(self, club):

        if not club.players:
            return 50

        total = 0

        for player in club.players:

            player_rating = (
                player.overall
                + player.form / 10
                + player.fitness / 20
            )

            total += player_rating

        return total / len(club.players)


    def choose_scorer(self, club):

        if not club.players:
            return "Unknown Player"

        attackers = [
            player for player in club.players
            if player.position in ["ST", "RW", "LW", "CAM"]
        ]

        if attackers:
            return random.choice(attackers).name

        return random.choice(club.players).name


    def play_match(self, home_club, away_club):

        home_power = self.team_strength(home_club)
        away_power = self.team_strength(away_club)

        # Home advantage
        home_power += 5


        home_goals = max(
            0,
            int(random.gauss(
                home_power / 35,
                1
            ))
        )

        away_goals = max(
            0,
            int(random.gauss(
                away_power / 35,
                1
            ))
        )


        home_scorers = []
        away_scorers = []


        for _ in range(home_goals):

            scorer = self.choose_scorer(home_club)

            home_scorers.append(scorer)


            for player in home_club.players:

                if player.name == scorer:

                    player.score_goal()


        for _ in range(away_goals):

            scorer = self.choose_scorer(away_club)

            away_scorers.append(scorer)


            for player in away_club.players:

                if player.name == scorer:

                    player.score_goal()


        if home_goals > away_goals:

            winner = home_club.name

            home_club.budget += 3000000


        elif away_goals > home_goals:

            winner = away_club.name

            away_club.budget += 3000000


        else:

            winner = "Draw"

            home_club.budget += 1000000
            away_club.budget += 1000000



        return {

            "result":
                f"{home_club.name} {home_goals}-{away_goals} {away_club.name}",

            "winner": winner,

            "home_scorers": home_scorers,

            "away_scorers": away_scorers,

            "money": 3000000
        }
