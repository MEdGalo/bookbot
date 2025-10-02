def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars
