import time

def check_cd(last_time, cooldown):
    return time.time() - last_time >= cooldown
