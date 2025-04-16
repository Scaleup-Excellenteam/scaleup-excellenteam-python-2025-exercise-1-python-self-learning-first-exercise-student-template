import random
from typing import List, Optional


class Player:
    MAX_HP = 100

    def __init__(self, name: str) -> None:
        self.name = name
        self.hp = Player.MAX_HP
        self.exp = 0.0
        self.level = 1
        self.nemeses: List[Player] = []
        self._revive_count = 0

    def is_mostly_dead(self) -> bool:
        return self.hp <= 0 and self._revive_count < 2

    def is_completely_dead(self) -> bool:
        return self._revive_count >= 2

    def attack(self, target: Optional['Player'] = None) -> bool:
        if target is None:
            if not self.nemeses:
                return False
            target = self.nemeses[-1]

        damage = random.randint(self.level * 5, self.level * 20)
        target.hp -= damage

        if target.hp <= 0:
            if not target.is_completely_dead():
                target._revive_count += 1
                target.revive()
                target.nemeses.append(self)
                self.exp += self.calculate_exp_gain(target)
                self.update_level()
            else:
                self.exp += 2 * self.calculate_exp_gain(target)
                self.update_level()
        return True

    def calculate_exp_gain(self, rival: 'Player') -> float:
        lr = rival.level
        lp = self.level
        return (lr * (2 * lr + 10) ** 2.5) / (5 * (lr + lp + 10) ** 2.5)

    @staticmethod
    def exp_needed_for_level(level: int) -> float:
        return (4 * (level - 1) ** 2.5) / 5

    def update_level(self) -> None:
        while self.exp >= self.exp_needed_for_level(self.level + 1):
            self.level += 1

    def revive(self) -> bool:
        if self.is_completely_dead():
            return False
        self.hp = Player.MAX_HP
        return True

    def __repr__(self) -> str:
        return f"{self.name} (Lvl {self.level}, HP {self.hp}, EXP {round(self.exp)})"


class Arena:
    def __init__(self, max_players: int) -> None:
        self.max_players = max_players
        self.players: List[Player] = []
        self._next_index = 0
        self.fight_started = False
        self.winner: Optional[Player] = None
        self.next_player: Optional[Player] = None

    def hajime(self) -> None:
        self.fight_started = True
        self.update_next_player()

    def get_players(self) -> List[Player]:
        return self.players

    def add_player(self, player: Player) -> bool:
        if self.fight_started or player in self.players or len(self.players) >= self.max_players:
            return False
        self.players.append(player)
        self.update_next_player()
        return True

    def remove_player(self, player: Player) -> bool:
        if self.fight_started or player not in self.players:
            return False
        self.players.remove(player)
        self.update_next_player()
        return True

    def update_next_player(self) -> None:
        alive_players = [pl for pl in self.players if not pl.is_completely_dead()]
        self.next_player = alive_players[0] if alive_players else None

    def make_move(self) -> None:
        if not self.next_player or self.next_player.is_completely_dead():
            self.update_next_player()
            return

        player = self.next_player

        if player.is_mostly_dead():
            if player.revive():
                player.attack()
                self.advance_turn()
                return

        print(f"{player.name} is taking a turn... (HP={player.hp}, Level={player.level})")

        acted = player.attack()

        if not acted:
            alive_enemies = [pl for pl in self.players if pl != player and not pl.is_completely_dead()]
            if alive_enemies:
                target = random.choice(alive_enemies)
                player.attack(target)

        self.advance_turn()

        alive_players = [pl for pl in self.players if not pl.is_completely_dead()]
        if len(alive_players) == 1:
            self.winner = alive_players[0]

    def advance_turn(self) -> None:
        alive_players = [pl for pl in self.players if not pl.is_completely_dead()]
        if not alive_players:
            self.next_player = None
            return

        if self.next_player not in alive_players:
            self._next_index = 0
        else:
            self._next_index = (alive_players.index(self.next_player) + 1) % len(alive_players)

        self.next_player = alive_players[self._next_index]


if __name__ == '__main__':
    arena = Arena(4)
    player_names = ['Ash', 'Misty', 'Brock', 'Gary']
    fighters = [Player(name) for name in player_names]

    for fighter in fighters:
        arena.add_player(fighter)

    arena.hajime()

    round_counter = 0
    while arena.winner is None:
        arena.make_move()
        round_counter += 1

        if round_counter % 10 == 0:
            print(f"\n--- Round {round_counter} ---")

        if round_counter > 500:
            print("Too many rounds – stopping simulation.")
            break

    print(f"\nWinner after {round_counter} rounds:", arena.winner)
