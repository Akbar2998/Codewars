def colour_association(arr):
    a = len(arr)
    b = []
    for i in range(a):
        dict = {}
        dict[arr[i][0]] = arr[i][1]
        b.append(dict)
    return b
