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
index = 0
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
        index += 1
        # Markdown formatting
        format_BTprime  = " ".join(BTprime)
        format_BTmirror = " ".join(BTmirror)
        print(f"|{index}|{prime}|{format_BTprime}|{format_BTmirror}|{mirror}|{mirror}|")

    else:
        oeis323784.append(mirror)
        # Markdown formatting
        format_BTprime  = " ".join(BTprime)
        format_BTmirror = " ".join(BTmirror)
        primefactors = sympy.primefactors(mirror)
        print(f"|{index}|{prime}|{format_BTprime}|{format_BTmirror}|{mirror}|{primefactors}|")


# Display
print("---Results---")
print(f"WARP FROM (A323782):  {','.join(map(str,oeis323782))}")
print(f"WARP TO   (A323783):  {','.join(map(str,oeis323783))}")

length = "1, -2, -11, 7, -5, 13, -29, -17, 37, 31, 43, -83, -101, 61, -89, 73, -53, -71, -59, 103, -173, 313, -353, 241, -137, -263, 223, 331, 277, 181, -269, 163, -179, -233, 199, -347, 139, 193, -311, -149, 367, 853, 691, -929, -443, -983, 421, -389, -839, 457, -677, -569, 727, 1051, -947, 709, 547, -479, -857, 601, 1087, 613, 883, -467, 379, 541, -809, 487, 811, 919, 757, -863, -827, -719, 739, 1063, -773, -449, 373, -599, 859, -761, 1021, 643, -977, 751, -383, -509, -887, -401 "
print(length[0:260:])