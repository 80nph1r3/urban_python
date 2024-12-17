import multiprocessing as mp
from os import read
from time import perf_counter


def read_info(file: str) -> None:
    all_data = []
    with open(file) as f:
        for line in f:
            all_data.append(line)


if __name__ == "__main__":
    files = [f"file{i}.txt" for i in range(1, 5)]
    start = perf_counter()
    for file in files:
        read_info(file)
    end = perf_counter()
    print(end - start)

    with mp.Pool() as pool:
        pool.map(read_info, files)
    end = perf_counter()
    print(end - start)
