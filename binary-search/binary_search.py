def find(search_list, value):
    L = 0
    R = len(search_list) - 1
    while L <= R:
        mid = L + (R - L)//2
        print("Mid: ", mid)
        print("L: ", L)
        print("R: ", R)
        if search_list[mid] == value:
            return mid
        if search_list[mid] < value:
            L = mid + 1
        if search_list[mid] > value:
            R = mid - 1
    raise ValueError("value not in array")