from stats import (
    get_word_count, 
    get_character_counts,
    chars_dict_to_sorted_list
)
# 
def main():
    book_to_examine = "./books/frankenstein.txt"
    with open(book_to_examine) as f:
        file_contents = f.read()
        # print(file_contents)
        # print(f"The word count is {get_word_count(file_contents)}")
        # print(f"{get_character_counts(file_contents)}")
        word_count = get_word_count(file_contents)
        print(f"Found {word_count} total words")
        char_hash = get_character_counts(file_contents)
        sorted_list = chars_dict_to_sorted_list(char_hash)
        print(sorted_list)
        # report = generate_report(char_hash, word_count, book_to_examine)
# 
main()

