from itertools import combinations

# Определяем доступные предметы
предметы = [
    {'название': 'Ингалятор', 'сокращение': 'i', 'размер': 1, 'очки': 5},
    {'название': 'Винтовка', 'сокращение': 'r', 'размер': 3, 'очки': 25},
    {'название': 'Пистолет', 'сокращение': 'p', 'размер': 2, 'очки': 15},
    {'название': 'Патроны', 'сокращение': 'a', 'размер': 2, 'очки': 15},
    {'название': 'Аптечка', 'сокращение': 'm', 'размер': 2, 'очки': 20},
    {'название': 'Нож', 'сокращение': 'k', 'размер': 1, 'очки': 15},
    {'название': 'Топор', 'сокращение': 'x', 'размер': 3, 'очки': 20},
    {'название': 'Амулет', 'сокращение': 't', 'размер': 1, 'очки': 25},
    {'название': 'Фляжка', 'сокращение': 'f', 'размер': 1, 'очки': 15},
    {'название': 'Антидот', 'сокращение': 'd', 'размер': 1, 'очки': 10},
    {'название': 'Еда', 'сокращение': 's', 'размер': 2, 'очки': 20},
    {'название': 'Арбалет', 'сокращение': 'c', 'размер': 2, 'очки': 20}
]

# Размер рюкзака (7 ячеек)
вместимость = 7

# Ингалятор обязателен, так как у Тома астма
ингалятор = [obj for obj in предметы if obj['сокращение'] == 'i'][0]

# Удаляем ингалятор из списка, так как он уже выбран
предметы = [obj for obj in предметы if obj['сокращение'] != 'i']

# Инициализируем список, который будет хранить все допустимые комбинации
допустимые_комбинации = []

# Проверяем все возможные комбинации предметов
for n in range(1, len(предметы) + 1):
    for комбинация in combinations(предметы, n):
        # Добавляем ингалятор в комбинацию
        комбинация = [ингалятор] + list(комбинация)
        
        # Проверяем, что суммарный размер не превышает вместимость рюкзака (7 ячеек)
        общий_размер = sum(obj['размер'] for obj in комбинация)
        
        # Если комбинация подходит, вычисляем очки
        if общий_размер <= вместимость:
            общие_очки = sum(obj['очки'] for obj in комбинация)
            
            # Если очки положительные, сохраняем комбинацию
            if общие_очки > 0:
                допустимые_комбинации.append((комбинация, общие_очки))

# Печатаем все допустимые комбинации и их очки
if допустимые_комбинации:
    for комбинация, очки in допустимые_комбинации:
        # Формируем вывод для каждого набора
        инвентарь = [obj['сокращение'] for obj in комбинация]
        print(f"Комбинация: {инвентарь} - Общие очки: {очки}")
else:
    print("Нет допустимых комбинаций с положительными очками выживания.")