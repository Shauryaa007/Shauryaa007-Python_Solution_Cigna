import math
import itertools
import datetime

# ------------------ PROGRAM FUNCTIONS for updated branches ------------------

# 1. Leap Year
def leap_year():
    year = int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

# 2. Perfect Square
def perfect_square():
    n = int(input("Enter the number: "))
    if math.isqrt(n) ** 2 == n:
        print("Perfect Square")
    else:
        print("Not Perfect Square")

# 3. Sum/Product/Average/Zero count
def stats_20_numbers():
    sump = sumn = evensum = evencnt = cnt0 = 0
    pro = 1
    for i in range(20):
        a = int(input(f"Enter no {i+1}: "))
        if a == 0:
            cnt0 += 1
        elif a > 0:
            sump += a
        else:
            sumn += a
        if a % 2 == 0 and a != 0:
            evensum += a
            evencnt += 1
        elif a % 2 != 0:
            pro *= a
    print(f"Sum of positives = {sump}")
    print(f"Sum of negatives = {sumn}")
    print(f"Average of evens = {evensum/evencnt if evencnt>0 else 0}")
    print(f"Product of odds = {pro}")
    print(f"Number of zeros = {cnt0}")

# 4. Search Key in List
def search_key():
    key = int(input("Enter key: "))
    lst = [1,2,3,4,5]
    for i in lst:
        print(i)
        if i == key:
            print("Found key")
            break
    else:
        print("Key not found")

# 5. Factorial
def factorial():
    def fact(n):
        return 1 if n in (0,1) else n*fact(n-1)
    n = int(input("Enter number: "))
    print("Factorial =", fact(n))

# 6. Palindrome String
def palindrome():
    s = input("Enter string: ")
    print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 7. Prime Number
def prime_check():
    n = int(input("Enter number: "))
    if n < 2:
        print("Not Prime")
        return
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

# 8. Flatten Nested List
def flatten_list():
    my_list = [[1], [2, 3], [4, 5, 6, 7],[8, 9],[0]]
    flat = [ele for l in my_list for ele in l]
    print("Flattened List:", flat)

# 9. Alternate Reverse
def alternate_reverse():
    lst = [1,2,3,4,5,6,7,8,9,10]
    print("Alternate elements in reverse:", lst[::-2])

# 10. Even numbers using comprehension
def even_numbers():
    numbers = [1,4,7,10,13,16,19,20,25]
    evens = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", evens)

# 11. Remove Duplicates
def remove_duplicates():
    lst = [1,2,3,4,1,2,3,4]
    print("Unique list:", list(dict.fromkeys(lst)))

# 12. Largest of 3 Numbers
def largest_of_three():
    a, b, c = int(input("a=")), int(input("b=")), int(input("c="))
    print("Largest:", max(a,b,c))

# 13. Positive/Negative/Zero
def pos_neg_zero():
    n = int(input("Enter number: "))
    if n > 0: print("Positive")
    elif n < 0: print("Negative")
    else: print("Zero")

# 14. Even/Odd Labels (List comprehension)
def even_odd_labels():
    lst = [1,2,3,4,5,6,7,8,9]
    labels = ["even" if x%2==0 else "odd" for x in lst]
    print(labels)

# 15. Element in List
def element_in_list():
    n = int(input("Enter number: "))
    lst = [1,2,3,4,5,7,0]
    print("Found" if n in lst else "Not Found")

# 16. Flatten again with itertools
def flatten_itertools():
    my_list = [[1], [2, 3], [4, 5, 6, 7],[8, 9],[0]]
    print(list(itertools.chain.from_iterable(my_list)))

# 17. Print Date with Separator
def print_date():
    day, mon, yr = 21, 12, 2012
    print(f"{day}-{mon}-{yr}")

# 18. Add two vars + input
def add_vars_input():
    a, b = 10, 20
    c = int(input("Enter another number: "))
    print("Sum =", a+b+c)

# 19. Dictionary Iteration
def dict_iteration():
    dt = {'a': 'Naruto', 'b': 'Onepiece', 'c': 'Bleach'}
    for k,v in dt.items():
        print(f"{k} -> {v}")

# 20. Alternate values in reverse (again)
def alternate_list():
    lst = [1,2,3,4,5,6,7,8,9,0]
    print(lst[::-2])

# ------------------ MENU ------------------

def main():
    programs = {
        1: leap_year,
        2: perfect_square,
        3: stats_20_numbers,
        4: search_key,
        5: factorial,
        6: palindrome,
        7: prime_check,
        8: flatten_list,
        9: alternate_reverse,
        10: even_numbers,
        11: remove_duplicates,
        12: largest_of_three,
        13: pos_neg_zero,
        14: even_odd_labels,
        15: element_in_list,
        16: flatten_itertools,
        17: print_date,
        18: add_vars_input,
        19: dict_iteration,
        20: alternate_list,
    }

    while True:
        print("\n=== Python Practice Programs ===")
        for k in programs:
            print(f"{k}. Program {k}")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
