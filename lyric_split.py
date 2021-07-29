from numpy import asarray


def split_lyrics(lyrics):
    train = []
    output = []
    
    for i in range(len(lyrics)):
        lyrics[i] = (lyrics[i] - 32) / (122 - 32)

        if i < len(lyrics) - 1:
            train.append(lyrics[i])

        if i != 0:
            output.append(lyrics[i])

    return asarray(train), asarray([output])
