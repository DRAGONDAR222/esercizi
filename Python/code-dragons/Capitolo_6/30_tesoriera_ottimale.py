'''Alla Tesoreria Ottimale, ogni tributo va minimizzato. Calcola con `min_coins(amount, coins)`: restituisci il **numero minimo** di monete per ottenere `amount`; se impossibile, torna `1_000_000_000`. Mantieni la firma e lascia che i test si aprano.'''

def min_coins(amount: int, coins: list[int]) -> int:

    if amount < 0:
        return'1_000_000_000'
    
    elif amount == 0:
        return 0

    coins_dict:dict = {}
    count_coins:int = 0

    for coin in sorted(coins,reverse = True):
        if coin < amount:
            coins_dict[coin] = amount // coin          

    while amount > 0:
        max_coin: int = min(coins_dict, key = lambda x:coins_dict[x])
        
 # tentativo non funzionante
