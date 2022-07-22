import os
import time
cnt=0
while True:

    with open('A.txt','a') as f:
        f.write(str(cnt)+"\n")
    cnt+=1
    time.sleep(3)



