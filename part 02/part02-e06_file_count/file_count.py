#!/usr/bin/env python3

import sys

def file_count(filename):
    count_lines = 0
    count_words = 0
    count_chars = 0

    with open(filename, "r") as f:
        for line in f:
            count_lines += 1
            words = line.split()
            count_words += len(words)
            count_chars += len(line) 

    return (count_lines, count_words, count_chars)

def main():
    for filename in sys.argv[1:]:
        result = file_count(filename)
        if result:
            line_count, word_count, char_count = result
            print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")

if __name__ == "__main__":
    main()
