def move_zeros(array):
    b = []
    for i in range (len(array)):
        if (array[i] == 0):
            b.append(array[i])
    for j in range (len(b)):
        array.remove(0)
    array.extend(b)
    return array


array = [0,0]
print(move_zeros(array))