
def bubble_sort(array:list):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

def merge(L1, L2):
    L=[]
    L=L1+L2
    L3=bubble_sort(L)
    return L3

def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10]
    l3 = merge(l1, l2)
    print(l3)
    pass

if __name__ == "__main__":
    main()
