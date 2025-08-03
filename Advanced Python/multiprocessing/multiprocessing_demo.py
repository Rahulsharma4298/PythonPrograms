import multiprocessing
import time

processes = []

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("Done sleeping")


if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(10):
        process = multiprocessing.Process(target=do_something, args=(1.5, ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end = time.perf_counter()

    print(f"Completed in {(end-start):.2f} seconds")

