from datetime import datetime, timedelta
import radar


# Готовы сортировки bubble_sort и merge_sort, остальное в процессе

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


# def counting_sort(N):
#     i_lower_bound, upper_bound = min(N), max(N)
#     lower_bound = i_lower_bound
#     if i_lower_bound < datetime(1900, 1, 1):
#         lb = i_lower_bound
#         N = [item + lb for item in N]
#         lower_bound, upper_bound = min(N), max(N)
#
#     counter_nums = [0] * (upper_bound - lower_bound + timedelta(days=1))
#     for item in N:
#         counter_nums[item - lower_bound] += timedelta(days=1)
#     pos = 0
#     for idx, item in enumerate(counter_nums):
#         num = idx + lower_bound
#         for i in range(item):
#             N[pos] = num
#             pos += 1
#     if i_lower_bound < datetime(1900, 1, 1):
#         lb = i_lower_bound
#         N = [item - lb for item in N]
#     return N




datetime_10 = []
for i in range(10):
    datetime_10.append(radar.random_datetime(start='2000-01-21', stop='2020-12-31T23:59:59'))
print("До ", datetime_10)

print("bubble_sort ", bubble_sort(datetime_10))
print("merge_sort ", merge_sort(datetime_10))
# print("counting_sort ", counting_sort(datetime_10))


