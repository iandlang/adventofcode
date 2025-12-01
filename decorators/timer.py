from functools import wraps
from timeit import default_timer
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec('P')
T = TypeVar('T')

def timer(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = default_timer()
        result = func(*args, **kwargs)
        end_time = default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper
