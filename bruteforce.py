import itertools
import hashlib

def brute_force_password_cracker(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            if hashlib.md5(guess_str.encode()).hexdigest() == target_hash:
                return f"Password found: {guess_str}"
    return "Password not found"

# Example usage
target_hash = "1da76f1041430a970fd6cc39fb20a797"  # Hash for the password
charset = "abcdefghijklmnopqrstuvwxyz"
max_length = 5

print(brute_force_password_cracker(target_hash, charset, max_length))