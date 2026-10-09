import sys
from stats import (
    chars_dict_to_sorted_list,
    get_character_dict,
    get_num_words, 
)
# 
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_character_dict(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)
    print_report(book_path, num_words, char_sorted_list)
# 
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
#
def print_report(
        book_path: str,num_words: int, chars_sorted_list: list[tuple[str, int]]
) -> None:
    print(" ========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for char, count in chars_sorted_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print(" ========== END ==========")
#  
main()
# 
