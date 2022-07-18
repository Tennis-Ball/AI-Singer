import requests
from bs4 import BeautifulSoup


def get_lyric_data():
    URL = 'http://www.songlyrics.com/top-songs-lyrics.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='wrapper')
    links = str(results.find_all('td', class_='td-item td-last')).split(',')
    to_remove = []
    temp = []
    final = ''
    not_english = ['http://www.songlyrics.com/loonie/tao-lang-lyrics/',
                   'http://www.songlyrics.com/prince-royce/darte-un-beso-lyrics/',
                   'http://www.songlyrics.com/banda-el-recodo-de-cruz-lizarraga/vas-a-llorar-por-m-lyrics/',
                   'http://www.songlyrics.com/banda-los-recoditos/mi-ultimo-deseo-lyrics/',
                   'http://www.songlyrics.com/aventura/el-malo-lyrics/',
                   'http://www.songlyrics.com/slank/ku-tak-bisa-lyrics/',
                   'http://www.songlyrics.com/ron-henley/hagdan-lyrics/',
                   'http://www.songlyrics.com/stromae/tous-les-mmes-lyrics/',
                   'http://www.songlyrics.com/prince-royce/el-amor-que-perdimos-lyrics/',
                   'http://www.songlyrics.com/yeng-constantino/alaala-lyrics/',
                   'http://www.songlyrics.com/yeng-constantino/chinito-lyrics/',
                   'http://www.songlyrics.com/anitta/zen-lyrics/',
                   'http://www.songlyrics.com/sarah-geronimo/tayo-lyrics/',
                   'http://www.songlyrics.com/rio-febrian/jenuh-lyrics/']

    for i in range(len(links)):
        http = 0

        for _ in range(len(links[i]) - 3):
            end_http = links[i][_] + links[i][_ + 1] + links[i][_ + 2]
            if end_http == '/" ':
                links[i] = links[i][42:_ + 1]
                http = 1
                break

        if http == 0:
            to_remove.append(i)

    for count, remove in enumerate(to_remove):
        links.remove(links[remove - count])

    for count, link in enumerate(links):
        songs = count
        print('Collecting lyrics from: ', link)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        song_lyrics = str(soup.find(id='songLyricsDiv')).split('<br/>\r\n')

        for i in range(len(song_lyrics)):
            for _ in song_lyrics[i].split():
                if link not in not_english:
                    temp.append(_)
    print(songs - 15, 'songs with lyrics found')

    for word in range(len(temp)):
        for z in range(temp[word].count('<')):
            to_remove.clear()
            tag = 0
            for _ in range(len(temp[word])):
                if tag == 1:
                    if temp[word][_] == '>':
                        to_remove.append(_)
                        tag = 0
                        break

                if temp[word][_] == '<':
                    to_remove.append(_)
                    tag = 1

            if len(to_remove) == 1:
                temp[word] = temp[word][to_remove[0] + 1:]

            if len(to_remove) == 2:
                temp[word] = temp[word][:to_remove[0]] + temp[word][to_remove[1] + 1:]

    to_remove.clear()

    for not_a_word in range(len(temp)):
        if temp[not_a_word] == 'p':
            to_remove.append(not_a_word)

        elif temp[not_a_word] == 'span':
            to_remove.append(not_a_word)

        elif temp[not_a_word][:4] == 'id="':
            to_remove.append(not_a_word)

        elif temp[not_a_word][:8] == 'iComment':
            to_remove.append(not_a_word)

        elif temp[not_a_word][:10] == 'data-chunk':
            to_remove.append(not_a_word)

        elif temp[not_a_word][:6] == 'href="':
            to_remove.append(not_a_word)

        elif temp[not_a_word][:7] == 'class="':
            to_remove.append(not_a_word)

        elif temp[not_a_word] == '':
            to_remove.append(not_a_word)

    for count, remove in enumerate(to_remove):
        temp.remove(temp[remove - count])

    print('Number of data points (in words): ', len(temp))
    for i in temp:
        final += i
        final += ' '

    return final
