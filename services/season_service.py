class SeasonService:

    def __init__(self):

        self.current_week = 1
        self.max_weeks = 20

        self.finished = False
        self.champion = None



    def next_week(self):

        self.current_week += 1


        if self.current_week > self.max_weeks:

            self.finished = True



    def finish_season(self, clubs):

        if not clubs:
            return None


        winner = max(
            clubs,
            key=lambda club: club.points
        )


        winner.trophies.append(
            "League Champion"
        )


        self.champion = winner.name


        return winner



    def reset(self):

        self.current_week = 1
        self.finished = False
        self.champion = None
