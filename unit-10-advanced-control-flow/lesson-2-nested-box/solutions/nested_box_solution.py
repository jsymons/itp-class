def nested_box():
    box = ''
    for i in range(4):
        row = ''
        for j in range(4):
            row += '*'
        row += '\n'
        box += row
    return box
