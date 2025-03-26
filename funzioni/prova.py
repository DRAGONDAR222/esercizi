def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
 
    for elemento in elements_to_remove:
        if elemento not in original_set:
            elements_to_remove.remove(elemento)
    
    for elemento in elements_to_remove:
        if elemento in original_set:
            original_set.remove(elemento)

                                                            
    return original_set

#print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({1, 2, 3, 4}, [2, 3]))