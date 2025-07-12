def word_count(book_string):
    words = book_string.split()
    return len(words)

def count_characters(book_text):
    lowercased_text = book_text.lower()
    count_total = {}
    
    for char in lowercased_text:
        if char not in count_total:
            count_total[char] = 1
        else:
            count_total[char] += 1
    return count_total

def sort_on(letters):
    return letters["num"]

def sort_dict(chars_dict):
    sorted_results = []
    for char in chars_dict:
        if char.isalpha():
            sorted_results.append({"char": char, "num": chars_dict[char]})
    sorted_results.sort(reverse=True, key=sort_on)
    return sorted_results