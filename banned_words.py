# Lowercase the words to go around words in mixed case
banned_words = open('banned_words.txt', 'r').read().lower().split('\n')
prose = open('prose.txt', 'r')

# Process file line by line to save RAM and CPU
for line in prose:
    if line == '':
        print("\n")
    else:
        # Tokenize the line
        tokens = line.split()
        filtered = []

        # Search for stop word in tokens
        for word in tokens:
            # Replace the word if it is found in banned ones
            if word.lower() in banned_words:
                filtered.append(word.replace(word, len(word)*'*'))
            else:
                filtered.append(word)

        # Print filtered output to stdout
        print(" ".join(filtered))

prose.close()
