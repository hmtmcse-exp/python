import time, sys

if __name__ == '__main__':
    x = 1
    while True:
        try:
            print(x)
            time.sleep(.3)
            x += 1
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()