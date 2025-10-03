'''Nello Scriptorium degli Echi ogni rotolo viene inciso e poi riascoltato: `write_and_read(lines)` deve restituire l’eco fedele degli appunti nell’ordine in cui sono stati fissati. Prima le parole vengono consegnate a un tomo chiamato `textio_write_and_read.txt`. Poi, quando il tomo viene riaperto, ogni riga emerge dal silenzio, purificata dai segni di fine riga, e va a comporre una nuova lista che custodisce la memoria del rito.'''

def write_and_read(lines: list[str]) -> list[str]:
    filename = 'textio_write_and_read.txt'
    

    with open(filename,'w') as writer:

        lines_pulite:list = [x +'\n' for x in lines  ]       

        writer.writelines(lines_pulite)
        
    
    with open(filename, 'r') as reader:

        return reader.readlines()
