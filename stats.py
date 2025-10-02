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

def sort_on(item):
    return item["num"]

def sort_dict(char_dict):
    sorted = [{"char": ch, "num": n} for ch, n in char_dict]
    sorted.sort(reverse=True, key=sort_on)
    return sorted
