import itertools
import string
import time

from bocpy import Cown, when, wait

ALPHABET = string.ascii_lowercase  # a-z


def weak_hash(plaintext: str) -> str:
    """Simple non-cryptographic 32-bit hash implemented in pure Python."""
    h = 2166136261
    for char in plaintext:
        h ^= ord(char)
        h = (h * 16777619) & 0xFFFFFFFFFFFFFFFF
    return f"{h:016x}"


def generate_candidates(length: int):
    """Yields every string of exactly `length` chars from the ALPHABET."""
    for combo in itertools.product(ALPHABET, repeat=length):
        yield "".join(combo)


def crack_prefix_segment(
    target_hash: str, prefix: str, suffix_length: int
) -> str | None:
    """
    Brute-force one prefix segment of the search space.
    Tries every suffix of length `suffix_length`, prepending `prefix` to each candidate.
    Returns the full matching plaintext, or None if no match exists in this segment.
    """
    for candidate in generate_candidates(suffix_length):
        full_candidate = prefix + candidate
        if weak_hash(full_candidate) == target_hash:
            print(f"Found solution: {full_candidate}")
            return full_candidate
    return None


def crack(target_hash: str, password_length: int) -> str | None:
    """
    Brute-force a hash by splitting work on the first character.
    For each possible first character in `ALPHABET`, searches the remaining
    `password_length - 1` characters.
    Returns the full matching plaintext, or None if not found.
    """

    # TODO: Try parallelizing this using BocPy
    for prefix in ALPHABET:
        crack_prefix_segment(target_hash, prefix, password_length-1)


SECRETS = [
    {"hash": "6cc5339b87c6a267", "input_length": 3},
    {"hash": "1f55559ccec577d1", "input_length": 4},
    {"hash": "1c67d81b5d9dd07e", "input_length": 5},
    {"hash": "c4401a130fceff97", "input_length": 6},
    {"hash": "cf61593182bb9434", "input_length": 7},
]

if __name__ == "__main__":

    for secret in SECRETS:
        print(f"Cracking hash: {secret["hash"]}  (length={secret["input_length"]})")

        start = time.perf_counter()
        crack(secret["hash"], secret["input_length"])
        elapsed = time.perf_counter() - start

        print(f"Time {elapsed:.3f}s")
        print()
