def word_frequencies(filename):
    words_freq = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            for word in line:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in words_freq:
                    words_freq[word] += 1
                else:
                    words_freq[word] = 1
                
    return words_freq  

def main():
    filename="src/alice.txt"
    alice = word_frequencies(filename)
    for key, item in alice.items():
        print(f"{key}\t{item}") 

if __name__ == "__main__":
    main()