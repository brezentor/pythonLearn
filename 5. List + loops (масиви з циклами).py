sweets = ['snickers', 'nuts', 'bounty', 'twix', 'mars', 'lion']

for x in sweets:
    print('1)', x.title()) # 1) вивело на екран кожний елемент масиву із заглавною буквою

print('---------------------------')

for x in range(0, 5, 2):
    print('2)', sweets[x]) # 2) вивело на екран перечислені елементи масиву з 0-го по 5-й елемент з кроком в 2

print('---------------------------')

p = list(range(0, 10))
print('3)', p) # 3) створив масив "р" з діапазоном від 0 до 9

print('---------------------------')


print('4)', max(p)) # 4) вивів на екран максимальне число із масиву "р"

print('---------------------------')

print('5)', min(p)) # 5) вивів на екран мінімальне число із масиву "р"

print('---------------------------')

print('6)', sum(p)) # 6) вивів на екран суму чисел із масиву "р"


print('---------------------------')

for x in p:
    p.sort(reverse=True)
    x = x * 2
    print('7)', x) # 7) вивів на екран елементи масиву "р" в оберненому алфавітному порядку, де кожне з чисел помножено на 2


print('---------------------------')

print('8)', sweets[2:5]) # 8)вивів на екран масив "солодощі", де показано з 2 по 4 елемент


print('---------------------------')

u = sweets[:]
del (sweets[2])
sweets.remove('snickers')
print('9)', sweets) # 9)скопіювавши масив "солодощі" в масив "и", потім видалив 2 елемент масиву а також елемент з назвою "снікерс" і вивів масив "солодощі" на екран

print('---------------------------')

print('10)', u) # 10) вивів на екран масив "и", де залишилась невідредагована копія масиву "солодощі"