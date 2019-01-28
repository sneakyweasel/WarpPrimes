"""
WARP PRIMES
Python code used to generate OEIS sequences:
- A323782: Prime warp entry
- A323783: Prime warp exit
- A323784: Prime warp to non-prime
Philippe Cochin - 28/01/2019 - FR
GNU General Public License v3.0
"""
import sympy
from ternary import BalancedTernary

# Result arrays
oeis323782 = []
oeis323783 = []
oeis323784 = []


# def a134028(n):
#     # https://oeis.org/A134028 : Reversal of n in balanced ternary representation
#     if n == 0:
#         return 0
#     s = []
#     x = 0
#     while n > 0:
#         x = n % 3
#         n = n/3
#         if x == 2:
#             x = -1
#             n += 1
#         s += [x, ]
#     l = s[::-1]
#     t = 0
#     for i in range(len(l)):
#         t += l[i]*3**i
#     return t


def a117966(n):
    # https://oeis.org/A117966 : Balanced ternary enumeration (or balanced ternary representation) of integers; write n in ternary and then replace 2's with (-1)'s.
    if n == 0:
        return 0
    if n % 3 == 0:
        return 3*a117966(n/3)
    elif n % 3 == 1:
        return 3*a117966((n - 1)/3) + 1
    else:
        return 3*a117966((n - 2)/3) - 1


# Generate primes
ulimit = 1000
primes = [i for i in sympy.primerange(0, ulimit)]

# Choose to loop primes or integers
# for index, prime in enumerate(range(ulimit)):
for index, prime in enumerate(primes):

    # Convert to balanced ternary notation string
    BTprime = str(BalancedTernary(prime))
    # Reverse string
    BTmirror = BTprime[::-1]
    # Convert from balanced ternary notation string
    mirror = BalancedTernary(BTmirror).to_int()
    # Prime factors of mirror
    primefactors = sympy.primefactors(mirror)

    # Test ternary conversion code from A117966
    ternA117966 = a117966(prime)
    # Test ternary conversion code from A134028 (not working)
    # ternA134028 = a134028(prime)

    # Github markdown formatting
    format_BTprime = " ".join(BTprime)
    format_BTmirror = " ".join(BTmirror)
    # print(f"| {prime} | {ternA117966} | {mirror} | {ternA134028} |")

    # Filter
    if sympy.isprime(abs(mirror)):
        oeis323782.append(prime)
        oeis323783.append(mirror)
    else:
        print(f"| {index} | {prime} | {ternA117966} | {format_BTprime} | {format_BTmirror} | {mirror} | {primefactors} |")
        oeis323784.append(prime)

# print("--OEIS A323782---")
# print(f"Sequence:  {','.join(map(str,oeis323782))}")
# for index, prime in enumerate(oeis323782):
#     # Convert to balanced ternary notation string
#     BTprime = str(BalancedTernary(prime))
#     # Reverse string
#     BTmirror = BTprime[::-1]
#     # Convert from balanced ternary notation string
#     mirror = BalancedTernary(BTmirror).to_int()
#     # Prime factors of mirror
#     primefactors = sympy.primefactors(mirror)

#     # Github markdown formatting
#     format_BTprime  = " ".join(BTprime)
#     format_BTmirror = " ".join(BTmirror)
#     print(f"| {index} | {prime} | {format_BTprime} | {format_BTmirror} | {mirror} | {primefactors} |")


print("--OEIS A323784---")
sequence_260 = ','.join(map(str,oeis323784))[0:260:]
print(f"Sequence:  {sequence_260}")
print("\n")
print(f"|index|prime|BT representation|reversed BT|warped prime|prime factors|")
print(f"| --- | --- | --- | --- | --- | --- |")

for index, prime in enumerate(oeis323784):
    # Convert to balanced ternary notation string
    BTprime = str(BalancedTernary(prime))
    # Reverse string
    BTmirror = BTprime[::-1]
    # Convert from balanced ternary notation string
    mirror = BalancedTernary(BTmirror).to_int()
    # Prime factors of mirror
    primefactors = sympy.primefactors(mirror)

    # Github markdown formatting
    format_BTprime  = " ".join(BTprime)
    format_BTmirror = " ".join(BTmirror)
    print(f"| {index} | {prime} | {format_BTprime} | {format_BTmirror} | {mirror} | {primefactors} |")


# Display results
# print("---Results A323782 & A323783---")
# print(f"WARP FROM (A323782):  {','.join(map(str,oeis323782))}")
# print(f"WARP TO   (A323783):  {','.join(map(str,oeis323783))}")
# print(f"Percentage of warp primes below {ulimit}: {len(oeis323782)} / {index} = {(len(oeis323782)/index) * 100} %")
# print("---Results A323784---")
# print(f"ORPHANS   (A323784):  {','.join(map(str,oeis323784))}")
# print(f"Percentage of warp primes below {ulimit}: {len(oeis323784)} / {index} = {(len(oeis323784)/index) * 100} %")
