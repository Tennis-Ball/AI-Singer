import py_midicsv as pm


def data_format():
    names = ['Alone.mid', 'Bad guy.mid', 'Despacito.mid', 'Dynamite.mid', 'Faded.mid', 'Shape of you.mid', 'Dance monkey.mid']
    data = []
    for i in names:
        for _ in pm.midi_to_csv('song_modules/song_data/' + i):
            data.append(_)
    return data
