#!/usr/bin/env python3
"""
Author: Sajjad
GitHub: https://github.com/Cyber-Anonymous
"""

import itertools
import string
import argparse
import sys
import time
import os
import math

Tool_Name = "BruteForge"
Version = "1.0.0"

charsets = {
    "digits": string.digits,
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "special": string.punctuation,
    "all": string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
}
#charset = string.printable


parser = argparse.ArgumentParser(description="Generate a brute-force wordlist.")

parser.add_argument("-l", "--length", type=int, help="Length of each combination.")
parser.add_argument("-c", "--charset", choices=["digits", "lowercase", "uppercase", "special", "all"], help="Character set to use: digits, lowercase, uppercase, special, all")
parser.add_argument("-s", "--custom_charset", type=str, help="Custom character set to use.")
parser.add_argument("-o", "--output", type=str, help="Output file name.")
parser.add_argument("-v", "--verbose", action="store_true", help="Print progress information.")
parser.add_argument("--version", action="version", version="{} {}".format(Tool_Name, Version))

args = parser.parse_args()

charset = charsets["all"]


def banner():
    print("\033[0;94m")
    print("""
    ____             __       ______                    
   / __ )_______  __/ /____  / ____/___  _________ ____ 
  / __  / ___/ / / / __/ _ \/ /_  / __ \/ ___/ __ `/ _ \\
 / /_/ / /  / /_/ / /_/  __/ __/ / /_/ / /  / /_/ /  __/ 
/_____/ /   \__,_/\__/\___/_/    \____/_/   \__, /\\___/ 
                                           /____/        
                                        Coded by Sajjad
          """)
    print("\033[0;0m")


if(bool(args.length) == True):
    length = args.length

elif(bool(args.length) == False):
    banner()
    while(True):
        length = input("Length of each combination > ")
        try:
            length = int(length)
            break
        except:
            print("\033[0;91mInvalid length.\033[0;00m\n")

else:
    pass

try:
    if bool(args.charset) == True and bool(args.custom_charset) == False:
        charset = charsets[args.charset]
        if args.verbose:
            print("\nCharacter Set Used: {}".format(charset))
        else:
            pass
    else:
        pass
        
    if bool(args.custom_charset) == True and bool(args.charset) == False:
        charset = args.custom_charset
        if args.verbose:
            print("Custom Character Set: {}".format(charset))
        else:
            pass
    else:
        pass

    if args.charset and args.custom_charset:
        charset = charsets[args.charset] + args.custom_charset
        if args.verbose:
            print("")
            print("Selected Character Set: {}".format(charsets[args.charset]))
            print("Custom Character Set: {}".format(args.custom_charset))
        else:
            pass
    else:
        pass

except Exception as error:
    print("\033[0;91m[ERROR] {}\033[0m".format(error)) 
    sys.exit()





if(bool(args.output) == True):
    filename = args.output
    file = open(filename, "w")


elif(bool(args.output) == False):
    while(True):
        try:
            filename = input("File name > ")
            file = open(filename, "w")
            break
        except Exception as error:
            print("\033[0;91m[ERROR] {}\033[0m]".format(error))

else:
    pass

print("")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return "{} {}".format(s, size_name[i])


try:
    start_time = time.time()
    total_combination = len(charset) ** length
    count = 0
    for combination in itertools.product(charset, repeat=length):
        password = "".join(combination)
        file.write(password + "\n")
        count += 1
        if args.verbose and count % 1 == 0:
            elapsed_time = int(time.time() - start_time)
            progress = (count / total_combination) * 100
            sys.stdout.write("\r[INFO] Progress: {:.2f}%".format(progress))
            sys.stdout.write(" | Password: {}".format(password))
            sys.stdout.write(" | Elapsed Time: {}s".format(elapsed_time))
            sys.stdout.flush()
        else:
            pass
    file.flush()
    os.fsync(file.fileno())
    file.close()

    if args.verbose:
        print("")
    file_size = os.path.getsize(filename)
    print("\nGenerated {} combinations.".format(count))
    print("Total data generated: {} bytes ({})".format(file_size, convert_size(file_size)))

    print("\nBrute-force list generated and saved to {}\n".format(args.output))

except Exception as error:
    print("\033[0;91m[ERROR] {}\033[0m]".format(error))
    sys.exit()









