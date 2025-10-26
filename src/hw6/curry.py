from functools import wraps

def curry(func, arity):
    """Преобразует функцию в каррированную форму"""
    if not callable(func):
        raise TypeError("First argument must be a function")
    if not isinstance(arity, int):
        raise TypeError("Arity must be a number")
    if arity < 0:
        raise ValueError("Arity must be not negativce")
    if func.__code__.co_argcount < arity:
        raise ValueError("Arity more than a function's arguments")
    
    if arity == 0:
        return lambda: func()

    def inner(arg_stack):
        @wraps(func)
        def curried(arg):
            new_stack = arg_stack + [arg]
            if len(new_stack) == arity:
                return func(*new_stack)
            return inner(new_stack)
        return curried

    return inner([])


def uncurry(curried_func, arity):
    """Преобразует каррированную функцию обратно в обычную."""
    if not callable(curried_func):
        raise TypeError("First argument must be a function")
    if not isinstance(arity, int):
        raise TypeError("Arity must be a number")
    if arity <= 0:
        raise ValueError("Arity must be a positive number")

    @wraps(curried_func)
    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Expected {arity} arguments, got {len(args)}")
        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried




