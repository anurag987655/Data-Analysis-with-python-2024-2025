#!/usr/bin/env python3

def reverse_dictionary(d):
    dic={}
    for key,item in d.items():
        if isinstance(item,list):
            for sub_item in item:
                if sub_item in dic:
                    dic[sub_item].append(key)
                else:
                    dic[sub_item]=[key]
        else:
            dic[item]=[key]
    return dic

def main():
    pass

if __name__ == "__main__":
    main()
