

def distinct_characters(L):
    dic={}
    for word in L:
        dic[word]=len(set(word))        
    return dic

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
