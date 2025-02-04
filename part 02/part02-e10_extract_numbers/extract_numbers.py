#!/usr/bin/env python3
def extract_numbers(s):
    x = []
    for item in s.split():
        try:
            x.append(int(item))
        except Exception:
            try:
                x.append(float(item))
            except Exception:
                continue
    return x

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()