import random


class MatchService:
    def __init__(self):
        pass

    def play_match(self, home_club, away_club):
        # Simple strength calculation
        home_strength = sum(player.rating for player in home_club.players)
        away_strength = sum(player.rating for player in away_club.players)

        # Home advantage
        home_strength += 10

        # Generate goals
        home_goals = random.randint(0, max(1, home_strength // 100))
        away_goals = random.randint(0, max(1, away_strength // 100))

        # Prize money
        if home_goals > away_goals:
            home_club.budget += 3_000_000
            winner = home_club.name
        elif away_goals > home_goals:
            away_club.budget += 3_000_000
            winner = away_club.name
        else:
            home_club.budget += 1_000_000
            away_club.budget += 1_000_000
            winner = "Draw"

        return {
            "home_team": home_club.name,
            "away_team": away_club.name,
            "home_goals": home_goals,
            "away_goals": away_goals,
            "winner": winner
        }
