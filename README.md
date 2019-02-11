# Banned Words
I got this exercise as part of one interview process. 



## Programming pre-screening exercise
Although Python is the preferred programming language for this exercise, I was allowed to use any other language to implement this program. 

## Banned words
Write a command-line program that reads two plain text files:
- The first file contains a list of banned words, one per line
- The second file contains English prose

The script needs to read both files and print to stdout the contents of the second file, replacing the banned words with one * per original character.

### Example
#### banned_words.txt:
```
fudge
secret
```
	
#### prose.txt:
```
There are some words that one must not say such as fudge and secret - everything else is fine!
```

### Script output:
```
There are some words that one must not say such as ***** and ****** - everything else is fine!
```

### Note
RAM and CPU consumption are important – the program should be optimised to deal with several thousands of banned words and a prose input that is several gigabytes long.

Write the program as it was meant to be used in production – complete with automated tests and inline documentation.