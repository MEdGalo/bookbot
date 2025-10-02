from stats import (count_words, count_chars, sort_dict)
import sys

def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def print_result(path, content, sorted):
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


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    sorted = sort_dict(count_chars(content).items())
    print_result(sys.argv[1], content, sorted)


main()
