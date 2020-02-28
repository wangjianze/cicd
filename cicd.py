#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import threading
from functools import wraps

class MyThread(threading.Thread):
    def run(self):
        self.result = self._target(*self._args, **self._kwargs)

    def get_result(self,timeout=None):
        threading.Thread.join(self,timeout)
        try:
            return self.result
        except Exception:
            return None

def timeout(times):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            # ret = func(*args,**kwargs)
            t = MyThread(target=func, args=args,kwargs=kwargs,daemon=True)
            t.start()
            ret = t.get_result(times)
            return ret
        return inner
    return wrapper





