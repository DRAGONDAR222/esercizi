'''Gli scribi spettrali pretendono energia scandita in segmenti regolari per il rituale. Suddividi la sequenza con `chunk(lst, size)`, spezzando `lst` in sottoliste consecutive di lunghezza `size` (l'ultimo blocco può essere più corto). Mantieni la firma e soddisfa i test.'''


def chunk(lst: list[int], size: int) -> list[list[int]]:
    my_list = []
    count = 0

    if not isinstance(lst, list) or not isinstance(size, int) or not all(isinstance(x, int) for x in lst) or len(lst) == 0 or size <= 0:
        return my_list
    
    if size >= len(lst):
        return [lst]

    while count <= len(lst) - size:
        chunk = []
        for x in range(size):
            chunk.append(lst[count + x])
        count += size
        my_list.append(chunk)

    if count < len(lst):
        chunk = [x for x in lst[count:]]
        my_list.append(chunk)

    return my_list
