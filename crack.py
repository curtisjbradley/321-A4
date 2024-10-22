from bcrypt import *
from base64 import b64decode as bdecode
from nltk.corpus import words
import time

def crack(factor, salt, phash):
    for word in words.words():
        if (len(word) < 6 or len(word) > 10):
            continue
        out = hashpw(bytes(word, "UTF-8"),bytes(f"$2b${factor}$" + salt, "UTF-8"))
        out = str(out).split("$")[3][22:-1]
        if (out == phash):
            print(word)
            return








with open("pwd", "r") as file:
    for line in file: 
        factor = line.split('$')[2]
        salt = line.split("$")[3][:22]
        phash = line.split("$")[3][22:].strip()
        print(f"Searching for {line.split('$')[0][:-1]}")
        print(factor)
        print(salt)
        start = time.time()
        crack(factor, salt, phash)
        end = time.time()
        print(f"Found after {end-start} seconds")


