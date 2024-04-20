'''lab11'''

# Copilot needed a few promts to optimize the code,
# and it was more efficient for him to indicate which function
# or part of the code should be changed. The modified version
# runs a bit faster, has no unnecessary branching,
# and reads the file using less memory.
# The modified version works correctly and passes all tests.

def read_file(file_path):
    '''
    funktion to read a file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding = 'utf-8')\
as file:
    ...     _=file.write('AB,200\\nBC,200')
    >>> read_file(file.name)
    {'AB': 200, 'BC': 200}
    '''
    dct = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.startswith('#'):
                key, values = line.strip().split(',')
                dct[key] = int(values)
    return dct

def rescue_people(smarties, limit_iq):
    '''
    function to present a last of people, where one list means that this
    people have a trip in one time
    >>> rescue_people({'AB': 200, 'BC': 200, 'ID': 250, 'IB': 250, 'OC': 300, \
'OD': 300, 'i': 350}, 550)
    (4, [['i', 'AB'], ['OC', 'IB'], ['OD', 'ID'], ['BC']])
    '''
    if len(smarties) == 0:
        return 0, []

    all_trip = []
    filtered_smarties = {k: v for k, v in smarties.items() if v <= limit_iq}
    sort_dct = dict(sorted(filtered_smarties.items(), key=lambda item: (-item[1], item[0])))
    keys = list(sort_dct.keys())

    while keys:
        key = keys.pop(0)
        sum_ = sort_dct[key]
        one_trip = [key]
        for other_key in keys[:]:
            if sum_ + sort_dct[other_key] <= limit_iq:
                sum_ += sort_dct[other_key]
                one_trip.append(other_key)
                keys.remove(other_key)
        all_trip.append(one_trip)

    return len(all_trip), all_trip

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
