def custom_write(file_name, strings):   # file_name - название файла для записи, strings - список строк для записи.
    i = 0
    strings_positions = {}
    for string in strings:
        i += 1
        file = open(file_name, 'a', encoding='utf-8')
        a = file.tell()
        file.write(f"{string}\n")
        file.close()
        strings_positions[i, a] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
