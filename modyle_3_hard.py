data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*args):
    result1 = 0
    for it in args:
        if isinstance(it, list | tuple | set):
            for element in it:
                result1 += calculate_structure_sum(element)
        elif isinstance(it, dict):
            for key, value in it.items():
                result1 += calculate_structure_sum(key, value)
        elif isinstance(it, str):
            result1 += len(it)
        elif isinstance(it, int):
            result1 += it
    return result1




result = calculate_structure_sum(data_structure)
print(result)






