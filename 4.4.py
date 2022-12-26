import os
import time
N = 100


time1, time2, time3 = 0, 0, 0
for i in range(N):
    startTime = time.time()
    os.startfile('Laboratornaya_rabota_4_1.py')
    end1Time = time.time()
    os.startfile('4.2.py')
    end2Time = time.time()
    os.startfile('4.3.py')
    endTime = time.time()
    time1 += end1Time - startTime
    time2 += end2Time - end1Time
    time3 += endTime - end2Time
print("Время работы кода 1 = ", time1/N)
print("Время работы кода 2 = ", time2/N)
print("Время работы кода 3 = ", time3/N)
