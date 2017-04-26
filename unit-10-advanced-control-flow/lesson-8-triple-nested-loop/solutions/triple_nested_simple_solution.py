def triple_nested_loop(size=5):
    box = ''
    for i in range(1, size + 1):
        row = ''
        for j in range(size - i):
            row += '.'
        for m in range(i):
            row += str(i)
        row += '\n'
        box += row
    return box
