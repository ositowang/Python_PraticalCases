from inspect import signature


#  Basic usage of decorator


def memo(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(50))


@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count


print(climb(10, (1, 2, 3)))


# Decorator with parameter

def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kargs):
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)

        return wrapper

    return decorator


# test
@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


f(1, 2, [1, 2, 3])
