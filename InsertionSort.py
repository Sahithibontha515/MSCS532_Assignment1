def apply_descending_insertion_sort(elements):
    #check if the list is empty
    if len(elements) <= 1:
        return
    for i in range(1,len(elements)):
        key = elements[i]
        j = i-1
        while j >= 0 and key > elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = key