# 
def get_num_words(text:str) -> int:
    words = text.split()
    return len(words)
# 
def get_character_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
# 
def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]
# 
def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars_list: list[tuple[str, int]] = []
    for char in num_chars_dict:
        count = num_chars_dict[char]
        chars_list.append((char, count))
    # 
    return sorted(chars_list, reverse=True, key=sort_on)
# 
"""
def generate_report(dic_char_count, word_count, book_title ):
    report = f"--- Begin report of {"/".join(book_title.split("/")[1:])} ---\n"
    report += f"{word_count} words found in the document\n\n"
    list_count = []
    #
    def helper_sort_on_count(d):
        return d["count"]
    #
    for key in dic_char_count:
        if key.isalpha():
            dict_phase_and_count = { "phrase": f"The '{key}' character was found {dic_char_count[key]} times", "count": dic_char_count[key]}
            list_count.append(dict_phase_and_count)
    #   
    list_count.sort(reverse=True, key=helper_sort_on_count)
    for item in list_count:
        current_phrase = item["phrase"]
        report += current_phrase
        report += "\n"
    #
    report += f"--- End report ---"
    #
    return report

"""
# 