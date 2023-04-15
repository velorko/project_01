# Задача 1.1.

# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца

# Первый трек
first_song = my_favorite_songs.split(',')[0].strip()
print('Первый трек: ', first_song)

# Последний трек
last_song = my_favorite_songs.split(',')[-1].strip()
print('Последний трек: ', last_song)

# Второй трек
second_song = my_favorite_songs.split(',')[1].strip()
print('Второй трек: ', second_song)

# Второй с конца трек
second_to_last_song = my_favorite_songs.split(',')[-2].strip()
print('Второй с конца трек: ', second_to_last_song)