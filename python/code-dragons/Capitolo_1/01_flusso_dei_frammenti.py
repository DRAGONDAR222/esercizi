'''Le porte della Biblioteca degli Specchi si spalancano: frammenti numerici orbitano instabili. Riuniscili in un unico flusso per riaccendere il foyer — concentra i frammenti pronunciando `sum_list(nums)`: deve restituire la somma degli interi in `nums`; se `nums` è vuota, ritorna `0`. Mantieni esattamente questa firma e fai in modo che i test si aprano come serrature.'''

def sum_list(nums:list[int]) -> int:
    return sum(nums) if nums else 0