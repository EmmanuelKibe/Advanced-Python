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
   