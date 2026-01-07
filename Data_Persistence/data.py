import time
from datetime import datetime
 
FILE_PATH="info/log.txt"

while True:
   with open(FILE_PATH, "a") as file:
      file.write(f"Started {datetime.now()}\n")
   print("Python")
   time.sleep(5)



