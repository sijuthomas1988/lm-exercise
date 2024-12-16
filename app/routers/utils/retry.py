import time


def retry(fun, max_tries=10):
    for i in range(max_tries):
        try:
           time.sleep(0.3)
           fun()
           break
        except Exception:
            continue