
import hot_redis 

ignore_list = ["hot_redis", "Fast", "ignore_list", "main"]

class Fast(object):

    def __init__(self, object):

        if type(object) == dict:
            print('dict')
            instance = hot_redis.Dict(object)
        elif type(object) == list:
            print('list')
            instance = hot_redis.List(object)
        elif type(object) == set:
            print('set')
            instance = hot_redis.Set(object)
        elif type(object) == str:
            print('str')
            instance = hot_redis.String(object)
        else:
            print(type(object))
            # instance = hot_redis(instance)
        self.instance = instance

        self.instance = object

Fast([]) 
Fast('foo')
Fast({})

# List                list                          list
# Set                 set                           set
# Dict                dict                          hash
# String              string                        string      Mutable - string methods that normally create a new string object in Python will mutate the string stored in Redis
# ImmutableString     string                        string      Immutable - behaves like a regular Python string
# Int                 int                           int
# Float               float                         float
#     pass

"""

List                list                          list
Set                 set                           set
Dict                dict                          hash
String              string                        string      Mutable - string methods that normally create a new string object in Python will mutate the string stored in Redis
ImmutableString     string                        string      Immutable - behaves like a regular Python string
Int                 int                           int
Float               float                         float
Queue               Queue.Queue                   list
LifoQueue           Queue.LifoQueue               list
SetQueue            N/A                           list + set  Extension of ``Queue`` with unique members
LifoSetQueue        N/A                           list + set  Extension of ``LifoQueue`` with unique members
BoundedSemaphore    threading.BoundedSemaphore    list        Extension of ``Queue`` leveraging Redis' blocking list pop operations with timeouts, while using Queue's ``maxsize`` arg to provide BoundedSemaphore's ``value`` arg
Semaphore           threading.Semaphore           list        Extension of ``BoundedSemaphore`` without a queue size
Lock                threading.Lock                list        Extension of ``BoundedSemaphore`` with a queue size of 1
RLock               threading.RLock               list        Extension of ``Lock`` allowing multiple ``acquire`` calls
DefaultDict         collections.DefaultDict       hash
MultiSet            collections.Counter           hash
"""

