# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace('!', '')
print("Пункт A. Входные данные: ""Hi! Hello!"" Выходные данные: ",remove_exclamation_marks ("Hi! Hello!"))
print("Пункт A. Входные данные: "" "" Выходные данные: ",remove_exclamation_marks (" "))
print("Пункт A. Входные данные: ""Oh, no!!!"" Выходные данные: ",remove_exclamation_marks ("Oh, no!!!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith('!'):
        return s[:-1] + s[-1:].replace('!', '', 1)
    else:
        return s
print("Пункт B. Входные данные: ""Hi!"" Выходные данные: ",remove_last_em ("Hi!"))
print("Пункт B. Входные данные: ""Hi!!!"" Выходные данные: ",remove_last_em ("Hi!!!"))
print("Пункт B. Входные данные: ""!Hi"" Выходные данные: ",remove_last_em ("!Hi"))
# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    new_words = []
    for word in words:
        if word.count('!') != 1:
            new_words.append(word)
    return ' '.join(new_words)

print("Пункт C. Входные данные: ""Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi!"))
print("Пункт C. Входные данные: ""Hi! Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi! Hi!"))
print("Пункт C. Входные данные: ""Hi! Hi! Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi! Hi! Hi!"))
print("Пункт C. Входные данные: ""Hi Hi! Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi Hi! Hi!"))
print("Пункт c. Входные данные: ""Hi! !Hi Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi! !Hi Hi!"))
print("Пункт C. Входные данные: ""Hi! Hi!! Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi! Hi!! Hi!"))
print("Пункт C. Входные данные: ""Hi! !Hi! Hi!"" Выходные данные: ",remove_word_with_one_em ("Hi! !Hi! Hi!"))