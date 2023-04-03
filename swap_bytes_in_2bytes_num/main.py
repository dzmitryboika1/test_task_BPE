import struct
from random import randint
import array

number = randint(1, 65535)


# first solution
def reverse_bytes_1(value):
    # split the two-byte number value into two single-byte ones
    low_byte = value % 256
    high_byte = value // 256

    # swap the bytes and collect the number back
    return low_byte * 256 + high_byte


# second solution
def reverse_bytes_2(value):
    return struct.unpack("H", struct.pack("H", value)[::-1])[0]


# third solution
def reverse_bytes_3(value):
    a = array.array('H', [value])
    a.tobytes()
    a.byteswap()
    a.tobytes()
    return a


if __name__ == '__main__':
    print(reverse_bytes_1(number))
    print(reverse_bytes_2(number))
    print(*reverse_bytes_3(number))



