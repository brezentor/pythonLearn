towns = ['Kiev', 'Lviv' , 'Odessa', 'Donetsk', 'Luhansk', 'Dymer', 'Poltava', 'Dnipro']
print("1)", towns) # 1) створення массиву

print("2)", towns[4]) # 2) виведення на екран 4 елементу масиву (Луганськ)

print("3)", towns[2].lower()) # 3) виведення на екран 2 елементу масиву з маленькими буквами (Одеса)

towns.append(towns[1].lower())
print("4)", towns) # 4) додати в кінець масиву 1 елемент масиву з маленькими буквами (Львів)

towns.append('Kherson')
print("5)", towns) # 5) додати в кінець масиву "Херсон"

towns.insert(3, 'Rivne')
print("6)", towns) # 6) додати в масив на місце 3 елементу  - елемент "Рівне"

del (towns[4])
print("7)", towns) # 7) видалити 4 елемент масиву

towns.remove('Dnipro')
print("8)", towns) # 8) видалити елемент масиву "Дніпро" (якшо буде декілька таких - видалить тільки один і перший елемент)

deleted = towns.pop()
print("9)", deleted) # 9) показує який елемент видалить (.pop() - означає, що видалить з кінця масиву)
print("10)", towns) # 10) покаже масив уже з видаленим елементом

towns.sort()
print("11)", towns) # 11) сортує в алфавітному порядку

towns.sort(reverse=True)
print("12)", towns) # 12) сортує в оберненому алфавітному порядку