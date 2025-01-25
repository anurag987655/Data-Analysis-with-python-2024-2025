

def interleave(*lists):
    interleaves=[]
    for item in zip(*lists):
        interleaves.extend(item)
        
        
    
    return interleaves

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
