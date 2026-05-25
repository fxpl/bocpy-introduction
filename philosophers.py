from bocpy import Cown, when, wait
from time import sleep

def eat(name, left_hand, right_hand):
    l = left_hand.value
    r = right_hand.value
    print(f"Philosopher {name} started eating with fork {l} and {r}")
    sleep(1)
    print(f"Philosopher {name} stopped eating")

fork1 = Cown(1)
fork2 = Cown(2)
fork3 = Cown(3)
fork4 = Cown(4)

@when(fork1, fork2, fork3, fork4)
def all_in_order(fork1, fork2, fork3, fork4):
    while True:
        eat("1", fork1, fork2)
        eat("2", fork2, fork3)
        eat("3", fork3, fork4)
        eat("4", fork4, fork1)

# TODO: This works, but all philosophers can't dine concurrently
# Try using boc to allow concurrent eating.

wait()