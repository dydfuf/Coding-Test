def solution(sorting_list):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = sorting_list[(low + high) // 2]
        while low <= high:
            while sorting_list[low] < pivot:
                low += 1
            while sorting_list[high] > pivot:
                high -= 1
            if low <= high:
                sorting_list[low], sorting_list[high] = sorting_list[high], sorting_list[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(sorting_list) - 1)


if __name__ == "__main__":
    sorting_list = [5, 4, 3, 2, 1, 8, 7, 9, 6,1]
    solution(sorting_list)
    print(sorting_list)