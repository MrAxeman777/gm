class Player:

    def __init__(
        self,
        name,
        age,
        position,
        overall,
        potential,
        value,
        wage,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physical
    ):

        self.name = name
        self.age = age
        self.position = position

        self.overall = overall
        self.potential = potential

        self.value = value
        self.wage = wage

        # Player attributes
        self.pace = pace
        self.shooting = shooting
        self.passing = passing
        self.dribbling = dribbling
        self.defending = defending
        self.physical = physical

        # Career stats
        self.matches = 0
        self.goals = 0
        self.assists = 0

        # Development
        self.form = 75
        self.fitness = 100
        self.morale = 75


    def play_match(self):
        self.matches += 1


    def score_goal(self):
        self.goals += 1


    def assist_goal(self):
        self.assists += 1


    def improve(self):

        if self.age <= 23 and self.overall < self.potential:
            self.overall += 1


    def get_market_value(self):

        return self.value
