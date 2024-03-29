import hot_redis
from redis.client import Redis

from itertools import zip_longest


""" Uses implicit 6379 Redis Client connection
"""
Client = Redis()

ignore_list = ["hot_redis", "Fast", "ignore_list", "main"]


class Fast(object):
    def __init__(self, var, val):

        if type(val) == dict:
            # print('dict')
            instance = hot_redis.Dict(val, key=var)
        elif type(val) == list:
            # print('list')
            instance = hot_redis.List(val, key=var)
        elif type(val) == set:
            # print('set')
            instance = hot_redis.Set(val, key=var)
        elif type(val) == str:
            # print('str')
            instance = hot_redis.String(val, key=var)
        elif type(val) == int:
            # print('int')
            instance = hot_redis.Int(val, key=var)
        elif type(val) == None:
            # Not handled
            # print('None Not handled')
            return None
        elif callable(val):
            # print('function')
            return None
        else:
            # print("else, None:", type(val))
            return None
            # instance = hot_redis(instance)
        # print("debug: ", var, val)
        self.instance = instance


def save():
    for k in globals().keys():
        if not k.startswith("_") and k not in ignore_list:
            Fast(k, globals()[k])


def delete():

    r = Redis()

    # # iterate a list in batches of size n
    # def batcher(iterable, n):
    #     args = [iter(iterable)] * n
    #     return zip_longest(*args)

    # # in batches of 500 delete keys matching user:*
    # for keybatch in batcher(r.scan_iter('user:*'),500):
    #     print("keybatch", keybatch)
    #     r.delete(*keybatch)
    for key in r.scan_iter("*"):
        # delete the key
        r.delete(key)


def keys():
    return [i.decode() for i in Redis().keys()]


def load():
    for k in keys():
        # print('PRE-K', k)
        fetch = _get(k)
        # print('fetched: {} for {}'.format(fetch, k) )
        globals()[k] = fetch


def _get(key):
    typecheck = Client.type(key).decode()
    # print("THE TYPECHECK", typecheck, key)

    if typecheck == "string":
        # print('calling strings')
        data = Client.get(key).decode()
    elif typecheck == "hash":
        data = Client.hgetall(key)
    elif typecheck == "list":
        data = Client.lrange(key, 0, -1)
    elif typecheck == "none":
        data = None

    return data


def incrementer(counts=0):
    counts += 1


def observerables(obs):
    for k in obs:
        if k not in globals():
            # print("NOT IN GLOBALS", k)
            globals()[str(k)] = ""


def magic(func):
    def wrapper():
        load()
        func()
        save()

    return wrapper


@magic
def main():
    observerables(["phrase"])
    for i in "Recurse!":
        phrase = phrase + i


if __name__ == "__main__":
    load()

    observerables(["phrase"])

    phrase = phrase + "Recurse!\n"

    print(phrase)
    save()
