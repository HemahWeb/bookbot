import sys
from stats import get_num_words, get_chars, sort_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    chars = get_chars(text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
            print(f"{char}: {count}")
        

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()