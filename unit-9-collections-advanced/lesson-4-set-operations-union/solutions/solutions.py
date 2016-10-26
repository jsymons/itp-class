def common_values(tuple_1, tuple_2):
    if isinstance(tuple_1, tuple) and isinstance(tuple_2, tuple):
        return set(tuple_1).union(set(tuple_2))
    return "Params not of type 'tuple'"