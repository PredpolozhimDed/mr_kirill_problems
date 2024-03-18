from mimesis import Person
from mimesis.locales import Locale

from random import randint

person = Person(Locale.RU)


#  Класс Player нужен для хранения имени и значения броска
class Player:
    def __init__(self, name):
        self.name = name
        self.value = None

    def roll_dice(self):
        self.value = randint(1, 6)


def games(players):
    while len(players) > 1:
        current_player_one = players.pop(0)  # Возвращаем из списка первого игрока
        current_player_two = players[0]  # Берём из списка второго игрока
        current_player_one.roll_dice()  # инициализируем бросок кубика для игрока №1
        # current_player_two.roll_dice()  #  инициализируем бросок для второго игрока

        if current_player_one.value == current_player_two.value:
            players.pop(0)
            #  Если у текущего игрока и того, что за ним, одинаковые значение
            #  Они оба вылетают
            print(f"Игрок {current_player_one.name} и {current_player_two.name} выбывают")
        else:
            players.append(current_player_one)
            #  А если разные, то текущий игрок уходит в конец очереди (списка)

    winner = players[0]
    print(f"Победил {winner.name}")


def main():
    num_players = int(input("Введите количество игроков (нечётное): "))
    if num_players % 2 == 0:
        print("Введено четное число!")
        return

    players = []
    for i in range(num_players):
        player_name = person.name()
        player = Player(name=player_name)
        players.append(player)

    print("Начало игры")
    games(players)


if __name__ == '__main__':
    main()
