# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

#Будем использовать список строк с названиями чисел от 0 до 9 в порядке возрастания. 
#Индекс элемента списка будет соответствовать значению числа. 

def switch_it_up(number):
    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return words[number] if 0 <= number <= 9 else None
print(switch_it_up(1))
print(switch_it_up(3))
print(switch_it_up(10000))

#Или можно попросить ввести число
while True:
    user_input = input("Enter a number between 0 and 9: ")
    try:
        number = int(user_input)
        if 0 <= number <= 9:
            print(switch_it_up(number))
            break
        else:
            print("Invalid input. Please enter a number between 0 and 9.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 9.")
        