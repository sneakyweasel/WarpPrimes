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
oeis323782 = [1]
oeis323783 = [1]

# Generate primes
primes = [i for i in sympy.primerange(0, 1000)]

for prime in primes:
    # Convert to balanced ternary notation string
    BTprime = str(BalancedTernary(prime))
    # Reverse string
    BTmirror = BTprime[::-1]
    # Convert from balanced ternary notation string
    mirror = BalancedTernary(BTmirror).to_int()

    # Filter
    if sympy.isprime(abs(mirror)):
        oeis323782.append(prime)
        oeis323783.append(mirror)
        print(
            f"NUM: {prime}\t{BTprime}\t|\t{BTmirror}\t{mirror}")

# Display
print("---Results---")
print(f"WARP FROM (A323782):  {','.join(map(str,oeis323782))}")
print(f"WARP TO   (A323783):  {','.join(map(str,oeis323783))}")
