import pickle
from random import randint
from collections import deque

N = randint(0, 100)
# Create the history entry
history = deque([], 5)


def guess_num(k):
    if k == N:
        print("Wow, Great")
        return True
    elif k > N:
        print("You are too big")
        return False
    else:
        print("You are so small")
        return False

while True:
    line = input("Please enter your guess:")
    if line.isdigit():
        k = int(line)
        history.append(line)
        if guess_num(k):
            break
    elif line == "h?":
        print(list(history))
        pickle.dump(history, open("Cache.pkl", "wb"))
        break

with open("Cache.pkl", "rb") as cache_history:
    history_cache = pickle.load(cache_history, encoding="bytes")
    print(history_cache)



