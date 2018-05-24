import re
def count_words(text, words):
    count = 0
    for word in words:
        res = []
        res = re.findall(word, text.lower())
        #print(res)
        if res != []:
            count += 1
    return count

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
