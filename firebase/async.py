from .lazy import LazyLoadProxy
from google.appengine.ext import deferred


__all__ = ['process_pool']

class ProcessPool:

    def __init__(self, size=5):
        self.size = 5

    def callback(self, callback, func, args):
        callback(func(*args))

    def apply_async(self, func, callback=None, args=[], **kwargs):
        if not callback:
            deferred.defer(func, *args, **kwargs)
        else:
            deferred.defer(self.callback, callback, func, args, **kwargs)


_process_pool = None
def get_process_pool(size=5):
    global _process_pool
    _process_pool = ProcessPool(size=size)
    return _process_pool
process_pool = LazyLoadProxy(get_process_pool)
