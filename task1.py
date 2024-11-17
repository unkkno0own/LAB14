import matplotlib.pyplot as plt  
import numpy as np

# Генерація значень x в діапазоні від -5 до 5
x = np.linspace(-5, 5, 1000)

# Обчислення значень функції Y(x) = (1/x) * sin(5x)
y = (1 / x) * np.sin(5 * x)

# Побудова графіка
plt.plot(x, y, label=r'$\frac{1}{x} \sin(5x)$', color="green", linewidth=2)

# Заголовок графіка
plt.title(r'Графік функції $Y(x) = \frac{1}{x} \sin(5x)$', fontsize=15)

# Позначення осей
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

# Легенда для графіка
plt.legend()

# Включення сітки
plt.grid(True)

# Виведення графіка
plt.show()
