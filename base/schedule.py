from time import sleep

from currency.currency import rain_check

def scheduler():
    rain_check()

def task():
    n = 1
    print('starting scheduled tasks')
    sleep(5)
    while 1:
        scheduler()

        print(f'Check {n} complete');n+=1;sleep(60)
        