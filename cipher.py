# ight this is whats gonna happen in the file
# take in a string input
# 1. reverse characters
# 2. shift 5-9 from starting to ending letter // spaces dont count or numbers
# 3. repeat every 4 times (goes back to 5)
# 4. then reverse again to have complete

import string
alphabet = list(string.ascii_lowercase)

def cipher(original, choice):
    # reverse it and make list for shift
    r_list = (list(original[::-1]))
    # now shift character 1, t places in the alphabet
    if r_list[::] == ' ' or r_list[::] == string.digits or r_list[::] == string.puncuation:
        None

    else:
