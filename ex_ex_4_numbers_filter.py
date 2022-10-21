def even_odd_filter(**kwargs):
    result = {}
    for key, values in kwargs.items():
        if key == 'even':
            filtered_even = [x for x in kwargs[key] if x % 2 == 0]
            result['even'] = filtered_even
        elif key == 'odd':
            filtered_odd = [x for x in kwargs[key] if x % 2 != 0]
            result['odd'] = filtered_odd

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
