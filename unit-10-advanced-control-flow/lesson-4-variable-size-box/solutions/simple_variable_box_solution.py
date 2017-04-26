def variable_size_box(size=4, char='*'):
    box = ''
    for i in range(size):
        row = ''
        for j in range(size):
            row += char
        row += '\n'
        box += row
    return box
