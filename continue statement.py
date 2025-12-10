def skip_5():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

def main():
    print("Numbers 1 to 10 skipping 5:")
    skip_5()
