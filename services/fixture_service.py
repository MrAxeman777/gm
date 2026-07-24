import random


class FixtureService:

    def __init__(self):
        self.fixtures = []


    def generate_fixtures(self, clubs):

        self.fixtures = []

        for i in range(len(clubs)):
            for j in range(i + 1, len(clubs)):

                self.fixtures.append({
                    "home": clubs[i],
                    "away": clubs[j],
                    "played": False
                })

                self.fixtures.append({
                    "home": clubs[j],
                    "away": clubs[i],
                    "played": False
                })

        random.shuffle(self.fixtures)

        return self.fixtures


    def get_next_match(self, club):

        for fixture in self.fixtures:

            if not fixture["played"]:

                if (
                    fixture["home"] == club
                    or fixture["away"] == club
                ):
                    return fixture

        return None
