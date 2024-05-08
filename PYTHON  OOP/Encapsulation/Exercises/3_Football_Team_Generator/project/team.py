from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def _find_player_by_name(self, name):
        player = None
        for p in self.__players:
            if name == p.name:
                player = p
                break
        return player

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        player = self._find_player_by_name(player_name)
        if not player:
            return f"Player {player_name} not found"
        self.__players.remove(player)
        return player



