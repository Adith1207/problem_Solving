def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x),x))
    

print(bigSorting(['23','1','2']))