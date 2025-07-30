import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_something(seconds):
    print(f'Sleeping {seconds} seconds ..')
    time.sleep(seconds) # Pause execution for 'seconds' duration
    return f"Done Sleeping - {seconds}"

start = time.perf_counter()

# The commented out section below demonstrates using ThreadPoolExecutor
# with `submit` and `as_completed`. This approach gives you futures
# that can be processed as they complete, regardless of the order they were submitted.

# with ThreadPoolExecutor() as executor:
#     seconds = [5, 4, 3, 2, 1]
#     # Submit each task to the executor. submit() returns a Future object
#     # which represents the eventual result of the asynchronous operation.
#     futures = [executor.submit(do_something, second) for second in seconds]
#     # as_completed yields Future objects as they complete, allowing you
#     # to process results as soon as they are ready.
#     results = as_completed(futures)
#     for result in results:
#         # result.result() retrieves the return value from the completed Future.
#         # This call will block only if the specific future hasn't completed yet,
#         # but since we are using as_completed, the futures yielded are already done.
#         print(result.result())


# This section demonstrates using ThreadPoolExecutor with `map`.
# `map` applies a function to each item in an iterable and returns
# an iterator that yields results in the order the tasks were submitted,
# even if some tasks finish earlier than others.
with ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    # executor.map() is a higher-level function that simplifies submitting
    # multiple tasks. It runs `do_something` for each item in `seconds`.
    # It returns an iterator that will yield results in the order corresponding
    # to the input `seconds` list
    # regardless of which task finishes first internally.
    results = executor.map(do_something, seconds)
    for result in results:
        # Each 'result' here is the direct return value from 'do_something'
        # for the corresponding item in 'seconds'.
        # This loop will wait for the 5-second task to finish before printing its result,
        # then the 4-second task, and so on, even if the 1-second task finished first.
        print(result)

end = time.perf_counter() # Record the ending time
print(f"Completed in {(end-start):.2f} seconds")