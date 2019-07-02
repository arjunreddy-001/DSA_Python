# use recursion to implement a countdown timer


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        print("foo")    # this code will execute after we reach the top of call stack


countdown(5)
