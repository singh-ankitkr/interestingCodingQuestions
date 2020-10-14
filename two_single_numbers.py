# Get 2 single numbers from an array.


# XOR method.
def find_two_single_numbers(numbers):
    x_n = numbers[0]
    for num in numbers[1:]:
        x_n ^= num

    first_set = 1
    while x_n & first_set == 0:
        first_set <<= 1

    num_g1, num_g2 = [], []
    for num in numbers:
        if num & first_set:
            num_g1.append(num)
        else:
            num_g2.append(num)

    n1 = 0
    for num in num_g1:
        n1 ^= num
    n2 = 0
    for num in num_g2:
        n2 ^= num

    return n1, n2


def two_single_number_set_method(numbers):
    temp_set = set()
    for num in numbers:
        if num in temp_set:
            temp_set.remove(num)
        else:
            temp_set.add(num)

    return temp_set


if __name__ == "__main__":
    print(find_two_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    print(find_two_single_numbers([2, 1, 3, 2]))
    print(two_single_number_set_method([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    print(two_single_number_set_method([2, 1, 3, 2]))
