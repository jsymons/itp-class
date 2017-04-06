def common_values(tuple_1, tuple_2):
    if type(tuple_1) != tuple or type(tuple_2) != tuple:
        return "Params not of type 'tuple'"
    result = []
    for elem in tuple_1:
      result.append(elem)

    for elem in tuple_2:
      result.append(elem)

    return set(result)
