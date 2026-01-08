import time
from datetime import datetime
 
FILE_PATH = "/detail/log.txt"
 
while True:
    with open(FILE_PATH, "a") as f:
        f.write(f"Welcome Devops {datetime.now()}\n")
    print("Python inprogress")
    time.sleep(5)
