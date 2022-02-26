from random_words import RandomWords
from quote import quote
r = RandomWords()
w = r.random_word()
print("Keyword Generated: ", w)
res = quote(w, limit=1)
for i in range(len(res)):
        print("\nQuote Generated: ", res[i]['quote'])