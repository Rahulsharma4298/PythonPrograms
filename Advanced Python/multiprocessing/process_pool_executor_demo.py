import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping..{seconds}"

if __name__ == '__main__':
    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result(), f2.result())
        seconds = [5,4,3,2,1]
        # futures = [executor.submit(do_something, second) for second in seconds]
        # for result in as_completed(futures):
        #     print(result.result())

        futures = executor.map(do_something, seconds)
        for result in futures:
            print(result)


    end = time.perf_counter()
    print(f"Completed in {(end - start):.2f} seconds")
