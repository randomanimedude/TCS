import os
import time

dir_path = "../time/"
while True:
    files = os.listdir(dir_path)
    if files:
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, "r") as f:
                file_content = f.read()
            print(f"File name: {file_name}, content: {file_content}")
    time.sleep(30)
    print("ж(")

