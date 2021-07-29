from lyrics import make_lyrics
from song import make_song
from profanityfilter import ProfanityFilter
import syllables as sl
import time


pf = ProfanityFilter()

lyrics_length = 75
lyrics_epochs = 50000
lyrics_neuron_size = 128

lyrics = make_lyrics(lyrics_length, lyrics_epochs, lyrics_neuron_size)
pf.set_censor('')
lyrics = pf.censor(lyrics)

print('\n\nLyrics generated: ' + lyrics + '\n')


song_length = sl.estimate(lyrics)
print('Estimated lyrics syllables:', song_length)
time.sleep(10)
song_epochs = 1
song_batch_size = 256

make_song(song_length, song_epochs, song_batch_size)
