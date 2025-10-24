import time 
import random

def waiting_game():
    target=random.randint(2,4)
    print(f"\n.....your target time to waiting is {target} seconds......")

    input("Press Enter To Begin")
    start=time.perf_counter()

    input(f"\n .....Press enter after the {target} seconds.....")
    elapsed=time.perf_counter()-start

    print(f"\n.....Your Elapsed Time is {elapsed} seconds.....\n")

    
    tolerance = 0.1  #adjust this for tolerance (±0.1 seconds)

    if abs(elapsed - target) <= tolerance:
        print(".....->(unbelivable, perfect timing )<-.....")
    elif(elapsed>target):
        print(f"(your just missed <<<- {elapsed-target:0.3f} sec to slow)")
    elif(elapsed<target):
        print(f"(your  too fast ->>> {target-elapsed:0.3f} sec to fast)")

waiting_game()

"""
🧠 Simple Explanation

target = random.randint(2, 4)
→ Chooses a random wait time between 2–4 seconds.

First input()
→ Starts the game when you press Enter.

time.perf_counter()
→ Records the most accurate current time in seconds.

Second input()
→ You press Enter again when you think the target time passed.

elapsed = time.perf_counter() - start
→ Calculates how long you actually waited.

Tolerance check (abs(elapsed - target) <= 0.1)
→ Allows for small timing differences (within ±0.1 sec).

Prints feedback:

Perfect (if within tolerance)

Too fast

Too slow
"""