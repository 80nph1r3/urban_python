import re


class WordsFinder:
    def __init__(self, *file_names: str) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name) as file:
                contents = file.read().lower()
                contents_clean = re.sub(" - |[.,=!?;:]+", "", contents)
                all_words[file_name] = contents_clean.split()
        return all_words

    def find(self, word: str) -> dict:
        word_dict = self.get_all_words()
        result_dict = {}
        word = word.lower()
        for file, words in word_dict.items():
            if word in words:
                result_dict[file] = words.index(word) + 1
        return result_dict

    def count(self, word: str) -> dict:
        word_dict = self.get_all_words()
        result_dict = {}
        word = word.lower()
        for file, words in word_dict.items():
            result_dict[file] = words.count(word)
        return result_dict


if __name__ == "__main__":
    finder2 = WordsFinder("test_file.txt")
    print(finder2.get_all_words())  # Все слова
    print(finder2.find("TEXT"))  # 3 слово по счёту
    print(finder2.count("teXT"))  # 4 слова teXT в тексте

    finder1 = WordsFinder(
        "Walt Whitman - O Captain! My Captain!.txt",
        "Rudyard Kipling - If.txt",
        "Mother Goose - Monday’s Child.txt",
    )
    print(finder1.get_all_words())
    print(finder1.find("the"))
    print(finder1.count("the"))

    finder1 = WordsFinder(
        "Mother Goose - Monday’s Child.txt",
    )
    print(finder1.get_all_words())
    print(finder1.find("Child"))
    print(finder1.count("Child"))

    finder1 = WordsFinder(
        "Rudyard Kipling - If.txt",
    )
    print(finder1.get_all_words())
    print(finder1.find("if"))
    print(finder1.count("if"))

    finder1 = WordsFinder("Walt Whitman - O Captain! My Captain!.txt")
    print(finder1.get_all_words())
    print(finder1.find("captain"))
    print(finder1.count("captain"))
