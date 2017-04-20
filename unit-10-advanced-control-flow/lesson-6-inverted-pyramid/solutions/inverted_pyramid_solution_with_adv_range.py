def inverted_pyramid():
    pyramid = ''
    for r in range(5, 0, -1):
        row = ''
        for c in range(r):
            row += '*'
        row += '\n'
        pyramid += row
    return pyramid
