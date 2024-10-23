from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

from datetime import datetime as time

def sha256_hash(input_string):
   data = bytearray(input_string, "ASCII") 
   h = SHA256.new()
   h.update(data)
   return h.hexdigest()

def truncate_hash(hash_string, bits):

    num = int(hash_string[:(int(bits / 4))], 16)
    
    mask = 0
    for i in range(0, bits):
        mask = mask | (1 << i)

    return num & mask

def hamming_distance(s1, s2):
    count = 0
    for (c1, c2) in zip(s1, s2):
        if c1 != c2:
            count = count + 1
    return count

def find_hamming_distance_1():
    base = get_random_bytes(10)

    for i in range(0,10):
        modified = base
        modified[i] = base[i] ^ (1 << i)
        if hamming_distance(base, modified) == 1:
            return base, modified
    return None, None

def find_collision(bits, max_attempts):
    seen = {}
    start = time.now()
    for i in range (1, max_attempts + 1):
        s = get_random_bytes(10)
        h = truncate_hash(sha256_hash(str(s)), bits)
        if h in seen:
            end = time.now()
            return seen[h], s, i, (end - start)
        else:
            seen[h] = s
    return None, None, i, (time.now() - start)

def task_1a():
    print("Task 1a: SHA256 hashes of arbitrary inputs")
    for word in ["Hello, World!", "Python", "Cryptography"]:
        h = sha256_hash(word)
        print(word, h)
def task_1b():
    print("Task 1b: Strings with Hamming distance of 1")
    for i in range(1, 3):
        s1 = "Hello World"
        s2 = s1
        s2 = s1[:i] + chr((ord(s2[i]) ^ 1)) + s1[i + 1:]
        h1 = sha256_hash(s1)
        h2 = sha256_hash(s2)
        print(s1, s2, h1, h2)

def task_1c():
    print("Task 1c: Finding collisions for truncated hashes")
    bits_list = []
    time = []
    inputs = []
    attempts = 50000
    for bits in range(8, 50, 2):
        out = find_collision(bits, attempts)
        if out[0] != None:
            bits_list.append(bits)
            inputs.append((out[0],out[1]))
            time.append(out[3])
            continue
        else:
            print("Exceeded Max Attempts")
    print(bits_list)
    print(time)
    print(inputs)
    #Print results table
   # Plot graphs:
  #      1. Digest Size vs Collision Time
 #       2. Digest Size vs Number of Inputs
#    Save graphs as 'collision_analysis.png'

task_1a()
task_1b()
task_1c()
