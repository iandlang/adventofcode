from functools import cache
import numpy as np
from pprint import pprint as pp
import sys
from decorators.timer import timer


def compute() -> None:

    answer = [2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]

    A0 = 0
    inc = 1
    search = 1
    print(f"incrementing by {inc} looking for {search} characters")

    while True:

        A = A0
        B = 0
        C = 0
        output = []

        while A > 0:

            B = A % 8
            B = B ^ 1
            C = A // 2**B
            B = B ^ 4
            A = A // 8
            B = B ^ C
            output.append(B % 8)

            if output != answer[:len(output)]:
                break
            elif len(output) == search:
                print(f"A0:{A0} found match for first {len(output)} digits output:{output}")
                if len(output) == 16:
                    break
                elif len(output) == 7:
                    inc = 1
                else:
                    inc *= 8
                search += 1
                print(f"incrementing by {inc} looking for {search} characters")

        if output == answer:
            break

        A0 += inc

    result = A0
    print(A0)

    answer = 202322936867370
    if answer:
        assert(result == answer)


@timer
def main() -> None:

    compute()


if __name__ == "__main__":
    main()
