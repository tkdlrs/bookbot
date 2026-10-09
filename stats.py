
# 
def get_word_count(str_text):
    return len(str_text.split())
# 

def get_character_counts(str_text):
    char_counts = {}

    for char in str_text:
        lower_case = char.lower()
        if lower_case not in char_counts:
            char_counts[lower_case] = 1
        else:
            char_counts[lower_case] += 1

    # print(char_counts)
    return char_counts
# 
def sort_on(character_count: tuple[str, int]) -> int:
    return character_count[1]
# 
def chars_dict_to_sorted_list(char_count_dict: dict[str, int]) -> list[tuple[str, int]]:
    output = []
    # 
    for character in char_count_dict:
        count = char_count_dict[character]
        output.append((character, count))

    
    # 
    return sorted(output, reverse=True, key=sort_on)


    
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