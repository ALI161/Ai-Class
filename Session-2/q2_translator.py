words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "hello": "سلام",
    "you": "تو",
    "book": "کتاب",
}

sent = "I love python and AI"
sent = sent.lower().split()

translat = []
translat_count = 0
unknown_count = 0

for word in sent:
    if word in words:
        translat.append(words[word])
        translat_count += 1
    else:
        translat.append("[" + word + "]")
        unknown_count += 1

print(" ".join(translat))

print("Translated words:", translat_count)
print("Unknown words:", unknown_count)
