def count_words(text):
    return len(text.split())
def count_characters(text):
    char_counts = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else :
            char_counts[char] = 1
    return char_counts

# python
def sorted_characters(char_counts):
    result = []
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    result.sort(key=sort_on, reverse=True)
    return result