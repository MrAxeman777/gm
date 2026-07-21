from services.finance_service import FinanceService
from services.transfer_service import TransferService
from services.match_service import MatchService
from services.season_service import SeasonService


class GameEngine:
    def __init__(self):
        self.club = None
        self.current_week = 1
        self.current_season = "2026/27"

        self.finance = FinanceService()
        self.transfer = TransferService()
        self.match = MatchService()
        self.season = SeasonService()

    def choose_club(self, club):
        self.club = club

    def next_week(self):
        self.current_week += 1
