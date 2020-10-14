
# Find the single number in an array where all numbers are repeated.

def find_single(numbers):
    x = numbers[0]
    for num in numbers[1:]:
        x ^= num
    return x


if __name__ == '__main__':
    print(find_single([1, 4, 2, 1, 3, 2, 3]))
