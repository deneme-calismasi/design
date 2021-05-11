import time

starttime = time.time()

print(starttime)
while True:
    print("tick")
    time.sleep(2.0 - ((time.time() - starttime) % 2.0))
