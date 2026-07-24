import json


class SaveService:

    def save_game(self, game):

        if game.club is None:
            return

        data = {
            "club": game.club.name,
            "budget": game.club.budget,
            "points": game.club.points,
            "week": game.season.current_week
        }

        with open("save.json", "w") as file:
            json.dump(data, file, indent=4)


    def load_game(self, game):

        try:
            with open("save.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return False

        game.choose_club(data["club"])

        game.club.budget = data["budget"]
        game.club.points = data["points"]
        game.season.current_week = data["week"]

        return True
