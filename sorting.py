from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
from radar import random_date
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


def counting_sort(N):
    lower_bound, upper_bound = min(N), max(N)
    i_lower_bound = lower_bound

    counter_date = {}
    for i in range((upper_bound - lower_bound).days + 1):
        counter_date[i_lower_bound] = 0
        i_lower_bound += timedelta(days=1)

    for dt in N:
        counter_date[dt] += 1

    pos = 0
    for dt in counter_date:
        for count in range(counter_date[dt]):
            N[pos] = dt
            pos += 1

    return N




time_bubble_sort = []
time_merge_sort = []
time_sorted = []
time_counting_sort = []

for i in (10, 100, 1000, 5000):
    datetimes = []
    for j in range(i):
        datetimes.append(random_date(
            start=date(year=2021, month=5, day=31),
            stop=date(year=2022, month=8, day=31)))


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

    startTime = time.time()
    counting_sort(datetimes)
    endTime = time.time()
    time_counting_sort.append(endTime - startTime)



x = ['10', '100', '1000', '5000']

plt.plot(x, time_bubble_sort, label='bubble_sort')
plt.plot(x, time_merge_sort, label='merge_sort')
plt.plot(x, time_sorted, label='sorted')
plt.plot(x, time_counting_sort, label='counting_sort')
plt.legend()
plt.grid()
plt.show()

