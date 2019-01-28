# Warp Primes

- This repository is the Python 3 code used to generate Warp Primes.
- Warp primes are prime numbers whose reverse of the balanced ternary representation is also prime or -prime.
- Balanced ternary notation might allow insight into relations hidden by classical notation.
- See [Wikipedia - Balanced Ternary]( https://en.wikipedia.org/wiki/Balanced_ternary)

## Warp operator

The warp operator is an unary numerical operator described in A134028: Reversal of n in balanced ternary representation as:

- Convert "classical" number to balanced ternary representation
- Reverse balanced ternary representation
- Convert reversed balanced ternary representation to "classical" number

```python
def a(n):
    if n==0: return 0
    s=[]
    x=0
    while n>0:
        x=n%3
        n=n/3
        if x==2:
            x=-1
            n+=1
        s+=[x, ]
    l=s[::-1]
    t=0
    for i in xrange(len(l)): t+=l[i]*3**i
    return t
```

## How-to

```shell
pip install sympy
py -3 warp.py
```

## Corresponding OEIS sequences

- Warp Entry   : [OEIS A323782](https://oeis.org/A323782)
- Warp Exit    : [OEIS A323783](https://oeis.org/A323783)
- Warp Orphans : [OEIS A323784](https://oeis.org/A323784)

## Related OEIS sequences

- Subsequence of A134028: Reversal of n in balanced ternary representation.
- Supersequence of A???: Prime palindrome in balanced ternary representation.
- To complete...

## A323782 & A323783: Prime warpers (primes that warp to other primes)

### A323782 Sequence

2,5,7,11,13,17,29,31,37,43,53,59,61,71,73,83,89,101,103,137,139,149,163,173,179,181,193,199,223,233,241,263,269,277,311,313,331,347,353,367,373,379,383,389,401,421,443,449,457,467,479,487,499,509,541,547,569,599,601,607,613,643,677,691,709,719,727,739,751,757,761,773,809,811,823,827,839,853,857,859,863,877,883,887,919,929,947,977,983

### A323782 Stats

- Percentage of warp primes below 10: 3 / 3 = 100.0 %
- Percentage of warp primes below 100: 17 / 24 = 70.83333333333334 %
- Percentage of warp primes below 1000: 89 / 167 = 53.293413173652695 %
- Percentage of warp primes below 10000: 474 / 1228 = 38.59934853420196 %
- Percentage of warp primes below 100000: 2870 / 9591 = 29.923886977374618 %
- Percentage of warp primes below 1000000: 18684 / 78497 = 23.80218352293718 %
- Percentage of warp primes below 10000000: 133077 / 664578 = 20.024286088314692 %
- Percentage of warp primes below 100000000: 996574 / 5761454 = 17.297265586082958 %

### A323782 Table

|index|prime|BT representation|reversed BT|warped prime|prime factors|
| --- | --- | --- | --- | --- | --- |
| 0 | 2 | + - | - + | -2 | [2] |
| 1 | 5 | + - - | - - + | -11 | [11] |
| 2 | 7 | + - + | + - + | 7 | [7] |
| 3 | 11 | + + - | - + + | -5 | [5] |
| 4 | 13 | + + + | + + + | 13 | [13] |
| 5 | 17 | + - 0 - | - 0 - + | -29 | [29] |
| 6 | 29 | + 0 + - | - + 0 + | -17 | [17] |
| 7 | 31 | + 0 + + | + + 0 + | 37 | [37] |
| 8 | 37 | + + 0 + | + 0 + + | 31 | [31] |
| 9 | 43 | + - - - + | + - - - + | 43 | [43] |
| 10 | 53 | + - 0 0 - | - 0 0 - + | -83 | [83] |
| 11 | 59 | + - + - - | - - + - + | -101 | [101] |
| 12 | 61 | + - + - + | + - + - + | 61 | [61] |
| 13 | 71 | + 0 - 0 - | - 0 - 0 + | -89 | [89] |
| 14 | 73 | + 0 - 0 + | + 0 - 0 + | 73 | [73] |
| 15 | 83 | + 0 0 + - | - + 0 0 + | -53 | [53] |
| 16 | 89 | + 0 + 0 - | - 0 + 0 + | -71 | [71] |
| 17 | 101 | + + - + - | - + - + + | -59 | [59] |
| 18 | 103 | + + - + + | + + - + + | 103 | [103] |
| 19 | 137 | + - - 0 + - | - + 0 - - + | -173 | [173] |
| 20 | 139 | + - - 0 + + | + + 0 - - + | 313 | [313] |
| 21 | 149 | + - 0 - - - | - - - 0 - + | -353 | [353] |
| 22 | 163 | + - 0 0 0 + | + 0 0 0 - + | 241 | [241] |
| 23 | 173 | + - 0 + + - | - + + 0 - + | -137 | [137] |
| 24 | 179 | + - + - 0 - | - 0 - + - + | -263 | [263] |
| 25 | 181 | + - + - 0 + | + 0 - + - + | 223 | [223] |
| 26 | 193 | + - + 0 + + | + + 0 + - + | 331 | [331] |
| 27 | 199 | + - + + 0 + | + 0 + + - + | 277 | [277] |
| 28 | 223 | + 0 - + - + | + - + - 0 + | 181 | [181] |
| 29 | 233 | + 0 0 - 0 - | - 0 - 0 0 + | -269 | [269] |
| 30 | 241 | + 0 0 0 - + | + - 0 0 0 + | 163 | [163] |
| 31 | 263 | + 0 + - + - | - + - + 0 + | -179 | [179] |
| 32 | 269 | + 0 + 0 0 - | - 0 0 + 0 + | -233 | [233] |
| 33 | 277 | + 0 + + - + | + - + + 0 + | 199 | [199] |
| 34 | 311 | + + 0 - - - | - - - 0 + + | -347 | [347] |
| 35 | 313 | + + 0 - - + | + - - 0 + + | 139 | [139] |
| 36 | 331 | + + 0 + - + | + - + 0 + + | 193 | [193] |
| 37 | 347 | + + + 0 - - | - - 0 + + + | -311 | [311] |
| 38 | 353 | + + + 0 + - | - + 0 + + + | -149 | [149] |
| 39 | 367 | + - - - - - + | + - - - - - + | 367 | [367] |
| 40 | 373 | + - - - - + + | + + - - - - + | 853 | [853] |
| 41 | 379 | + - - - 0 0 + | + 0 0 - - - + | 691 | [691] |
| 42 | 383 | + - - - + - - | - - + - - - + | -929 | [929] |
| 43 | 389 | + - - - + + - | - + + - - - + | -443 | [443] |
| 44 | 401 | + - - 0 0 - - | - - 0 0 - - + | -983 | [983] |
| 45 | 421 | + - - + - - + | + - - + - - + | 421 | [421] |
| 46 | 443 | + - - + + + - | - + + + - - + | -389 | [389] |
| 47 | 449 | + - 0 - - 0 - | - 0 - - 0 - + | -839 | [839] |
| 48 | 457 | + - 0 - 0 - + | + - 0 - 0 - + | 457 | [457] |
| 49 | 467 | + - 0 - + 0 - | - 0 + - 0 - + | -677 | [677] |
| 50 | 479 | + - 0 0 - + - | - + - 0 0 - + | -569 | [569] |
| 51 | 487 | + - 0 0 0 0 + | + 0 0 0 0 - + | 727 | [727] |
| 52 | 499 | + - 0 0 + + + | + + + 0 0 - + | 1051 | [1051] |

## A323784: Orphan warp primes (primes that don't warp to primes)

### A323784 Sequence

3,19,23,41,47,67,79,97,107,109,113,127,131,151,157,167,191,197,211,227,229,239,251,257,271,281,283,293,307,317,337,349,359,397,409,419,431,433,439,461,463,491,503,521,523,557,563,571,577,587,593,617,619,631,641,647,653,659,661,673,683,701,733,743,769,787,797,821,829,881,907,911,937,941,953,967,971,991,997

### A323784 Stats

Stats for A323784 are 100% - stats(A323782) since A323784 is the complement of A323782.

### A323784 Table for primes < 500

|index|prime|BT representation|reversed BT|warped prime|prime factors|
| --- | --- | --- | --- | --- | --- |
| 0 | 3 | + 0 | 0 + | 1 | [] |
| 1 | 19 | + - 0 + | + 0 - + | 25 | [5] |
| 2 | 23 | + 0 - - | - - 0 + | -35 | [5, 7] |
| 3 | 41 | + - - - - | - - - - + | -119 | [7, 17] |
| 4 | 47 | + - - + - | - + - - + | -65 | [5, 13] |
| 5 | 67 | + - + + + | + + + - + | 115 | [5, 23] |
| 6 | 79 | + 0 0 - + | + - 0 0 + | 55 | [5, 11] |
| 7 | 97 | + + - - + | + - - + + | 49 | [7] |
| 8 | 107 | + + 0 0 - | - 0 0 + + | -77 | [7, 11] |
| 9 | 109 | + + 0 0 + | + 0 0 + + | 85 | [5, 17] |
| 10 | 113 | + + + - - | - - + + + | -95 | [5, 19] |
| 11 | 127 | + - - - 0 + | + 0 - - - + | 205 | [5, 41] |
| 12 | 131 | + - - 0 - - | - - 0 - - + | -335 | [5, 67] |
| 13 | 151 | + - 0 - - + | + - - 0 - + | 133 | [7, 19] |
| 14 | 157 | + - 0 - + + | + + - 0 - + | 295 | [5, 59] |
| 15 | 167 | + - 0 + - - | - - + 0 - + | -299 | [13, 23] |
| 16 | 191 | + - + 0 + - | - + 0 + - + | -155 | [5, 31] |
| 17 | 197 | + - + + 0 - | - 0 + + - + | -209 | [11, 19] |
| 18 | 211 | + 0 - - + + | + + - - 0 + | 289 | [17] |
| 19 | 227 | + 0 - + + - | - + + - 0 + | -143 | [11, 13] |
| 20 | 229 | + 0 - + + + | + + + - 0 + | 343 | [7] |
| 21 | 239 | + 0 0 0 - - | - - 0 0 0 + | -323 | [17, 19] |
| 22 | 251 | + 0 0 + 0 - | - 0 + 0 0 + | -215 | [5, 43] |
| 23 | 257 | + 0 + - - - | - - - + 0 + | -341 | [11, 31] |
| 24 | 271 | + 0 + 0 0 + | + 0 0 + 0 + | 253 | [11, 23] |
| 25 | 281 | + 0 + + + - | - + + + 0 + | -125 | [5] |
| 26 | 283 | + 0 + + + + | + + + + 0 + | 361 | [19] |
| 27 | 293 | + + - 0 - - | - - 0 - + + | -329 | [7, 47] |
| 28 | 307 | + + - + 0 + | + 0 + - + + | 265 | [5, 53] |
| 29 | 317 | + + 0 - + - | - + - 0 + + | -185 | [5, 37] |
| 30 | 337 | + + 0 + + + | + + + 0 + + | 355 | [5, 71] |
| 31 | 349 | + + + 0 - + | + - 0 + + + | 175 | [5, 7] |
| 32 | 359 | + + + + 0 - | - 0 + + + + | -203 | [7, 29] |
| 33 | 397 | + - - 0 - 0 + | + 0 - 0 - - + | 637 | [7, 13] |
| 34 | 409 | + - - 0 0 + + | + + 0 0 - - + | 961 | [31] |
| 35 | 419 | + - - + - - - | - - - + - - + | -1037 | [17, 61] |
| 36 | 431 | + - - + 0 0 - | - 0 0 + - - + | -713 | [23, 31] |
| 37 | 433 | + - - + 0 0 + | + 0 0 + - - + | 745 | [5, 149] |
| 38 | 439 | + - - + + - + | + - + + - - + | 583 | [11, 53] |
| 39 | 461 | + - 0 - 0 + - | - + 0 - 0 - + | -515 | [5, 103] |
| 40 | 463 | + - 0 - 0 + + | + + 0 - 0 - + | 943 | [23, 41] |
| 41 | 491 | + - 0 0 + - - | - - + 0 0 - + | -893 | [19, 47] |
| 42 | 503 | + - 0 + - 0 - | - 0 - + 0 - + | -785 | [5, 157] |
| 43 | 521 | + - 0 + + 0 - | - 0 + + 0 - + | -623 | [7, 89] |
| 44 | 523 | + - 0 + + 0 + | + 0 + + 0 - + | 835 | [5, 167] |
| 45 | 557 | + - + 0 - 0 - | - 0 - 0 + - + | -803 | [11, 73] |
| 46 | 563 | + - + 0 0 - - | - - 0 0 + - + | -965 | [5, 193] |
| 47 | 571 | + - + 0 0 + + | + + 0 0 + - + | 979 | [11, 89] |
| 48 | 577 | + - + 0 + 0 + | + 0 + 0 + - + | 817 | [19, 43] |
| 49 | 587 | + - + + - + - | - + - + + - + | -533 | [13, 41] |
| 50 | 593 | + - + + 0 0 - | - 0 0 + + - + | -695 | [5, 139] |
| 51 | 617 | + 0 - - 0 - - | - - 0 - - 0 + | -1007 | [19, 53] |
| 52 | 619 | + 0 - - 0 - + | + - 0 - - 0 + | 451 | [11, 41] |
| 53 | 631 | + 0 - - + 0 + | + 0 + - - 0 + | 775 | [5, 31] |
| 54 | 641 | + 0 - 0 - + - | - + - 0 - 0 + | -575 | [5, 23] |
| 55 | 647 | + 0 - 0 0 0 - | - 0 0 0 - 0 + | -737 | [11, 67] |
| 56 | 653 | + 0 - 0 + - - | - - + 0 - 0 + | -899 | [29, 31] |
| 57 | 659 | + 0 - 0 + + - | - + + 0 - 0 + | -413 | [7, 59] |
| 58 | 661 | + 0 - 0 + + + | + + + 0 - 0 + | 1045 | [5, 11, 19] |
| 59 | 673 | + 0 - + 0 - + | + - 0 + - 0 + | 505 | [5, 101] |
| 60 | 683 | + 0 - + + 0 - | - 0 + + - 0 + | -629 | [17, 37] |
| 61 | 701 | + 0 0 - 0 0 - | - 0 0 - 0 0 + | -755 | [5, 151] |
| 62 | 733 | + 0 0 0 0 + + | + + 0 0 0 0 + | 973 | [7, 139] |
| 63 | 743 | + 0 0 + - - - | - - - + 0 0 + | -1025 | [5, 41] |
| 64 | 769 | + 0 0 + + + + | + + + + 0 0 + | 1081 | [23, 47] |
| 65 | 787 | + 0 + - 0 + + | + + 0 - + 0 + | 955 | [5, 191] |
| 66 | 797 | + 0 + 0 - - - | - - - 0 + 0 + | -1043 | [7, 149] |
| 67 | 821 | + 0 + 0 + + - | - + + 0 + 0 + | -395 | [5, 79] |
| 68 | 829 | + 0 + + - 0 + | + 0 - + + 0 + | 685 | [5, 137] |
| 69 | 881 | + + - 0 - 0 - | - 0 - 0 - + + | -815 | [5, 163] |
| 70 | 907 | + + - + - - + | + - - + - + + | 427 | [7, 61] |
| 71 | 911 | + + - + - + - | - + - + - + + | -545 | [5, 109] |
| 72 | 937 | + + 0 - - 0 + | + 0 - - 0 + + | 625 | [5] |
| 73 | 941 | + + 0 - 0 - - | - - 0 - 0 + + | -995 | [5, 199] |
| 74 | 953 | + + 0 - + 0 - | - 0 + - 0 + + | -671 | [11, 61] |
| 75 | 967 | + + 0 0 - + + | + + - 0 0 + + | 895 | [5, 179] |
| 76 | 971 | + + 0 0 0 0 - | - 0 0 0 0 + + | -725 | [5, 29] |
| 77 | 991 | + + 0 + - 0 + | + 0 - + 0 + + | 679 | [7, 97] |
| 78 | 997 | + + 0 + 0 - + | + - 0 + 0 + + | 517 | [11, 47] |

## Table for primes < 500

|index|prime|BT representation|reversed BT|warped prime|prime factors|
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | + - | - + | -2 | [2] |
| 2 | 3 | + 0 | 0 + | 1 | [] |
| 3 | 5 | + - - | - - + | -11 | [11] |
| 4 | 7 | + - + | + - + | 7 | [7] |
| 5 | 11 | + + - | - + + | -5 | [5] |
| 6 | 13 | + + + | + + + | 13 | [13] |
| 7 | 17 | + - 0 - | - 0 - + | -29 | [29] |
| 8 | 19 | + - 0 + | + 0 - + | 25 | [5] |
| 9 | 23 | + 0 - - | - - 0 + | -35 | [5, 7] |
| 10 | 29 | + 0 + - | - + 0 + | -17 | [17] |
| 11 | 31 | + 0 + + | + + 0 + | 37 | [37] |
| 12 | 37 | + + 0 + | + 0 + + | 31 | [31] |
| 13 | 41 | + - - - - | - - - - + | -119 | [7, 17] |
| 14 | 43 | + - - - + | + - - - + | 43 | [43] |
| 15 | 47 | + - - + - | - + - - + | -65 | [5, 13] |
| 16 | 53 | + - 0 0 - | - 0 0 - + | -83 | [83] |
| 17 | 59 | + - + - - | - - + - + | -101 | [101] |
| 18 | 61 | + - + - + | + - + - + | 61 | [61] |
| 19 | 67 | + - + + + | + + + - + | 115 | [5, 23] |
| 20 | 71 | + 0 - 0 - | - 0 - 0 + | -89 | [89] |
| 21 | 73 | + 0 - 0 + | + 0 - 0 + | 73 | [73] |
| 22 | 79 | + 0 0 - + | + - 0 0 + | 55 | [5, 11] |
| 23 | 83 | + 0 0 + - | - + 0 0 + | -53 | [53] |
| 24 | 89 | + 0 + 0 - | - 0 + 0 + | -71 | [71] |
| 25 | 97 | + + - - + | + - - + + | 49 | [7] |
| 26 | 101 | + + - + - | - + - + + | -59 | [59] |
| 27 | 103 | + + - + + | + + - + + | 103 | [103] |
| 28 | 107 | + + 0 0 - | - 0 0 + + | -77 | [7, 11] |
| 29 | 109 | + + 0 0 + | + 0 0 + + | 85 | [5, 17] |
| 30 | 113 | + + + - - | - - + + + | -95 | [5, 19] |
| 31 | 127 | + - - - 0 + | + 0 - - - + | 205 | [5, 41] |
| 32 | 131 | + - - 0 - - | - - 0 - - + | -335 | [5, 67] |
| 33 | 137 | + - - 0 + - | - + 0 - - + | -173 | [173] |
| 34 | 139 | + - - 0 + + | + + 0 - - + | 313 | [313] |
| 35 | 149 | + - 0 - - - | - - - 0 - + | -353 | [353] |
| 36 | 151 | + - 0 - - + | + - - 0 - + | 133 | [7, 19] |
| 37 | 157 | + - 0 - + + | + + - 0 - + | 295 | [5, 59] |
| 38 | 163 | + - 0 0 0 + | + 0 0 0 - + | 241 | [241] |
| 39 | 167 | + - 0 + - - | - - + 0 - + | -299 | [13, 23] |
| 40 | 173 | + - 0 + + - | - + + 0 - + | -137 | [137] |
| 41 | 179 | + - + - 0 - | - 0 - + - + | -263 | [263] |
| 42 | 181 | + - + - 0 + | + 0 - + - + | 223 | [223] |
| 43 | 191 | + - + 0 + - | - + 0 + - + | -155 | [5, 31] |
| 44 | 193 | + - + 0 + + | + + 0 + - + | 331 | [331] |
| 45 | 197 | + - + + 0 - | - 0 + + - + | -209 | [11, 19] |
| 46 | 199 | + - + + 0 + | + 0 + + - + | 277 | [277] |
| 47 | 211 | + 0 - - + + | + + - - 0 + | 289 | [17] |
| 48 | 223 | + 0 - + - + | + - + - 0 + | 181 | [181] |
| 49 | 227 | + 0 - + + - | - + + - 0 + | -143 | [11, 13] |
| 50 | 229 | + 0 - + + + | + + + - 0 + | 343 | [7] |
| 51 | 233 | + 0 0 - 0 - | - 0 - 0 0 + | -269 | [269] |
| 52 | 239 | + 0 0 0 - - | - - 0 0 0 + | -323 | [17, 19] |
| 53 | 241 | + 0 0 0 - + | + - 0 0 0 + | 163 | [163] |
| 54 | 251 | + 0 0 + 0 - | - 0 + 0 0 + | -215 | [5, 43] |
| 55 | 257 | + 0 + - - - | - - - + 0 + | -341 | [11, 31] |
| 56 | 263 | + 0 + - + - | - + - + 0 + | -179 | [179] |
| 57 | 269 | + 0 + 0 0 - | - 0 0 + 0 + | -233 | [233] |
| 58 | 271 | + 0 + 0 0 + | + 0 0 + 0 + | 253 | [11, 23] |
| 59 | 277 | + 0 + + - + | + - + + 0 + | 199 | [199] |
| 60 | 281 | + 0 + + + - | - + + + 0 + | -125 | [5] |
| 61 | 283 | + 0 + + + + | + + + + 0 + | 361 | [19] |
| 62 | 293 | + + - 0 - - | - - 0 - + + | -329 | [7, 47] |
| 63 | 307 | + + - + 0 + | + 0 + - + + | 265 | [5, 53] |
| 64 | 311 | + + 0 - - - | - - - 0 + + | -347 | [347] |
| 65 | 313 | + + 0 - - + | + - - 0 + + | 139 | [139] |
| 66 | 317 | + + 0 - + - | - + - 0 + + | -185 | [5, 37] |
| 67 | 331 | + + 0 + - + | + - + 0 + + | 193 | [193] |
| 68 | 337 | + + 0 + + + | + + + 0 + + | 355 | [5, 71] |
| 69 | 347 | + + + 0 - - | - - 0 + + + | -311 | [311] |
| 70 | 349 | + + + 0 - + | + - 0 + + + | 175 | [5, 7] |
| 71 | 353 | + + + 0 + - | - + 0 + + + | -149 | [149] |
| 72 | 359 | + + + + 0 - | - 0 + + + + | -203 | [7, 29] |
| 73 | 367 | + - - - - - + | + - - - - - + | 367 | [367] |
| 74 | 373 | + - - - - + + | + + - - - - + | 853 | [853] |
| 75 | 379 | + - - - 0 0 + | + 0 0 - - - + | 691 | [691] |
| 76 | 383 | + - - - + - - | - - + - - - + | -929 | [929] |
| 77 | 389 | + - - - + + - | - + + - - - + | -443 | [443] |
| 78 | 397 | + - - 0 - 0 + | + 0 - 0 - - + | 637 | [7, 13] |
| 79 | 401 | + - - 0 0 - - | - - 0 0 - - + | -983 | [983] |
| 80 | 409 | + - - 0 0 + + | + + 0 0 - - + | 961 | [31] |
| 81 | 419 | + - - + - - - | - - - + - - + | -1037 | [17, 61] |
| 82 | 421 | + - - + - - + | + - - + - - + | 421 | [421] |
| 83 | 431 | + - - + 0 0 - | - 0 0 + - - + | -713 | [23, 31] |
| 84 | 433 | + - - + 0 0 + | + 0 0 + - - + | 745 | [5, 149] |
| 85 | 439 | + - - + + - + | + - + + - - + | 583 | [11, 53] |
| 86 | 443 | + - - + + + - | - + + + - - + | -389 | [389] |
| 87 | 449 | + - 0 - - 0 - | - 0 - - 0 - + | -839 | [839] |
| 88 | 457 | + - 0 - 0 - + | + - 0 - 0 - + | 457 | [457] |
| 89 | 461 | + - 0 - 0 + - | - + 0 - 0 - + | -515 | [5, 103] |
| 90 | 463 | + - 0 - 0 + + | + + 0 - 0 - + | 943 | [23, 41] |
| 91 | 467 | + - 0 - + 0 - | - 0 + - 0 - + | -677 | [677] |
| 92 | 479 | + - 0 0 - + - | - + - 0 0 - + | -569 | [569] |
| 93 | 487 | + - 0 0 0 0 + | + 0 0 0 0 - + | 727 | [727] |
| 94 | 491 | + - 0 0 + - - | - - + 0 0 - + | -893 | [19, 47] |
| 95 | 499 | + - 0 0 + + + | + + + 0 0 - + | 1051 | [1051] |

## Relation between balanced ternary operation of A117966 and warp operator A323782 on integers

### Python Code from A117966: Balanced ternary enumeration (or balanced ternary representation) of integers; write n in ternary and then replace 2's with (-1)'s

```python
def a(n):
    if n==0: return 0
    if n%3==0: return 3*a(n/3)
    elif n%3==1: return 3*a((n - 1)/3) + 1
    else: return 3*a((n - 2)/3) - 1`
```

### Python Code from A134028: Reversal of n in balanced ternary representation

```python
def a(n):
    if n==0: return 0
    s=[]
    x=0
    while n>0:
        x=n%3
        n=n/3
        if x==2:
            x=-1
            n+=1
        s+=[x, ]
    l=s[::-1]
    t=0
    for i in xrange(len(l)): t+=l[i]*3**i
    return t
```

### Comparative table between A117966 & A134028

|index|A117966 operator|A323782 & A134028 warp operator|
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | -1 | -2 |
| 3 | 3 | 1 |
| 4 | 4 | 4 |
| 5 | 2 | -11 |
| 6 | -3 | -2 |
| 7 | -2 | 7 |
| 8 | -4 | -8 |
| 9 | 9 | 1 |
| 10 | 10 | 10 |
| 11 | 8 | -5 |
| 12 | 12 | 4 |
| 13 | 13 | 13 |
| 14 | 11 | -38 |
| 15 | 6 | -11 |
| 16 | 7 | 16 |
| 17 | 5 | -29 |
| 18 | -9 | -2 |
| 19 | -8 | 25 |
| 20 | -10 | -20 |
| 21 | -6 | 7 |
| 22 | -5 | 34 |
| 23 | -7 | -35 |
| 24 | -12 | -8 |
| 25 | -11 | 19 |
| 26 | -13 | -26 |
| 27 | 27 | 1 |
| 28 | 28 | 28 |
| 29 | 26 | -17 |
| 30 | 30 | 10 |
| 31 | 31 | 37 |
| 32 | 29 | -32 |
| 33 | 24 | -5 |
| 34 | 25 | 22 |
| 35 | 23 | -23 |
| 36 | 36 | 4 |
| 37 | 37 | 31 |
| 38 | 35 | -14 |
| 39 | 39 | 13 |
| 40 | 40 | 40 |
| 41 | 38 | -119 |
| 42 | 33 | -38 |
| 43 | 34 | 43 |
| 44 | 32 | -92 |
| 45 | 18 | -11 |
| 46 | 19 | 70 |
| 47 | 17 | -65 |
| 48 | 21 | 16 |
| 49 | 22 | 97 |
| 50 | 20 | -110 |
| 51 | 15 | -29 |
| 52 | 16 | 52 |
| 53 | 14 | -83 |
| 54 | -27 | -2 |
| 55 | -26 | 79 |
| 56 | -28 | -56 |
| 57 | -24 | 25 |
| 58 | -23 | 106 |
| 59 | -25 | -101 |
| 60 | -30 | -20 |
| 61 | -29 | 61 |
| 62 | -31 | -74 |
| 63 | -18 | 7 |
| 64 | -17 | 88 |
| 65 | -19 | -47 |
| 66 | -15 | 34 |
| 67 | -14 | 115 |
| 68 | -16 | -116 |
| 69 | -21 | -35 |
| 70 | -20 | 46 |
| 71 | -22 | -89 |
| 72 | -36 | -8 |
| 73 | -35 | 73 |
| 74 | -37 | -62 |
| 75 | -33 | 19 |
| 76 | -32 | 100 |
| 77 | -34 | -107 |
| 78 | -39 | -26 |
| 79 | -38 | 55 |
| 80 | -40 | -80 |
| 81 | 81 | 1 |
| 82 | 82 | 82 |
| 83 | 80 | -53 |
| 84 | 84 | 28 |
| 85 | 85 | 109 |
| 86 | 83 | -98 |
| 87 | 78 | -17 |
| 88 | 79 | 64 |
| 89 | 77 | -71 |
| 90 | 90 | 10 |
| 91 | 91 | 91 |
| 92 | 89 | -44 |
| 93 | 93 | 37 |
| 94 | 94 | 118 |
| 95 | 92 | -113 |
| 96 | 87 | -32 |
| 97 | 88 | 49 |
| 98 | 86 | -86 |
| 99 | 72 | -5 |
| 100 | 73 | 76 |