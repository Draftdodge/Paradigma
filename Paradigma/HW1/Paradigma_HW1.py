def sort_list_imperative(arr):
    temp = 0
    for i in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr


def sort_list_declarative(arr):
    return sorted(arr)


if __name__ == '__main__':
    array = [6, 34, 1, 8, 44, 22, 22, 0, 55, 3, 9, -8]

    print(sort_list_imperative(array))

    print(sort_list_declarative(array))
