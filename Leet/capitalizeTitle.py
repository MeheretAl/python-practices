def capitalizeTitle(title: str) -> str:
    words = title.split(' ')
    for i in range(len(words)):
        if len(words[i]) <= 2:
            words[i] = words[i].lower()
            # words[i][0:2].lower() and words[i][:2].lower() are valid ways
        else:
            words[i] = words[i][0].upper() + words[i][1:].lower()

    return " ".join(words)


sentence = "First leTTeR of EACH Word"
print(capitalizeTitle(sentence))
