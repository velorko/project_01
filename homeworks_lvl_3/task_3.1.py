# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

# Создаем  класс "Matrix" который содержит две перменные - количество строк и количество 
# класс имеет  методы "set_value" для установки значения в ячейку матрицы 
# и "get_value" для получения значения из ячейки матрицы
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None] * columns for _ in range(rows)]

    def set_value(self, row, column, value):
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            raise IndexError("Index out of range")
        self.matrix[row][column] = value

    def get_value(self, row, column):
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            raise IndexError("Index out of range")
        return self.matrix[row][column]

    def num_rows(self):
        return self.rows

    def num_columns(self):
        return self.columns

    
 #метод для отображения матрицы на экране
    def print(self):
        for i in range(self.rows):
            row = "["
            for j in range(self.columns):
                value = str(self.get_value(i, j))
                if value is None:
                    value = "None"
                row += value + ", "
            row = row[:-2] + "]"
            print(row)

# создаем матрицу 10x10 из единиц
matrix = Matrix(10, 10)
for i in range(10):
    for j in range(10):
        matrix.set_value(i, j, 1)

# устанавливаем значение в ячейку (3, 5)
matrix.set_value(3, 5, 42)

# получаем значение из ячейки (3, 5)
print(matrix.get_value(3, 5)) # 42

# выводим количество строк и столбцов матрицы
print(matrix.num_rows()) # 10
print(matrix.num_columns()) # 10
# выводим матрицу на экран 
print(matrix.print())

