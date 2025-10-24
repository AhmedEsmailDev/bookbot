from stats import get_words_number, get_chars_counts, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    number_of_words = get_words_number(book_text)
    chars_counts = get_chars_counts(book_text)
    sorted_chars = get_sorted_list(chars_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()