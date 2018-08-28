words_used = {}
text = input("Enter text: ")
words = text.split()
for word in words:
    frequency = words_used.get(word, 0)
    words_used[word] = frequency + 1

words = list(words_used.keys())
words.sort()
max_length = max(len(word) for word in words)
print("Text: {}".format(text))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_used[word]))


