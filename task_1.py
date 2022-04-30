import csv
import pandas as pd
import ast
from collections import defaultdict
import matplotlib.pyplot as plt


# Функция получения финального словаря для работы с Pandas построения графика
def get_finally_dict(file):
    # Открываем файл csv через DictReader, чтобы получить словарь
    with open(file, 'r') as f:
        csv_file = csv.DictReader(f)
        result_dict = {}
        finally_dict = {}
        reversed = defaultdict(list)
        # Формируем изначальный словарь result_dict, отсеивая ненужную информацию
        for genres in csv_file:
            result_dict[genres['Title']] = ast.literal_eval(genres['Genre'])
        # Инвертируем ключи со значениями и записываем в финальный словарь finally_dict, где ключ - название жанра,
        # значение - количество фильмов в данном жанре
        for key, array in result_dict.items():
            for value in array:
                reversed[value].append(key)
        for k, v in reversed.items():
            finally_dict[k] = len(list(v))
        return finally_dict


# Делаем круговую диаграмму с помощью pandas и выводим ее изображение через show()
def build_chart(func):
    dataframe = pd.DataFrame(list(func.items()), columns=['Genre', 'Quantity'])
    max_values = dataframe.sort_values('Quantity', ascending=False).head(5)
    max_values.set_index('Genre', inplace=True)
    max_values.plot.pie(y='Quantity', figsize=(7, 7), label='', legend=False, autopct='%1.1f%%')
    return plt.show()


if __name__ == '__main__':
    build_chart(get_finally_dict('film.csv'))
