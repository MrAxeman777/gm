import random


class MatchService:

    def __init__(self):
        pass


    def team_strength(self, club):

        if not club.players:
            return 60

        total = 0

        for player in club.players:
            total += (
                player.overall
                + player.form / 10
                + player.fitness / 20
            )

        return total / len(club.players)


    def choose_scorer(self, club):

        if not club.players:
            return None

        attackers = [
            player for player in club.players
            if player.position in ["ST", "RW", "LW", "CAM"]
        ]

        if attackers:
            return random.choice(attackers)

        return random.choice(club.players)


    def play_match(
        self,
        home_club,
        away_club
    ):

        home_power = self.team_strength(home_club) + 5
        away_power = self.team_strength(away_club)

        home_goals = max(
            0,
            int(random.gauss(home_power / 35, 1))
        )

        away_goals = max(
            0,
            int(random.gauss(away_power / 35, 1))
        )

        home_scorers = []
        away_scorers = []

        for _ in range(home_goals):

            scorer = self.choose_scorer(home_club)

            raise Exception(
                f"""
DEBUG

Scorer: {scorer}

Type: {type(scorer)}

Club Players:

{club_players(home_club)}
"""
            )

        for _ in range(away_goals):

            scorer = self.choose_scorer(away_club)

            raise Exception(
                f"""
DEBUG

Scorer: {scorer}

Type: {type(scorer)}

Club Players:

{club_players(away_club)}
"""
            )

        home_club.record_match(
            home_goals,
            away_goals
        )

        away_club.record_match(
            away_goals,
            home_goals
        )

        if home_goals > away_goals:

            home_club.budget += 3000000
            winner = home_club.name

        elif away_goals > home_goals:

            away_club.budget += 3000000
            winner = away_club.name

        else:

            home_club.budget += 1000000
            away_club.budget += 1000000
            winner = "Draw"

        return {
            "result": f"{home_club.name} {home_goals}-{away_goals} {away_club.name}",
            "winner": winner,
            "home_scorers": home_scorers,
            "away_scorers": away_scorers,
            "money": 3000000
        }


def club_players(club):

    output = []

    for player in club.players:
        output.append(
            f"{player} ({type(player)})"
        )

    return "\n".join(output)
