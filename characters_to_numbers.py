def characters_to_numbers(words):
    final = []
    for i in range(len(words)):
        if ord(words[i]) < 166:
            final.append(ord(words[i]))

    return final
