import os
from datetime import date


class WordService:
    def __init__(self):
        self.words_file_path = os.path.join(os.path.dirname(__file__), "../data/words.txt")
        self.word_of_the_day_file_path = os.path.join(os.path.dirname(__file__), "../data/word_of_the_day.txt")

    def get_words(self):
        with open(self.words_file_path, "r") as file:
            words = file.read().splitlines()
        return words

    def get_word_for_today(self):
        today = date.today()

        if os.path.exists(self.word_of_the_day_file_path):
            with open(self.word_of_the_day_file_path, "r") as file:
                saved_date, saved_word = file.read().split(",")
                if saved_date == today.isoformat():
                    return saved_word

        words = self.get_words()
        day_of_year = today.timetuple().tm_yday
        word_for_today = words[day_of_year % len(words)]

        with open(self.word_of_the_day_file_path, "w") as file:
            file.write(f"{today.isoformat()},{word_for_today}")

        return word_for_today
