import pnmt
import time

n = int(input("please enter num: "))
t = int(input("please enter thread count: "))

start_time = time.time()

pnmt.PerfectNumber(n, t)

print("--- %s Seconds ---" % (time.time() - start_time))
