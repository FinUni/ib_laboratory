import matplotlib.pyplot as plt
import radar
import time


def bubble_sort(N):
    for i in range(len(N) - 1):
        F = 0
        for j in range(len(N) - 1):
            if N[j] > N[j + 1]:
                N[j], N[j + 1] = N[j + 1], N[j]
                F = 1
        if F == 0:
            break
    return N


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(N):
    if len(N) <= 1:
        return N
    mid = len(N) // 2

    left_list = merge_sort(N[:mid])
    right_list = merge_sort(N[mid:])

    return merge(left_list, right_list)



time_bubble_sort = []
time_merge_sort = []
time_sorted = []

for i in (10, 100, 1000, 5000):
    datetimes = []
    for j in range(i):
        datetimes.append(radar.random_datetime(start='2000-01-21', stop='2020-12-31T23:59:59'))

    startTime = time.time()
    bubble_sort(datetimes)
    endTime = time.time()
    time_bubble_sort.append(endTime - startTime)

    startTime = time.time()
    merge_sort(datetimes)
    endTime = time.time()
    time_merge_sort.append(endTime - startTime)

    startTime = time.time()
    sorted(datetimes)
    endTime = time.time()
    time_sorted.append(endTime - startTime)



x = ['10', '100', '1000', '5000']
y_for_bubble_sort = time_bubble_sort
y_for_merge_sort = time_merge_sort
y_for_sorted = time_sorted

plt.plot(x, y_for_bubble_sort, label='bubble_sort')
plt.plot(x, y_for_merge_sort, label='merge_sort')
plt.plot(x, y_for_sorted, label='sorted')
plt.legend()
plt.grid()
plt.show()

