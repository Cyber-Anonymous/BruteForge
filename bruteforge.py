#!/usr/bin/env python3

Tool_Name = "BruteForge"
Version = "1.2.0"
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


charsets = {
    "digits": string.digits,
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "special": string.punctuation,
    "all": string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
}
#charset = string.printable


parser = argparse.ArgumentParser(description="Generate a brute-force wordlist.")

parser.add_argument("-m", "--min_length", type=int, help="Minimum combination length.")
parser.add_argument("-M", "--max_length", type=int, help="Maximum combination length.")
parser.add_argument("-c", "--charset", choices=["digits", "lowercase", "uppercase", "special", "all"], help="Character set to use.")
parser.add_argument("-s", "--custom_charset", type=str, help="Custom character set.")
parser.add_argument("-o", "--output", type=str, help="Output file name.")
parser.add_argument("-v", "--verbose", action="store_true", help="Display progress information.")
parser.add_argument("--version", action="version", version="{} {}".format(Tool_Name, Version))

args = parser.parse_args()

charset = charsets["all"]

start_time = time.time()

def banner():
    print("\033[1;94m")
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


if(bool(args.min_length) == True):
    min_length = args.min_length

elif(bool(args.min_length) == False):
    banner()
    while(True):
        min_length = input("Minimum length > ")
        try:
            min_length = int(min_length)
            break
        except:
            print("\033[0;91mInvalid minimum length.\033[0;00m\n")
else:
    pass


if(bool(args.max_length) == True):
    max_length = args.max_length

elif(bool(args.max_length) == False):
    while(True):
        max_length = input("Maximum length > ")
        try:
            max_length = int(max_length)
            break
        except:
            print("\033[0;91mInvalid maximum length.\033[0;00m\n")

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

def print_progress_bar(count, total):
    bar_length = 40
    progress = count / total
    percent = progress * 100
    arrow = "#" * int(round(progress * bar_length))
    spaces = " " * (bar_length - len(arrow))
    sys.stdout.write("\r[{}{}] {}/{} ({:.2f}%)".format(arrow, spaces, count, total, percent))
    sys.stdout.flush()

try:
    if args.verbose:
        print("Process started at {}\n".format(time.ctime(start_time)))
    total_combination = 0
    count = 0

    for length in range(min_length, max_length +1):
        comb_per_length = len(charset) ** length
        total_combination += comb_per_length

    for length in range(min_length, max_length +1):
        for combination in itertools.product(charset, repeat=length):
            password = "".join(combination)
            file.write(password + "\n")
            count += 1
            if bool(args.verbose) == False:
                print_progress_bar(count, total_combination)
            if args.verbose:
                progress = (count / total_combination) * 100
                sys.stdout.write("\r[INFO] Progress: {:.2f}%".format(progress))
                sys.stdout.write(" | Password: {}".format(password))
                sys.stdout.flush()
            else:
                pass
    file.flush()
    os.fsync(file.fileno())
    file.close()

    print("")
    file_size = os.path.getsize(filename)
    print("\nGenerated {} combinations.".format(count))
    end_time = time.time()
    if args.verbose:
        elapsed = end_time - start_time
        elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        print("Elapsed Time: {}".format(elapsed_time))
    print("Total data generated: {} bytes ({})".format(file_size, convert_size(file_size)))
    if args.verbose:
        print("\nProcess ended at {}".format(time.ctime(end_time)))
    print("\nBrute-force list generated and saved to {}\n".format(filename))

except Exception as error:
    print("\033[0;91m[ERROR] {}\033[0m]".format(error))
    sys.exit()
