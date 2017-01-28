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
        self.display = [u"\u2596", u"\u2598",u"\u2597", u"\u259A", u"\u259E"]
        self.delay = 0.5
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

    def complete_spin(self):
        sys.stdout.write('\x08')
        sys.stdout.write('\x08')
        sys.stdout.write(u"\u2588"+"]")
        sys.stdout.flush()

    def __call__(self, *args, **kwargs):
        try:
            self.spinner = multiprocessing.Process(
                None, self.spin_test, args=('Processing function - ' + self.func.__name__ + ' ', '')
            )
            self.spinner.start()
            starttime = time.time()
            self.func(*args)
            endtime = time.time()
            self.spinner.terminate()
            self.complete_spin()
            print(" - Completed in " + str(round(endtime-starttime, 5)) +"secs" )

        except AttributeError:
            print("Progress bar error")