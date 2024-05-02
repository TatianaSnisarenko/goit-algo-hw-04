from random import randint, choice, uniform, seed
from string import ascii_lowercase
import timeit
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timsort import timsort
from timeit import timeit
from math import log


def generate_random_string(length):
    return ''.join(choice(ascii_lowercase) for _ in range(length))


def generate_strings(size):
    return [generate_random_string(5) for _ in range(size)]


def generate_random_numbers(length):
    return [randint(-1000, 1000) for _ in range(length)]


def generate_random_floats(length):
    return [uniform(-1000.0, 1000.0) for _ in range(length)]


def measure_time(sort_func, arr):
    setup = f"from __main__ import {sort_func}"
    stmt = f"{sort_func}({arr})"
    return timeit(stmt, setup, number=1)


def count_increase(arr_generator, name):
    arr_min = arr_generator(100)
    arr_max = arr_generator(1000)

    insertion_min = measure_time("insertion_sort", arr_min.copy())
    merge_min = measure_time("merge_sort", arr_min.copy())
    timsort_min = measure_time("timsort", arr_min.copy())
    insertion_max = measure_time("insertion_sort", arr_max.copy())
    merge_max = measure_time("merge_sort", arr_max.copy())
    timsort_max = measure_time("timsort", arr_max.copy())

    print(f"Збільшення часу виконання сортування {name}:")
    print(f"{'Вставки:':<15}{round(insertion_max / insertion_min, 2)} разів")
    print(f"{'Злиття:':<15}{round(merge_max / merge_min, 2)} разів")
    print(f"{'Timsort:':<15}{round(timsort_max / timsort_min, 2)} разів ")
    print()


if __name__ == "__main__":

    seed(42)

    count_increase(generate_random_numbers, "цілих чисел")
    count_increase(generate_strings, "символів")
    count_increase(generate_random_floats, "з плаваючою точкою")
