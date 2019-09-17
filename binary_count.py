def checkio(number: int) -> int:
    binary = str(bin(number))
    ones = len([x for x in binary if x == '1'])
    return ones

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
