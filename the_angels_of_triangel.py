from typing import List

import math
def checkio(a: int, b: int, c: int) -> List[int]:
    if a + b > c and a + c > b and b + c > a:
        ang_a = math.acos(((b * b + c * c - a * a) / (2 * b * c)))
        ang_b = math.acos((c * c + a * a - b * b) / (2 * a * c))
        ang_c = math.acos((b * b + a * a - c * c) / (2 * a * b))
        return sorted([round(math.degrees(ang_a)), round(math.degrees(ang_b)), round(math.degrees(ang_c))])
    else:
        return [0, 0, 0]
    #replace this for solution


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")


#A=arccos((b^2+c^2-a^2)/2bc)