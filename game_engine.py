import json

from services.finance_service import FinanceService
from services.transfer_service import TransferService
from services.match_service import MatchService
from services.season_service import SeasonService

from models.club import Club


class GameEngine:

    def __init__(self):

        self.finance = FinanceService()
        self.transfer = TransferService()
        self.match = MatchService()
        self.season = SeasonService()

        self.available_clubs = self.load_clubs()

        self.club = None


    def load_clubs(self):

        with open("data/clubs.json", "r") as file:
            data = json.load(file)

        clubs = []

        for c in data:
            club = Club(
                name=c["name"],
                league=c["league"],
                budget=c["budget"],
                wage_budget=c["wage_budget"],
                reputation=c["reputation"]
            )

            clubs.append(club)

        return clubs


    def choose_club(self, club_name):

        for club in self.available_clubs:

            if club.name == club_name:
                self.club = club
                return True

        return False


    def play_match(self):

        self.club.budget += 3000000

        self.season.next_week()

        return {
            "result": "Match completed!",
            "money": 3000000,
            "week": self.season.current_week
        }
