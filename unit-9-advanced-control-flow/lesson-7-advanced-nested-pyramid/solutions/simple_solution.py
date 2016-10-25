def advanced_nested_pyramid(start=1, last=5, char='*'):
    pyramid = ''
    for r in range(start, last + 1):
        row = ''
        for c in range(r):
            row += char

        row += '\n'
        pyramid += row

    return pyramid
