def print_numbers_in_line(start, end):
    """
    This function prints numbers in a line from start to end.
    """
    for num in range(start, end + 1):
        print(num, end=" ")

# Example usage:
start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))

print_numbers_in_line(start_number, end_number)


def s(inp):
    return sorted(inp)

out = input("Enter a alphanum value")
final=s(out)
print(final)


def evenOdd(num):
    if num % 2 == 0:
        return "{} even ".format(num)
    else:
        return " {} odd".format(num)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = list(map(evenOdd, l))
print(p, end=' ')


li = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, li))
print(even)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using filter() with lambda to filter out even numbers
filtered_numbers = list(map(lambda x: x % 2 != 0, numbers))
print("Original list:", numbers)
print("Filtered odd numbers:", filtered_numbers)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
print(even_odd)