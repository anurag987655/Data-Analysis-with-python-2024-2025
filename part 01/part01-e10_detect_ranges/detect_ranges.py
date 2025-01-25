

def detect_ranges(L):
    l=sorted(L)
    new_list=[]
    i=0
    
    while i < len(l):
        if l[i]+1 in l:
            a=l[i]
            b=a
            while b+1 in l:
                i+=1
                b=b+1
            new_list.append((a,b+1))
        else:
            new_list.append(l[i])
        i+=1
    return new_list
                

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
