from collections import deque

words = input("Escreve um conjunto de palavras separadas por espaços: ")
words_separated = deque()
new_words = words.split()
for i in new_words:
   words_separated.appendleft(i)
print(words_separated)

for word in new_words:
    if "o" in word:
     print(word)