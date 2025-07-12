import sys
from stats import word_count, count_characters, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
         print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
         sys.exit(1)
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(book_text)
    print(char_counts)
    sorted_dict_count = sort_dict(char_counts)
    for entry in sorted_dict_count:
        print(f"{entry['char']}: {entry['num']}")

main()