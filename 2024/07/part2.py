from functools import wraps
import sys
from timeit import default_timer
from typing import Dict, List

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        end_time = default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper


def get_data(file:str) -> List[Dict[int,List[int]]]:

  data = []
  with open(file) as f:
      for line in f:
          parts = line.strip().split(":")
          data.append({int(parts[0]):[int(x) for x in parts[1].split()]})

  return data


def compute(data:List[Dict[int,List[int]]]) -> None:

    def solve(current:int, target:int, arr:List[int], ops:List[str]) -> bool:
        if current > target:
             return False
        elif arr == []:
            if current == target:
                #print(f"{target} = {' '.join(ops)}")
                return True
            else:
                return False
        else:
            if solve(current*arr[0], target, arr[1:], ops + ['*',str(arr[0])]):
                return True
            elif solve(current+arr[0], target, arr[1:], ops + ['+',str(arr[0])]):
                return True
            elif solve(int(str(current)+str(arr[0])), target, arr[1:], ops + ['||',str(arr[0])]):
                return True
            else:
                return False

    result = 0

    for d in data:
        for target, arr in d.items():
            result += target * solve(current=arr[0], target=target, arr=arr[1:], ops=[str(arr[0])])

    answer = 337041851384440
    print(result)
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    data = get_data(sys.argv[1])
    compute(data)


if __name__ == "__main__":
    main()
