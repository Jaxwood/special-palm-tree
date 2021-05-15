import hashlib


def hash_of(s: str, pattern: str) -> str:
    i = 0
    while True:
        x = s + str(i)
        hash = hashlib.md5(x.encode()).hexdigest()
        if hash[:(len(pattern))] == pattern:
            return i
        else:
            i += 1
