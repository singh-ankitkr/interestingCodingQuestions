# Find the complement of a number represented in base 10.

def find_complement(number):
    all_1 = 1
    while all_1 < number:
        all_1 = (all_1 << 1) + 1

    return all_1 ^ number


if __name__ == "__main__":
    print(find_complement(8))
    print(find_complement(10))

