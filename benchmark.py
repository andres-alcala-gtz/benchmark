import timeit

import os
import numpy
import multiprocessing


def system_call() -> None:
    os.system("echo Hello World")


def write_file(n: int) -> None:
    data = "a" * n
    with open(file="test.txt", mode="w") as f:
        f.write(data)


def read_file() -> None:
    with open(file="test.txt", mode="r") as f:
        _ = f.read()


def matrix_multiplication(n: int) -> None:
    a = numpy.random.rand(n, n)
    b = numpy.random.rand(n, n)
    _ = numpy.dot(a, b)


def structure_manipulation(n: int) -> None:
    _ = {i: i**2 for i in range(n)}


def processing_task(n: int) -> int:
    x = 0
    for i in range(n):
        x += i
    return x


def multiprocessing_task(n: int) -> None:
    processes = 2
    with multiprocessing.Pool(processes) as pool:
        pool.map(processing_task, [n] * processes)


if __name__ == "__main__":

    executions = 1000
    length = 1000

    time_sc = timeit.timeit(stmt=lambda: system_call(), number=executions) / executions
    time_wf = timeit.timeit(stmt=lambda: write_file(length), number=executions) / executions
    time_rf = timeit.timeit(stmt=lambda: read_file(), number=executions) / executions
    time_mm = timeit.timeit(stmt=lambda: matrix_multiplication(length), number=executions) / executions
    time_sm = timeit.timeit(stmt=lambda: structure_manipulation(length), number=executions) / executions
    time_mt = timeit.timeit(stmt=lambda: multiprocessing_task(length), number=executions) / executions

    print(f"system_call: {time_sc:.8f} seconds")
    print(f"write_file: {time_wf:.8f} seconds")
    print(f"read_file: {time_rf:.8f} seconds")
    print(f"matrix_multiplication: {time_mm:.8f} seconds")
    print(f"structure_manipulation: {time_sm:.8f} seconds")
    print(f"multiprocessing_task: {time_mt:.8f} seconds")
