import threading as thr
import time


def write_words(word_count: int, file_name: str) -> None:
    with open(file_name, "w") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово №{i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    start_time = time.time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time = time.time()
    print("Elapsed time:", end_time - start_time)

    start_time = time.time()
    thread1 = thr.Thread(target=write_words, args=(10, "example5.txt"))
    thread2 = thr.Thread(target=write_words, args=(30, "example6.txt"))
    thread3 = thr.Thread(target=write_words, args=(200, "example7.txt"))
    thread4 = thr.Thread(target=write_words, args=(100, "example8.txt"))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    end_time = time.time()
    print("Elapsed time:", end_time - start_time)
