import threading
import time

threads = []

def do_something(seconds):
    print(f'Sleeping {seconds} seconds ..')
    time.sleep(seconds)
    print("Done Sleeping")

start = time.perf_counter()
for _ in range(10):
    t = threading.Thread(target=do_something, args=(10, ))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"Completed in {(end-start):.2f} seconds")


# Better and easier way of doing it, see thread_pool_executor_demo.py
