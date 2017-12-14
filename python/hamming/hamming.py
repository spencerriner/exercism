def distance(strand_a, strand_b):
    length = 0
    strand_a = list(strand_a)
    strand_b = list(strand_b)
    if len(strand_a) != len(strand_b):
        raise ValueError('Invalid input')
    for letter in strand_a:
        if letter != strand_b[i]:
            length += 1
        i += 1
    return length
