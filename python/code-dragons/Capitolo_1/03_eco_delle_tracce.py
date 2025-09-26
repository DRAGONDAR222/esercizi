'''La terza navata risuona di echi ripetuti: per calmare il rimbombo, lascia parlare solo la prima voce di ogni numero. Fallo con `dedup_stable(nums)`, che crea una nuova lista con la prima occorrenza di ciascun valore mantenendo l'ordine della lista originale. Mantieni la firma e placa i test.'''

def dedup_stable(nums: list[int]) -> list[int]:

    if len(nums) == 0:
        return nums

    new_nums: list[int] = [nums[0]]

    for num in nums:
        if num  != new_nums[-1]:
            new_nums.append(num)

    return new_nums