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

# Побудова графіка для динаміки показника
def plot_graph(data):
    years = ['2017', '2018', '2019']

    # Дані для України та Великобританії
    ukraine_data = [data['Ukraine'][year] for year in years]
    uk_kingdom_data = [data['United Kingdom'][year] for year in years]

    # Побудова лінійного графіка
    plt.plot(years, ukraine_data, label='Ukraine', color="blue", linewidth=2)
    plt.plot(years, uk_kingdom_data, label='United Kingdom', color="green", linewidth=2)

    plt.title('Population ages 60-64, male (2017-2019)', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='black')  # позначення вісі абсцис
    plt.ylabel('Population', fontsize=12, color='black')  # позначення вісі ординат
    plt.legend()
    plt.grid(True)
    plt.show()

# Основна функція
def main():
    # Шлях до CSV файлу
    file_path = 'data.csv'  

    # Зчитуємо дані з CSV файлу
    data = read_csv(file_path)

    if data:
        # Побудова графіка
        plot_graph(data)

if __name__ == "__main__":
    main()
