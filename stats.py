def get_words_number(text):
    return len(text.split())

def get_chars_counts(text):
    text = text.lower()
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(counts_dict):
    list = []
    for char in counts_dict:
        new_dict = {"char": char, "num": counts_dict[char]}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list