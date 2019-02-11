prose = open('prose.txt', 'r').read().split('\n')

banned_words = open('banned_words.txt', 'r').read().lower().split('\n')

output = ''

for s in prose:
    if s == '':
        output = output + '\n'
    else:
        tokens = s.split()
        filtered = []

        for word in tokens:
            if word.lower() in banned_words:
                filtered.append(word.replace(word, len(word)*'*'))
            else:
                filtered.append(word)

        output = output + " ".join(filtered) + "\n"

print(output)
