from bocpy import Cown, when, wait

receiver = Cown("World")

@when(receiver)
def who(receiver):
    receiver.value = input("What's your name? \n")

@when(receiver)
def print(b):
    print(f"Hello {b.value}")

wait()
