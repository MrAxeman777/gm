import json

from services.finance_service import FinanceService
from services.transfer_service import TransferService
from services.match_service import MatchService
from services.season_service import SeasonService

from models.club import Club
from models.player import Player


class GameEngine:

    def __init__(self):

        self.finance = FinanceService()
        self.transfer = TransferService()
        self.match = MatchService()
        self.season = SeasonService()

        self.available_players = self.load_players()
        self.available_clubs = self.load_clubs()

        self.club = None


    def load_players(self):

        with open("data/players.json", "r") as file:
            data = json.load(file)

        players = []

        for p in data:

            player = Player(
                name=p["name"],
                age=p["age"],
                position=p["position"],
                overall=p["overall"],
                potential=p["potential"],
                value=p["value"],
                wage=p["wage"],
                pace=p["pace"],
                shooting=p["shooting"],
                passing=p["passing"],
                dribbling=p["dribbling"],
                defending=p["defending"],
                physical=p["physical"]
            )

            players.append(player)

        return players


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


            for player_name in c.get("players", []):

                for player in self.available_players:

                    if player.name == player_name:

                        club.add_player(player)


            clubs.append(club)

        return clubs


    def choose_club(self, club_name):

        for club in self.available_clubs:

            if club.name == club_name:

                self.club = club
                return True

        return False


    def play_match(self):

        result = self.match.play_match(
            self.club,
            self.club
        )

        self.season.next_week()

        return result
