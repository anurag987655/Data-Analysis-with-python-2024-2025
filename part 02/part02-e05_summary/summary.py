#!/usr/bin/env python3

import statistics
import sys

def summary(filename):
    with open(filename, "r") as f:
        datas = []
        for line in f:
            try:
                x = float(line.strip())
                datas.append(x)
            except ValueError:
                continue  

    if datas: 
        return (sum(datas), statistics.mean(datas), statistics.stdev(datas))
    else:
        return None  

def main():
    for filename in sys.argv[1:]:
        result = summary(filename)
        if result:
            sum_numbers, average, stddev = result
           
            print(f"File: {filename} Sum: {sum_numbers:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")
        else:
            print(f"No valid data found in the file: {filename}")

if __name__ == "__main__":
    main()
