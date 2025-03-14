from stats import get_num_words, get_book_text, get_char_count, get_sorted_dict_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = get_sorted_dict_list(char_count)
    print(("="*12) + " BOOKBOT " + ("="*12))
    print(f"Analyzing book found at {book_path}...")
    print(("-"*11) + " Word Count " + ("-"*11))
    print(f"Found {word_count} total words")
    print(("-"*9) + " Character Count " + ("-"*9))
    for i in range(len(sorted_chars)):
        print(f"{sorted_chars[i]['char']}: {sorted_chars[i]['count']}")
    print(("="*13) + " END " + ("="*13))

main()
