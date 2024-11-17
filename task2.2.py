import csv
import matplotlib.pyplot as plt


# Функція для зчитування даних з CSV файлу
def read_csv(file_path):
    data = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                country = row['Country Name']
                if country not in data:
                    data[country] = {}
                # Зберігаємо дані за роками
                data[country]['2017'] = int(row['2017 [YR2017]'])
                data[country]['2018'] = int(row['2018 [YR2018]'])
                data[country]['2019'] = int(row['2019 [YR2019]'])
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
    return data


# Побудова стовпчастої діаграми для конкретної країни
def plot_bar_chart_for_country(data, country_name):
    if country_name not in data:
        print(f"Дані для країни '{country_name}' не знайдено.")
        return

    years = ['2017', '2018', '2019']
    country_data = [data[country_name][year] for year in years]

    # Створення стовпчастої діаграми
    width = 0.35  # Ширина стовпців
    x = range(len(years))

    fig, ax = plt.subplots()

    # Розміщуємо стовпці для обраної країни
    ax.bar(x, country_data, width, label=country_name, color='blue')

    ax.set_xlabel('Year', fontsize=12, color='black')
    ax.set_ylabel('Population', fontsize=12, color='black')
    ax.set_title(f'Population ages 60-64, male (2017-2019) - {country_name}',
                 fontsize=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend()

    plt.show()


# Основна функція
def main():
    # Шлях до CSV файлу
    file_path = 'data.csv'

    # Зчитуємо дані з CSV файлу
    data = read_csv(file_path)

    if not data:
        print("Не вдалося зчитати дані з файлу.")
        return

    # Введення назви країни для побудови діаграми
    country_name = input(
        "Введіть назву країни для побудови діаграми (наприклад, 'Ukraine' або 'United Kingdom'): "
    )

    # Побудова стовпчастої діаграми для обраної країни
    plot_bar_chart_for_country(data, country_name)


if __name__ == "__main__":
    main()
