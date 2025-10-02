from stats import count_words, count_chars

def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    content = get_book_text("./books/frankenstein.txt")
    print(f"Found {count_words(content)} total words")
    print(count_chars(content))

main()
