def count_words(text):
    word_list = text.split()
    num_words = 0
    for word in word_list:
        num_words += 1
    return num_words

def character_count(text):
    lowercase = text.lower()
    counts = {}
    for ch in lowercase:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_characters(counts):
    sorted_list = []
    for ch, cnt in counts.items():
        sorted_list.append({"char": ch, "num": cnt}) 
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list
