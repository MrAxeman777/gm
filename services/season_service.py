class SeasonService:
    def __init__(self):
        self.current_season = "2026/27"
        self.current_week = 1

    def next_week(self):
        self.current_week += 1

        if self.current_week > 38:
            self.current_week = 1
            self.advance_season()

    def advance_season(self):
        start_year = int(self.current_season[:4])
        end_year = start_year + 2

        self.current_season = f"{start_year + 1}/{str(end_year)[2:]}"
