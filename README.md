# Warp Primes by sneakyweasel

- Prime numbers whose reverse of the balanced ternary representation is also prime.
- Balanced ternary notation might allow insight into relations hidden by classical notation. [Balanced Ternary]( https://en.wikipedia.org/wiki/Balanced_ternary)

Python code used to generate Warp Primes:

- Warp Entry: [OEIS A323782](https://oeis.org/A323782)
- Warp Exit : [OEIS A323783](https://oeis.org/A323783)

## How-to

$ pip install sympy

$ py -3 warp.py

## Table

|index|prime|BT representation|reversed BT representation|warped prime|prime factors|
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
| 96 | 503 | + - 0 + - 0 - | - 0 - + 0 - + | -785 | [5, 157] |
| 97 | 509 | + - 0 + 0 - - | - - 0 + 0 - + | -947 | [947] |
| 98 | 521 | + - 0 + + 0 - | - 0 + + 0 - + | -623 | [7, 89] |
| 99 | 523 | + - 0 + + 0 + | + 0 + + 0 - + | 835 | [5, 167] |
| 100 | 541 | + - + - 0 0 + | + 0 0 - + - + | 709 | [709] |
| 101 | 547 | + - + - + - + | + - + - + - + | 547 | [547] |
| 102 | 557 | + - + 0 - 0 - | - 0 - 0 + - + | -803 | [11, 73] |
| 103 | 563 | + - + 0 0 - - | - - 0 0 + - + | -965 | [5, 193] |
| 104 | 569 | + - + 0 0 + - | - + 0 0 + - + | -479 | [479] |
| 105 | 571 | + - + 0 0 + + | + + 0 0 + - + | 979 | [11, 89] |
| 106 | 577 | + - + 0 + 0 + | + 0 + 0 + - + | 817 | [19, 43] |
| 107 | 587 | + - + + - + - | - + - + + - + | -533 | [13, 41] |
| 108 | 593 | + - + + 0 0 - | - 0 0 + + - + | -695 | [5, 139] |
| 109 | 599 | + - + + + - - | - - + + + - + | -857 | [857] |
| 110 | 601 | + - + + + - + | + - + + + - + | 601 | [601] |
| 111 | 607 | + - + + + + + | + + + + + - + | 1087 | [1087] |
| 112 | 613 | + 0 - - - 0 + | + 0 - - - 0 + | 613 | [613] |
| 113 | 617 | + 0 - - 0 - - | - - 0 - - 0 + | -1007 | [19, 53] |
| 114 | 619 | + 0 - - 0 - + | + - 0 - - 0 + | 451 | [11, 41] |
| 115 | 631 | + 0 - - + 0 + | + 0 + - - 0 + | 775 | [5, 31] |
| 116 | 641 | + 0 - 0 - + - | - + - 0 - 0 + | -575 | [5, 23] |
| 117 | 643 | + 0 - 0 - + + | + + - 0 - 0 + | 883 | [883] |
| 118 | 647 | + 0 - 0 0 0 - | - 0 0 0 - 0 + | -737 | [11, 67] |
| 119 | 653 | + 0 - 0 + - - | - - + 0 - 0 + | -899 | [29, 31] |
| 120 | 659 | + 0 - 0 + + - | - + + 0 - 0 + | -413 | [7, 59] |
| 121 | 661 | + 0 - 0 + + + | + + + 0 - 0 + | 1045 | [5, 11, 19] |
| 122 | 673 | + 0 - + 0 - + | + - 0 + - 0 + | 505 | [5, 101] |
| 123 | 677 | + 0 - + 0 + - | - + 0 + - 0 + | -467 | [467] |
| 124 | 683 | + 0 - + + 0 - | - 0 + + - 0 + | -629 | [17, 37] |
| 125 | 691 | + 0 0 - - - + | + - - - 0 0 + | 379 | [379] |
| 126 | 701 | + 0 0 - 0 0 - | - 0 0 - 0 0 + | -755 | [5, 151] |
| 127 | 709 | + 0 0 - + - + | + - + - 0 0 + | 541 | [541] |
| 128 | 719 | + 0 0 0 - 0 - | - 0 - 0 0 0 + | -809 | [809] |
| 129 | 727 | + 0 0 0 0 - + | + - 0 0 0 0 + | 487 | [487] |
| 130 | 733 | + 0 0 0 0 + + | + + 0 0 0 0 + | 973 | [7, 139] |
| 131 | 739 | + 0 0 0 + 0 + | + 0 + 0 0 0 + | 811 | [811] |
| 132 | 743 | + 0 0 + - - - | - - - + 0 0 + | -1025 | [5, 41] |
| 133 | 751 | + 0 0 + - + + | + + - + 0 0 + | 919 | [919] |
| 134 | 757 | + 0 0 + 0 0 + | + 0 0 + 0 0 + | 757 | [757] |
| 135 | 761 | + 0 0 + + - - | - - + + 0 0 + | -863 | [863] |
| 136 | 769 | + 0 0 + + + + | + + + + 0 0 + | 1081 | [23, 47] |
| 137 | 773 | + 0 + - - 0 - | - 0 - - + 0 + | -827 | [827] |
| 138 | 787 | + 0 + - 0 + + | + + 0 - + 0 + | 955 | [5, 191] |
| 139 | 797 | + 0 + 0 - - - | - - - 0 + 0 + | -1043 | [7, 149] |
| 140 | 809 | + 0 + 0 0 0 - | - 0 0 0 + 0 + | -719 | [719] |
| 141 | 811 | + 0 + 0 0 0 + | + 0 0 0 + 0 + | 739 | [739] |
| 142 | 821 | + 0 + 0 + + - | - + + 0 + 0 + | -395 | [5, 79] |
| 143 | 823 | + 0 + 0 + + + | + + + 0 + 0 + | 1063 | [1063] |
| 144 | 827 | + 0 + + - 0 - | - 0 - + + 0 + | -773 | [773] |
| 145 | 829 | + 0 + + - 0 + | + 0 - + + 0 + | 685 | [5, 137] |
| 146 | 839 | + 0 + + 0 + - | - + 0 + + 0 + | -449 | [449] |
| 147 | 853 | + + - - - - + | + - - - - + + | 373 | [373] |
| 148 | 857 | + + - - - + - | - + - - - + + | -599 | [599] |
| 149 | 859 | + + - - - + + | + + - - - + + | 859 | [859] |
| 150 | 863 | + + - - 0 0 - | - 0 0 - - + + | -761 | [761] |
| 151 | 877 | + + - - + + + | + + + - - + + | 1021 | [1021] |
| 152 | 881 | + + - 0 - 0 - | - 0 - 0 - + + | -815 | [5, 163] |
| 153 | 883 | + + - 0 - 0 + | + 0 - 0 - + + | 643 | [643] |
| 154 | 887 | + + - 0 0 - - | - - 0 0 - + + | -977 | [977] |
| 155 | 907 | + + - + - - + | + - - + - + + | 427 | [7, 61] |
| 156 | 911 | + + - + - + - | - + - + - + + | -545 | [5, 109] |
| 157 | 919 | + + - + 0 0 + | + 0 0 + - + + | 751 | [751] |
| 158 | 929 | + + - + + + - | - + + + - + + | -383 | [383] |
| 159 | 937 | + + 0 - - 0 + | + 0 - - 0 + + | 625 | [5] |
| 160 | 941 | + + 0 - 0 - - | - - 0 - 0 + + | -995 | [5, 199] |
| 161 | 947 | + + 0 - 0 + - | - + 0 - 0 + + | -509 | [509] |
| 162 | 953 | + + 0 - + 0 - | - 0 + - 0 + + | -671 | [11, 61] |
| 163 | 967 | + + 0 0 - + + | + + - 0 0 + + | 895 | [5, 179] |
| 164 | 971 | + + 0 0 0 0 - | - 0 0 0 0 + + | -725 | [5, 29] |
| 165 | 977 | + + 0 0 + - - | - - + 0 0 + + | -887 | [887] |
| 166 | 983 | + + 0 0 + + - | - + + 0 0 + + | -401 | [401] |
| 167 | 991 | + + 0 + - 0 + | + 0 - + 0 + + | 679 | [7, 97] |
| 168 | 997 | + + 0 + 0 - + | + - 0 + 0 + + | 517 | [11, 47] |