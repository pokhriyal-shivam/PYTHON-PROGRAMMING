def print_until_7():
    i = 1
    while i <= 10:
        if i > 7:
            break
        print(i)
        i += 1

def main():
    print("Printing numbers 1 to 7 using break:")
    print_until_7()
