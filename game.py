import random

from game_display import hangman
from words import random_word
from exceptions import input_checker

words = random_word()


class Base:
    def __init__(self, word, mistakes=0, letter=None, hangman=hangman[0]):
        self.word = word.lower()
        self.mistakes = mistakes
        self.letter = letter
        self.hangman = hangman
        self.word_display = ['_' for i in range(len(self.word))]

    def display(self):
        print(f'Слово: {" ".join(self.word_display)}')
        print(f'Ошибок: {self.mistakes}')
        print(self.hangman)


# основная игра - "тяжелый" уровень
class Game(Base):
    def game_game(self):
        self.display()
        while True:
            gamer_answer = input_checker('Введите одну букву: ')

            count = self.word.count(gamer_answer)

            if count > 1:
                p = [i for i, ltr in enumerate(self.word) if ltr == gamer_answer]
                for i in p:
                    self.word_display[i] = gamer_answer
                self.letter = gamer_answer
                self.display()
            elif count == 1:
                index_word = self.word.find(gamer_answer)
                self.word_display[index_word] = gamer_answer
                self.letter = gamer_answer
                self.display()
            else:
                self.mistakes += 1
                self.hangman = hangman[self.mistakes]
                self.letter = gamer_answer
                self.display()
                if self.mistakes == 6:
                    print('Вы проиграли :(')
                    print(hangman[7])
                    show_answer = input('Хотите увидеть неотгаданное слово? [Да/Нет]').lower()
                    if show_answer == 'да':
                        print(self.word)
                        start_again()
                    else:
                        start_again()

                    return False

            if self.word_display == [i for i in self.word]:
                print('Вы победили!')
                start_again()
                return False


# легкий уровень
class EasyGame(Game):
    def game_game(self):
        word_length = len(self.word)

        if word_length <= 5:
            index = random.choice(range(word_length))
            self.word_display[index] = self.word[index]
        elif word_length > 5:
            for _ in range(2):
                index = random.choice(range(word_length))
                self.word_display[index] = self.word[index]

        super().game_game()


def start_again():
    again_answer = input('Хотите поиграть еще раз? [Да/Нет]').lower()
    if again_answer == 'да':
        start_game()
    else:
        print('Спасибо за игру, пока!')


def start_game():
    print('Игра "Виселица"')
    print('Легкий уровень: некоторые буквы известны заранее')
    print('Тяжелый уровень: все буквы неизвестны')
    level_choice = input('Выберите уровень: [Легкий/Тяжелый]').lower()

    if level_choice == 'тяжелый':
        game = Game(words)
        game.game_game()
    elif level_choice == 'легкий':
        game = EasyGame(words)
        game.game_game()


if __name__ == '__main__':
    start_game()
