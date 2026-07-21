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

        self.club = Club(
            name="Manchester United",
            league="Premier League",
            budget=150_000_000,
            wage_budget=4_000_000,
            reputation=90
        )

    def play_match(self):

        # Temporary placeholder
        self.club.budget += 3_000_000

        self.season.next_week()

        return {
            "result": "Manchester United 2-1 Chelsea",
            "money": 3000000,
            "week": self.season.current_week
        }
