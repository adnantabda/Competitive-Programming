def length_of_last(string: str) -> int:
    words = string.split(" ")
    word_count = []
    for word in words:
        if word:
            word_count.append(len(word))

    if word_count:
        return word_count[len(word_count) - 1]
    else:
        return 0

