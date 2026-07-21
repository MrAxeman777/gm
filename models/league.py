class League:
    def __init__(self, name):
        self.name = name
        self.clubs = []

    def add_club(self, club):
        self.clubs.append(club)

    def standings(self):
        return sorted(
            self.clubs,
            key=lambda club: club.squad_rating(),
            reverse=True
        )
