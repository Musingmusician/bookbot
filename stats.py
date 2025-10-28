def count_words(string):
    words = string.split()
    return len(words)

def char_count(string):
    char_dict = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
     return items["num"]

def sorted_char_count(char_dict):
        sort_char_dict = []
        for char in char_dict:
            sort_char_dict.append({
                  "char" : char,
                  "num" : char_dict[char]
             })
        sort_char_dict.sort(reverse=True, key=sort_on)
        return sort_char_dict