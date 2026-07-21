class FinanceService:
    def __init__(self):
        pass

    def add_money(self, club, amount):
        club.budget += amount

    def remove_money(self, club, amount):
        if club.budget >= amount:
            club.budget -= amount
            return True
        return False
