banned_words = open('banned_words.txt', 'r').read().lower().split('\n')
prose = open('prose.txt', 'r')

for line in prose:
    if line == '':
        print("\n")
    else:
        tokens = line.split()
        filtered = []

        for word in tokens:
            if word.lower() in banned_words:
                filtered.append(word.replace(word, len(word)*'*'))
            else:
                filtered.append(word)

        print(" ".join(filtered))

prose.close()
