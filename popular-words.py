txt = 'When I was One I had just begun When I was Two I was nearly new'
wrd =  ['i', 'was', 'three', 'near']


def popular_words(text, words):
    res = []
    for word in words:
        i = 0
        for item in text.lower().split():
            if word == item:
                i += 1
        res.append((word, i))
    #print(dict(res))
    return dict(res)




popular_words(txt, wrd)