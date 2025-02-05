#!/usr/bin/env python3

import re

def file_extensions(filename):
    lst = []
    dic = {}
  
    pattern = r"(.+)\.(\w+)$"
    with open(filename, "r") as f:
         
        for line in f:
            line = line.strip()
            match = re.search(pattern, line)
            
            if match:
                full_file_name = match.group(0) 
                extension = match.group(2)
                
                if extension in dic:
                    dic[extension].append(full_file_name)
                else:
                    dic[extension] = [full_file_name]
                    
            else:
                lst.append(line)
                
    return lst, dic

def main():
    file_name = "src/filename.txt"
    no_ext, ext = file_extensions(file_name)
    print(f"{len(no_ext)} files with no extension")
    
    # Print extensions in alphabetical order
    for key in sorted(ext.keys()):
        print(f"{key} {len(ext[key])}")

if __name__ == "__main__":
    main()