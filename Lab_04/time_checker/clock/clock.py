import os
import time

dir_path = "../time/"
while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file_name = current_time.replace(":", "_") + ".txt"
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "w+") as f:
        f.write(current_time)
    time.sleep(10)

