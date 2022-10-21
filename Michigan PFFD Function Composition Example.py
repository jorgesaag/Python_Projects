def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

print(most_common_letter("aaaacbbbbbbuuuuuuuuu"))

