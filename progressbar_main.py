'''

ProgressBar Package
Author: Indika2000
github: https://github.com/indika2000/progressbar
Date: Jan 2017

'''

import sys, time, timeit
import multiprocessing


class progressbar():
    """ Parent Class for ProgressBar, will make abstract later"""
    def __init__(self, f):
        self.display = ['|', '/', '-', '\\']
        self.delay = 0.1
        self.func = f

    def spin_test(self, before = '', after = ''):
        write, flush = sys.stdout.write, sys.stdout.flush
        pos = -1
        while True:
            pos = (pos + 1) % len(self.display)
            msg = before + "["+ self.display[pos] + "]" + after
            write(msg)
            flush()
            write('\x08' * len(msg))
            time.sleep(self.delay)


    def __call__(self, *args, **kwargs):
        try:
            self.spinner = multiprocessing.Process(
                None, self.spin_test, args=('Calculating - ' + self.func.__name__ + ' ', '')
            )
            self.spinner.start()
            starttime = time.time()
            self.func(*args)
            endtime = time.time()
            print(" - Completed in " + str(round(endtime-starttime, 5)) +"secs" )
            self.spinner.terminate()
        except AttributeError:
            print("Progress bar error")