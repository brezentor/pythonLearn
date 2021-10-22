
cars = list('bmw')
marks = ['acura', 'bmw', 'citroen', 'dacia', 'elantra', 'fiat', 'getta', 'hernya', 'icarus' ,'jele', 'kia' , 'lamborgini', 'mersedes' ,'nissan', 'opel', 'parmezan', 'quatro', 'raseya', 'skoda', ' tesla', 'ultra', 'vendetta', 'wally', 'xxx', 'yurgay', 'zippo']
lenthmarks = len(marks)
num = [] # номерной массив
for k1 in range (lenthmarks):
    num.append(k1)
nummark = [] # массив "номер=машина"
for b1 in num:
    m1 = marks[b1]
    j1 = num[b1]
    if j1 == b1:
        v1 = str(j1) + '=' + str(m1)
        nummark.append(v1)
abc = list('abcdefghijklmnopqrstuvwxyz')
result = []
for an in cars:
    x1 = cars[an]
    y1 = abc[an]
    if x1 == y1:
        print(1)
    else:
        print(0)
