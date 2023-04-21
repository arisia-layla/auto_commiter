import os
import datetime
import time
dt = str(datetime.datetime.now())
# print(dt[21:27])

for i in range(1, 10000, 1):
    time.sleep(10)
    commit = 'git commit -m "commit-timeline"'
    commit = commit.replace("timeline", dt[21:27])
    print(commit)
    # os.getcwd()
    os.chdir(os.getcwd())
    os.system('git add .')
    os.system(commit)
    os.system('git push -u origin main')