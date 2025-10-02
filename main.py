from stats import count_words, count_chars, sort_dict

def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    path = "./books/frankenstein.txt"
    content = get_book_text(path)
    sorted = sort_dict(count_chars(content).items())

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(content)} total words")
    print("----------- Char Count ----------")

    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")

    print("============ END ============")


main()
