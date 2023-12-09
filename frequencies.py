def frequencies(items):
    frequencies = {}
    string_items = map(str, items)
    for i in string_items:
        if i in frequencies:
            frequencies[i] = frequencies[i] + 1
        else:
            frequencies[i] = 1
    return frequencies
