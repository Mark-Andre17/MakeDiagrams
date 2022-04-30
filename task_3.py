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
            if 'Family' in genres['Genre']:
                result = genres['Title'][genres['Title'].find('(') + 1:genres['Title'].find(')')]
                result_dict[int(genres['Domestic Sales (in $)'])] = result

        return result_dict


# Делаем график BAR, складывая значения доходов с фильмов Family по годам
def build_plot_chart(func):
    dataframe = pd.DataFrame(list(func.items()), columns=['Domestic Sales', 'Year'])
    result = dataframe.groupby('Year')['Domestic Sales'].sum()
    result.plot(x='Year', y='Domestic Sales', rot=5, fontsize=8)
    return plt.show()


if __name__ == '__main__':
    build_plot_chart(get_finally_dict('film.csv'))
