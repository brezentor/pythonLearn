name = "marcus brutus"
print("1) " + name.title()) # 1) перші букви в словах заглавні
print("2) " + name.lower()) # 2) всі букви маленькі
print("3) " + name.upper()) # 3) всі букви заглавні

print("4) " + "Dear Mr. " + name.title() + '\n We want to tell you a few things:\n\tfirst\n\tsecond\n\nThats all') # 4) використання \n нової строки (аналог клавіши *enter*) та \t відступу (аналог клавіши *tab*)

name1 = "___...   mark   ...___"
print("-----------редагування тексту-------------\n" + name1 + "\n")

name1 = name1.strip("_") # 5) стерти з усіх сторін "_"
print("5) " + name1)

name1 = name1.strip(".") # 6) тепер стерти з усіх сторін "."
print("6) " + name1)

name1 = name1.strip() # 7) тепер стерти з усіх сторін "пробіли"
print("7) " + name1)

name2 = "---brut---"
print(name2)

name3 = name2.lstrip("-") # 8) стерти зліва "-"
print("8) " + name3)

name3 = name2.rstrip("-") # 9) стерти справа "-"
print("9) " + name3)

print("10) " + name, end = ' | ') # 10) end - параметр команди print, що вказує, як буде закінчуватись строка
print(name, end = '\n')
print(name, end = '')
print("---")