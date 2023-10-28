import datetime
import subprocess
import time

while True:
    current_time = datetime.datetime.now()
    print("Current time:", current_time)

    # 运行特定的Python文件
    subprocess.run(["python", "26.py"])

    # 每隔8个小时执行一次
    time.sleep(8 * 60 * 60)
