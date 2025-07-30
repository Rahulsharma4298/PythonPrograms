import threading
import time

lock = threading.Lock()
shared_counter = 0

def increment():
    global shared_counter
    for _ in range(100):
        with lock:
            current_value = shared_counter
            current_value += 1
            time.sleep(0.000001)
            shared_counter = current_value

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final value:", shared_counter) # race condition without lock