
def triple(x:int):
    return 3*x

def square(x:int):
    return x*x


def main():
    for i in range(1,11):
        x=square(i)
        y=triple(i)
        if x>y:
            break
        print(f"triple({i})=={y} square({i})=={x}")
    pass

if __name__ == "__main__":
    main()
