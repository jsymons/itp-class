def inverted_pyramid():
    pyramid = ''
    for r in range(1, 6):
        row = ''
        for c in range(6 - r):
            row += '*'
        row += '\n'
        pyramid += row
    return pyramid
