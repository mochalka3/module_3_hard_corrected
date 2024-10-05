def calculate_structure_sum(data):
    total_sum = 0


    def sum_elements(elements):
        nonlocal total_sum
        for element in elements:
            if isinstance(element, (int, float)):
                total_sum += element
            elif isinstance(element, str):
                total_sum += len(element)
            elif isinstance(element, list):
                sum_elements(element)
            elif isinstance(element, dict):
                for key, value in element.items():
                    total_sum += len(key)
                    if isinstance(value, (int, float)):
                        total_sum += value
                    elif isinstance(value, list):
                        sum_elements([value])
            elif isinstance(element, (list, tuple, set)):
                sum_elements(list(element))


    sum_elements(data)
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
