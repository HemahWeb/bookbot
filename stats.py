def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_chars(text):
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_chars(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            line = {"char": char, "count": count}
            char_list.append(line)

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list




