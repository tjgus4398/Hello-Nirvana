import sys, time

def typewriter(message, *args):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")
