'''Nelle camere del Conclave dei Set il censimento deve essere perfetto: conta quante scintille sono davvero uniche nel cerchio. Fallo con `unique_count(nums)`, che restituisce il numero di interi distinti presenti in `nums`. Mantieni la firma e lascia che i test registrino il tuo conteggio.'''

def unique_count(nums: list[int]) -> int:

    my_list:list[int] = []

    for x in nums:
        if x not in my_list:
            my_list.append(x)

    return len(my_list)