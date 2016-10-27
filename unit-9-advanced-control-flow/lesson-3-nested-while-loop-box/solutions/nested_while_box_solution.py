def nested_while_loop_box():
    box = ''
    row_count = 1
    while row_count < 5:
        row = ''
        col_count = 1
        while col_count < 5:
            row += '*'
            col_count += 1

        row += '\n'
        box += row
        row_count += 1
    return box
