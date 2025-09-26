'''Con il foyer illuminato, le colonne di vetro rivelano onde di potere: il varco si apre solo al picco giusto. Isolalo con `max_or_none(nums)`, restituendo il massimo in `nums` o `None` se è vuota. Mantieni la firma e soddisfa i test come richiesto dal rituale.'''

def max_or_none(nums:list[int]) -> int:
    return max(nums) if nums else None
