'''Unione di Intervalli Sovrapposti
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.
Requisiti:
● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].
● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
○ Se l’input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com’è.'''


def merge_intervals(intervals:list[list[int]]) -> list:

    my_list:list[list[int]] = []
    count:int = 1

    for lista in intervals:

        successivo_inizio:int = intervals[count][0]
        successivo_fine:int = intervals[count][1]
        
        count += 1

        inizio:int = lista[0]
        fine:int = lista[1]

        if fine > successivo_inizio:
            my_list.append([inizio,successivo_fine])
        else:
            if count != 1 and len(my_list) > 1:
                    pass
            else:
                my_list.append([inizio,fine])
                print(my_list)

    return my_list

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15, 18]]
