import json


class SaveService:


    def save_game(self, game):

        data = {

            "club": game.club.name
            if game.club else None,

            "budget":
            game.club.budget
            if game.club else 0,

            "week":
            game.season.current_week,


            "points":
            game.club.points
            if game.club else 0,


            "players":

            [
                player.name
                for player in game.club.players
            ]
            if game.club else []

        }


        with open(
            "save.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )



    def load_game(self, game):

        try:

            with open(
                "save.json",
                "r"
            ) as file:

                data = json.load(file)


        except:

            return False



        if data["club"]:

            game.choose_club(
                data["club"]
            )


            game.club.budget = (
                data["budget"]
            )


            game.club.points = (
                data["points"]
            )


            game.season.current_week = (
                data["week"]
            )


        return True
