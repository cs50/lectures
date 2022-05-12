import inflect

p = inflect.engine()

for i in range(10):
    word = p.number_to_words(i)
    print(word)
