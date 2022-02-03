# -*- encoding: utf-8 -*-

from kmp import kmp_algorithm
from shrek import shrek_text
import random
import datetime

checked = 0
failed = 0
tests = 10000
start = datetime.datetime.now()
print(f'Начало тестов: {start}')

for i in range(0, tests):
    if not i % (tests / 10):
        print(f'{i / tests * 100}%')

    start_fragment = random.randint(0, len(shrek_text) - 2100)
    length_fragment = random.randint(20, 2000)
    shrek_text_fragment = shrek_text[start_fragment:start_fragment + length_fragment]

    start_search = random.randint(0, len(shrek_text_fragment) - 15)
    length_search = random.randint(1, 10)
    search = shrek_text_fragment[start_search:start_search + length_search]
    
    index = kmp_algorithm(shrek_text_fragment, search)

    for j in index:
        if search != shrek_text_fragment[j:j + len(search)]:
            print(f'Тест #{i} содержит неверный ответ по индексу: {j}')
            print(f'{search} != {shrek_text_fragment[j:j + len(search)]}')
            print(f'Текст: "{shrek_text_fragment}"')
            failed = failed + 1
        else:
            checked = checked + 1    

end = datetime.datetime.now()
print(f'Тесты завершены: {end}\nДлительность тестов: {end - start}')
print(f'Всего тестов: {tests}\nСовпадений: {checked}\nОшибок: {failed}')

