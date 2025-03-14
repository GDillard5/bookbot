import collections

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for i, c in enumerate(text):
        char = c.lower()
        if char not in char_count.keys():
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def get_sorted_dict_list(table):
    dict_list = []
    for k in table.keys():
        dict_list.append({'char':k, 'count':table[k]})
    sorted_list = sorted(dict_list, reverse=True, key=lambda d: d['count'])
    return sorted_list

