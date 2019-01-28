"""
WARP PRIMES
Python code used to generate OEIS sequences:
- A323782: Prime warp entry
- A323783: Prime warp exit
Philippe Cochin - 28/01/2019 - FR
GNU General Public License v3.0
"""
import sympy
from ternary import BalancedTernary

# Result arrays
oeis323782 = []
oeis323783 = []
oeis323784 = []

# Generate primes
primes = [i for i in sympy.primerange(0, 1000)]
for index, prime in enumerate(primes):
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
    
    # Filter
    if sympy.isprime(abs(mirror)):
        oeis323782.append(prime)
        oeis323783.append(mirror)    
    else:
        oeis323784.append(prime)

# Display
# print("---Results---")
# print(f"WARP FROM (A323782):  {','.join(map(str,oeis323782))}")
# print(f"WARP TO   (A323783):  {','.join(map(str,oeis323783))}")
# print(f"ORPHANS   (A323784):  {','.join(map(str,oeis323784))}")


print("--OEIS A323782---")
print(f"Sequence:  {','.join(map(str,oeis323782))}")
for index, prime in enumerate(oeis323782):
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


print("--OEIS A323784---")
print(f"Sequence:  {','.join(map(str,oeis323784))}")
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
