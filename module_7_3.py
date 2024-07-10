class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        _list = []
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:    # Перебор названий файлов
            with open(name, encoding='utf-8') as file:    # Открываем файл
                for line in file:   # Перебираем строки в файле    # Переводим строку в нижний регистр
                    for symbol in symbols:  # Перебор символов
                        if symbol in line:  # Если есть символы в строке
                            line.replace(symbol, '')    # Удаляем их
                    _list += (line.lower()).split()
                all_words[name] = _list
                return all_words

    def find(self, word):
        k = 0
        for key in self.get_all_words():
            for j in self.get_all_words()[key]:
                k += 1
                if j == word.lower():
                    return {key, k}

    def count(self, word):
        k = 0
        for key in self.get_all_words():
            for j in self.get_all_words()[key]:
                if j == word.lower():
                    k += 1
            return {key, k}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))     # 3 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего
