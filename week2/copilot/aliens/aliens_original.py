'''lab11'''
from benchmark_funcs import time_to_run, memory_used

def read_file(file_path):
    '''
    funktion to read a file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', delete=False, encoding = 'utf-8')\
as file:
    ...     _=file.write('AB,200\\nBC,200')
    >>> read_file(file.name)
    {'AB': 200, 'BC': 200}
    Time taken: read_file 1.6854819978107117e-05
    Memory: read_file (805, 14661)
    '''
    dct = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()
    for i in text:
        if i.startswith('#'):
            pass
        else:
            key, values = i.strip().split(',')
            dct[key] = int(values)
    return dct
@memory_used
def rescue_people(smarties, limit_iq):
    '''
    function to present a last of people, where one list means that this
    people have a trip in one time
    >>> rescue_people({'AB': 200, 'BC': 200, 'ID': 250, 'IB': 250, 'OC': 300, \
'OD': 300, 'i': 350}, 550)
    (4, [['i', 'AB'], ['OC', 'IB'], ['OD', 'ID'], ['BC']])
    Time taken: rescue_people 5.399766017944785e-06
    Memory: rescue_people (384, 904)
    '''
    if len(smarties) == 0:
        return 0, []
    sum_ = 0
    chec = []
    all_trip = []
    sort_dct = {}
    for k, v in sorted(smarties.items(), key=lambda item: (-item[1], item[0])):
        if v <= limit_iq:
            sort_dct[k] = v
    for key, value in sort_dct.items():
        if key not in chec:
            sum_ = value
            one_trip = []
            one_trip.append(key)
            chec.append(key)
            for k, v in sort_dct.items():
                if value <= limit_iq and v <= limit_iq and key != k and k not in chec:
                    if sum_ + v <= limit_iq:
                        sum_ += v
                        one_trip.append(k)
                        chec.append(k)
            all_trip.append(one_trip)
    first = len(all_trip)
    return first, all_trip

if __name__ == '__main__':
    dct = read_file("smart_people.txt")
    print(rescue_people(dct, 550))
