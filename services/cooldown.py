import time

DAY = 86400

def check_cd(last):
    return time.time() - last >= DAY
