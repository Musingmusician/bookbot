from stats import (
    count_words,
    char_count,
    sorted_char_count
)

import sys

def main():
    if not len(sys.argv) == 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = char_count(text)
    character_count_sorted = sorted_char_count(character_count)
    print_report(book_path,word_count,character_count_sorted)

def print_report(book_path, word_count, char_count_sorted):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in char_count_sorted:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
       return f.read()

main()