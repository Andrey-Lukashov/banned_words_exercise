from nltk.tokenize import word_tokenize

prose = open('prose.txt', 'r').read()

banned_words = open('banned_words.txt', 'r').read().lower().split('\n')
banned_words = list(filter(None, banned_words))

word_tokens = word_tokenize(prose)

filtered_sentence = []

for w in word_tokens:
    if w.lower() not in banned_words:
        filtered_sentence.append(w)
    else:
        filtered_sentence.append(w.replace(w, len(w)*'*'))

print(filtered_sentence)