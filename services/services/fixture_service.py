import random


class FixtureService:

    def __init__(self):
        self.fixtures = []


    def generate_fixtures(self, clubs):

        self.fixtures = []

        for i in range(len(clubs)):

            for j in range(i + 1, len(clubs)):

                self.fixtures.append(
                    {
                        "home": clubs[i],
                        "away": clubs[j],
                        "played": False
                    }
                )

                self.fixtures.append(
                    {
                        "home": clubs[j],
                        "away": clubs[i],
                        "played": False
                    }
                )


        random.shuffle(self.fixtures)

        return self.fixtures


    def get_next_match(self, club):

        for match in self.fixtures:

            if not match["played"]:

                if (
                    match["home"] == club
                    or match["away"] == club
                ):

                    return match

        return None
