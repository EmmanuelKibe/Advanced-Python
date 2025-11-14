#Basic example
class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Resource acquired"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type:
            print("An error occurred:", exc_val)
        return False  # Don't suppress exceptions

#Using the context manager
with MyContext() as resource:
    print(resource)

#Generator-based context manager
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('demo.txt') as f:
    f.write('Hello World!')   