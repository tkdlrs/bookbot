from stats import (
    chars_dict_to_sorted_list,
    get_character_dict,
    get_num_words, 
)
# 
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_character_dict(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)
    # 
    print(f"Found {num_words} total words")
    print(char_sorted_list)
    # report = generate_report(char_hash, word_count, book_to_examine)
# 
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
# 
main()
