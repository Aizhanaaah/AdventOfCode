import hashlib
secret_key = "bgvyzdsv"


def find_hash_with_prefix(secret_key, prefix, start=0):
    i = start
    while True:
        input_data = f"{secret_key}{i}".encode()
        hash_result = hashlib.md5(input_data).hexdigest()
        if hash_result.startswith(prefix):
            return i
        i += 1


# Part 1

prefix = "00000"
result = find_hash_with_prefix(secret_key, prefix)
print(f"Part 1: {result}")


# Part 2
prefix = "000000"
result = find_hash_with_prefix(secret_key, prefix, start=result)
print(f"Part 2: {result}")
