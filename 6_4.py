# ------------- LESSON 6, EXERCISE 4 -------------------
# Filter list for string types

# ---- 1st way ----
def filter_for_string(list_to_filter):
    for i in list_to_filter:
        if isinstance(i, list):
            list_to_filter[list_to_filter.index(i)] = filter_for_string(i)
    return [*filter(lambda x: isinstance(x, (str, list)), list_to_filter)]
# ---- 1st way ----
# ---- 2nd way ----
def filter_for_string2(list_to_filter, lngth):
    i = 0  # counter
    while i != lngth:
        if isinstance(list_to_filter[i], list):
            any_in_list = filter_for_string2(list_to_filter[i], len(list_to_filter[i]))
            if not any_in_list:  # if blank list returned
                list_to_filter.remove(list_to_filter[i])  # remove blank list
                lngth -= 1
            else:
                i += 1
        elif not isinstance(list_to_filter[i], str):
            list_to_filter.remove(list_to_filter[i])
            lngth -= 1
        else:
            i += 1

    return list_to_filter
# ---- 2nd way ----

list_for_filter = [1, 2, 3, [4, '234', 45, 345, '34', [234, 0, '34', '90'], [234, '34']],
                   'efg', '234', None, 234, 234, True, {'key': 'value'}, 'rsgh', ['345', '00000', '3454', 345, 345],
                   '325', [34, 34, [34, 34, '7'], [1, 2]]]

print(filter_for_string2(list_for_filter, len(list_for_filter)))
print(filter_for_string(list_for_filter))
