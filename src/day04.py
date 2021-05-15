import hashlib


def hash_of(s: str) -> str:
    i = 0
    while True:
        x = s + str(i)
        hash = hashlib.md5(x.encode()).hexdigest()
        if hash[:5] == '00000':
            return i
        else:
            i += 1
