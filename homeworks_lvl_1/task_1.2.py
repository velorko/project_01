# Задача 1.2.

import random
from datetime import datetime, timedelta

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат "минуты:секунды" 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Выбираем три случайные песни my_favorite_songs, метод random.sample() трех случайных песен
random_songs = random.sample(my_favorite_songs, 3)

# Считаем общее время звучания
total_duration = sum([song[1] for song in random_songs])

# Преобразуем общее время звучания в формат времени
total_duration_time = timedelta(minutes=total_duration)

# Выводим результат в строку формата "минуты:секунды" 
print(f"Пункт A. Три песни звучат {total_duration_time.seconds // 60} минут {total_duration_time.seconds % 60} секунд")

# Пункт B.
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат "минуты:секунды" 

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Выбираем три случайные песни c помощью метода list() преобразуется словарь в список кортежей
random_songs_dict = random.sample(list(my_favorite_songs_dict.items()), 3)

# Считаем общее время звучания так же, как и в пункте A
total_duration_dict = sum([song[1] for song in random_songs_dict])

# Преобразуем общее время звучания в формат времени
total_duration_time_dict = timedelta(minutes=total_duration_dict)

# Выводим результат в строку формата "минуты:секунды" 
print(f"Пункт A. Три песни звучат {total_duration_time_dict.seconds // 60} минут {total_duration_time_dict.seconds % 60} секунд")


# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random

# Пример генерации случайных песен из списка my_favorite_songs 
# выбираем три индекса элементов списка, после чего выбранные элементы записываются в новый список
random_song_indices = random.sample(range(len(my_favorite_songs)), 3)
random_songs_c = [my_favorite_songs[i] for i in random_song_indices]
print(f"Пункт C. Случайно сгенерированные три песни:", random_songs_c)

# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
# Преобразуем минуты и секунды в формат времени 
# используется функция divmod() для вычисления минут и секунд 
total_duration_minutes, total_duration_seconds = divmod(total_duration, 1)
total_duration_formatted = datetime.strptime(f"{int(total_duration_minutes):02}:{int(total_duration_seconds*60):02}", "%M:%S")

# Выводим результат
print(f"Пункт D. Три песни из пункта А звучат {total_duration_formatted.strftime('%M:%S')}.")