#A normal synchronous function
import time

def fetch_data():
    time.sleep(3)  # Pretend to fetch something
    return "Data loaded"

print("Start")
data = fetch_data()   # Everything stops here for 3 seconds
print(data)
print("End")
