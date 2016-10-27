def nested_pyramid():
    pyramid = ''
    for r in range(1, 6):
        row = ''
        for c in range(r):
            row += '*'
        row += '\n'
        pyramid += row
    return pyramid
