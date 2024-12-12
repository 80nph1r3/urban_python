def single_root_words(root_word: str, *other_words: str) -> list[str]:
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


if __name__ == "__main__":
    result1 = single_root_words("rich", "richiest", "orichalcum", "cheers", "richies")
    result2 = single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel")
    print(result1)
    print(result2)
