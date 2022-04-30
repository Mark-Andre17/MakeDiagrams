import csv
import pandas as pd
import matplotlib.pyplot as plt


# Функция получения финального словаря для работы с Pandas построения графика
def get_finally_dict(file):
    # Открываем файл csv через DictReader, чтобы получить словарь
    with open(file, 'r') as f:
        csv_file = csv.DictReader(f)
        result_dict = {}
        # Формируем изначальный словарь result_dict, отсеивая ненужную информацию
        for genres in csv_file:
            result = genres['Title'][genres['Title'].find('(') + 1:genres['Title'].find(')')]
            result_dict[int(genres['World Sales (in $)'])] = result

        return result_dict


# Делаем график BAR, складывая значения доходов с фильмов по годам
def build_bar_chart(func):
    dataframe = pd.DataFrame(list(func.items()), columns=['World Sales', 'Year'])
    result = dataframe.groupby('Year')['World Sales'].sum()
    result.plot(x='Year', y='World Sales', kind='bar', rot=0, fontsize=5)
    return plt.show()


if __name__ == '__main__':
    build_bar_chart(get_finally_dict('film.csv'))
