def pick_peaks(arr):
    res = {}
    pos = []
    peaks = []

    for i in range(len(arr)):
        if ((i == 0) or (i == len(arr) - 1)):
            pass
        else:
            if (((arr[i] > arr[i - 1]) and (arr[i] > arr[i + 1])) or (
                    (arr[i] > arr[i - 1]) and (arr[i] == arr[i + 1]) and (arr[i] > arr[i + 2]) and (
                    arr[i] != arr[-1]))):
                pos.append(i)
                peaks.append(arr[i])
            elif ((arr[i] > arr[i - 1]) and (arr[i] == arr[i + 1]) and (arr[i] == arr[i + 2]) and (arr[i] != arr[-1])):
                pos.append(i)
                peaks.append(arr[i])


    res['pos'] = pos
    res['peaks'] = peaks
    return  res


arr = [1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]
print(pick_peaks(arr))

# в итоге не правильно

#правильное решение:
"""def pick_peaks(arr):
    peaks = []
    pos = []
    res = {"pos": [], "peaks": []}

    for i in range(1, len(arr)):
        if (arr[i] > arr[i - 1]):
            peaks = [arr[i]]
            pos = [i]

        elif (arr[i] < arr[i - 1]):
            res["peaks"] += peaks
            res["pos"] += pos
            peaks = []
            pos = []
    return res"""