def replace_missing_element(lst):
    missing_element = None
    for element in lst:
        if element is None:
            missing_element = element
            break

    total_sum = sum(x for x in lst if x is not None)
    total_count = len(lst)

    average = total_sum / (total_count - 1)
    for i in range(len(lst)):
        if lst[i] is None:
            lst[i] = average
            break

    return lst
