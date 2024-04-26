'''
This script has functions that work with dictionary 
'''
import copy

def dict_reader_tuple(file_dict:str)->list:
    '''
    This fucntion reads file and returns a tuple with 3 items
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('ABDUCT 1 AE0 B D AH1 K T\\n\
ABDUCTING 1 AE0 B D AH1 K T IH0 NG\\n\
ABDUCTING 2 AH0 B D AH1 K T IH0 NG')
    >>> dict_reader_tuple(tmpfile.name)
    [('ABDUCT', 1, ['AE0', 'B', 'D', 'AH1', 'K', 'T']), \
('ABDUCTING', 1, ['AE0', 'B', 'D', 'AH1', 'K', 'T', 'IH0', 'NG']), \
('ABDUCTING', 2, ['AH0', 'B', 'D', 'AH1', 'K', 'T', 'IH0', 'NG'])]
    '''
    list_of_tup = []
    with open(file_dict,'r+',encoding='utf-8') as file:
        length = file.readlines()
        file.seek(0)
        for _ in range(len(length)):
            line = file.readline().strip('\n')
            line_s = line.split(' ')
            line_no_2 = line_s.copy()
            for _ in range(2):
                del line_no_2[0]
            voc_tup = (line_s[0],int(line_s[1]),line_no_2)
            list_of_tup.append(voc_tup)
        return list_of_tup

def dict_reader_dict(file_dict):
    '''
    This fucntion reads file and returns a tuple with 3 items
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('ABDUCT 1 AE0 B D AH1 K T\\n\
ABDUCTING 1 AE0 B D AH1 K T IH0 NG\\n\
ABDUCTING 2 AH0 B D AH1 K T IH0 NG')
    >>> dict_reader_dict(tmpfile.name) == {'ABDUCT': {('AE0', 'B', 'D', 'AH1', 'K', 'T')}, \
'ABDUCTING': {('AE0', 'B', 'D', 'AH1', 'K', 'T', 'IH0', 'NG'), \
('AH0', 'B', 'D', 'AH1', 'K', 'T', 'IH0', 'NG')}}
    True
    '''
    lines_dict = {}
    with open(file_dict, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for _, line in enumerate(lines):
            line_s = line.strip().split(' ')
            line_ss = copy.deepcopy(line_s)
            final_line = []
            final_line.append(line_ss[2:])
            lines_set = set()
            line_del = final_line.copy()
            for lst in line_del:
                lines_set.add(tuple(lst))
            if line_s[1] == '1':
                lines_dict[line_s[0]] = lines_set
            if line_s[1] != '1':
                val = lines_dict[line_s[0]]
                for lst in line_del:
                    val.add(tuple(lst))
                lines_dict[line_s[0]] = val
    return lines_dict

def dict_invert(dct):
    '''
    This fucntion reads file and returns a tuple with 3 items
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},\
'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1',\
'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},\
'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}})==\
{1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G')), \
('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')),('A42128', \
('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T'))}, \
2: {('A', ('EY1',)), ('A', ('AH0',))}}
    True
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False) as file:
    ...     _ = file.write("A 1 AH0\\n\
A. 1 EY1\\n\
A 2 EY1\\n\
A42128 1 EY1 F AO1 R T UW1 W AH1 N T UW1 EY1 T\\n\
AAA 1 T R IH2 P AH0 L EY1\\n\
AABERG 1 AA1 B ER0 G\\n\
AACHEN 1 AA1 K AH0 N\\n\
AACHENER 1 AA1 K AH0 N ER0\\n\
AAKER 1 AA1 K ER0\\n\
AALSETH 1 AA1 L S EH0 TH\\n\
AAMODT 1 AA1 M AH0 T\\n\
AANCOR 1 AA1 N K AO2 R\\n\
AARDEMA 1 AA0 R D EH1 M AH0\\n\
AARDVARK 1 AA1 R D V AA2 R K\\n\
AARON 1 EH1 R AH0 N\\n\
AARON'S 1 EH1 R AH0 N Z\\n\
AARONS 1 EH1 R AH0 N Z\\n\
AARONSON 1 EH1 R AH0 N S AH0 N\\n\
AARONSON 2 AA1 R AH0 N S AH0 N\\n\
AARONSON'S 1 EH1 R AH0 N S AH0 N Z")
    >>> dict_invert(dict_reader_tuple(file.name)) == dict_invert(dict_reader_dict(file.name))
    True
    '''
    result = {}
    if isinstance(dct, list):
        temp = {}
        for item in dct:
            if item[0] not in temp:
                temp[item[0]] = set()
                temp[item[0]].add(tuple(item[2]))
            else:
                temp[item[0]].add(tuple(item[2]))
        dct = temp
    if isinstance(dct, dict):
        for item in dct:
            count = len(dct[item])
            if count not in result:
                result[count] = set()
            for val in dct[item]:
                result[count].add((item, val))
        return result
    return None

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
