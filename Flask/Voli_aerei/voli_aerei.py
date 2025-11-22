from flask import Flask, url_for, jsonify, request

dati = {
    'Nazione': {
        1: {'id': 1, 'nome': 'Italia'},
        2: {'id': 2, 'nome': 'Stati Uniti'},
        3: {'id': 3, 'nome': 'Francia'},
        4: {'id': 4, 'nome': 'Germania'},
        5: {'id': 5, 'nome': 'Spagna'}
    },

    'Citta': {
        101: {'id': 101, 'n_abitanti': 2800000, 'nome': 'Roma',   'nazione': 1},
        102: {'id': 102, 'n_abitanti': 8500000, 'nome': 'New York', 'nazione': 2},
        103: {'id': 103, 'n_abitanti': 2100000, 'nome': 'Parigi',  'nazione': 3},
        104: {'id': 104, 'n_abitanti': 1700000, 'nome': 'Milano',  'nazione': 1},
        105: {'id': 105, 'n_abitanti': 3700000, 'nome': 'Berlino','nazione': 4},
        106: {'id': 106, 'n_abitanti': 3300000, 'nome': 'Madrid', 'nazione': 5},
        107: {'id': 107, 'n_abitanti': 1300000, 'nome': 'Napoli', 'nazione': 1}
    },

    'Aereoporto': {
        201: {'id': 201, 'nome': 'Fiumicino', 'codice': 'FCO', 'citta': 101},
        202: {'id': 202, 'nome': 'JFK', 'codice': 'JFK', 'citta': 102},
        203: {'id': 203, 'nome': 'Charles de Gaulle', 'codice': 'CDG', 'citta': 103},
        204: {'id': 204, 'nome': 'Linate', 'codice': 'LIN', 'citta': 104},
        205: {'id': 205, 'nome': 'Malpensa', 'codice': 'MXP', 'citta': 104},
        206: {'id': 206, 'nome': 'Tegel', 'codice': 'TXL', 'citta': 105},
        207: {'id': 207, 'nome': 'Adolfo Suárez Madrid-Barajas', 'codice': 'MAD', 'citta': 106},
        208: {'id': 208, 'nome': 'Capodichino', 'codice': 'NAP', 'citta': 107}
    },

    'CompagniaAerea': {
        301: {'id': 301, 'fondazione': 1946, 'nome': 'Alitalia', 'citta': 101},
        302: {'id': 302, 'fondazione': 1939, 'nome': 'American Airlines', 'citta': 102},
        303: {'id': 303, 'fondazione': 1933, 'nome': 'Air France', 'citta': 103},
        304: {'id': 304, 'fondazione': 1953, 'nome': 'Lufthansa', 'citta': 105},
        305: {'id': 305, 'fondazione': 1927, 'nome': 'Iberia', 'citta': 106}
    },

    'Volo': {
        401: {'id': 401, 'durata_in_minuti': 180, 'codice': 'AZ100', 'compagniaAerea': 301, 'aeroporto_partenza': 201, 'aeroporto_arrivo': 203},
        402: {'id': 402, 'durata_in_minuti': 480, 'codice': 'AA200', 'compagniaAerea': 302, 'aeroporto_partenza': 202, 'aeroporto_arrivo': 201},
        403: {'id': 403, 'durata_in_minuti': 90,  'codice': 'AF300', 'compagniaAerea': 303, 'aeroporto_partenza': 203, 'aeroporto_arrivo': 204},
        404: {'id': 404, 'durata_in_minuti': 120, 'codice': 'LH400', 'compagniaAerea': 304, 'aeroporto_partenza': 206, 'aeroporto_arrivo': 205},
        405: {'id': 405, 'durata_in_minuti': 150, 'codice': 'IB500', 'compagniaAerea': 305, 'aeroporto_partenza': 207, 'aeroporto_arrivo': 201},
        406: {'id': 406, 'durata_in_minuti': 60,  'codice': 'AZ101', 'compagniaAerea': 301, 'aeroporto_partenza': 204, 'aeroporto_arrivo': 201},
        407: {'id': 407, 'durata_in_minuti': 450, 'codice': 'AA201', 'compagniaAerea': 302, 'aeroporto_partenza': 201, 'aeroporto_arrivo': 202},
        408: {'id': 408, 'durata_in_minuti': 100, 'codice': 'AF301', 'compagniaAerea': 303, 'aeroporto_partenza': 203, 'aeroporto_arrivo': 208},
        409: {'id': 409, 'durata_in_minuti': 130, 'codice': 'LH401', 'compagniaAerea': 304, 'aeroporto_partenza': 205, 'aeroporto_arrivo': 206},
        410: {'id': 410, 'durata_in_minuti': 160, 'codice': 'IB501', 'compagniaAerea': 305, 'aeroporto_partenza': 201, 'aeroporto_arrivo': 207}
    }
}

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return '<h3>Hello, world!<h3>'

#-----------------------------------

@app.route('/nazioni', methods=['GET'])
def get_nazioni():
    return jsonify({'nazioni': dati['Nazione'], 'totale': len(dati['Nazione'])})

@app.route('/nazioni', methods=['POST'])
def add_nazioni():

    nuovi_dati = request.get_json()

    if not nuovi_dati or 'nome' not in nuovi_dati:
        return {'errore':'campi obbligatori'}, 400
    
    nuova_nazione = {
        'nome': nuovi_dati['nome']
    }

    index = max(dati['Nazione'].keys()) + 1
    dati['Nazione'][index] = nuova_nazione
    return jsonify(nuova_nazione), 201

@app.route('/nazioni/<int:id>', methods=['GET'])
def nazione(id:int) -> str:
    return jsonify({'nazione':dati['Nazione'][id]})

#-----------------------------------

@app.route('/citta', methods=['GET'])
def get_citta():
    return jsonify({'citta': dati['Citta'], 'totale': len(dati['Citta'])})

@app.route('/citta', methods=['POST'])
def add_citta():
    nuovi_dati = request.get_json()

    if not nuovi_dati or 'nome' not in nuovi_dati or 'n_abitanti' not in nuovi_dati or 'nazione' not in nuovi_dati:
        return {'errore':'campi obbligatori'}, 400
    if nuovi_dati['nazione'] not in dati['Nazione']:
        return {'errore':'nazione non presente nel sistema'}, 404
    
    nuova_citta = {
        'n_abitanti': nuovi_dati['n_abitanti'],
        'nome': nuovi_dati['nome'],
        'nazione': nuovi_dati['nazione']
    }

    index = max(dati['Citta'].keys()) + 1
    dati['Citta'][index] = nuova_citta
    return jsonify(nuova_citta), 201

@app.route('/citta/<int:id>', methods=['GET'])
def citta(id:int) -> str:
    return jsonify({'citta':dati['Citta'][id]})

#-----------------------------------

@app.route('/aeroporti', methods=['GET'])
def get_aeroporti():
    return jsonify({'aeroporti': dati['Aereoporto'], 'totale': len(dati['Aereoporto'])})

@app.route('/aeroporti', methods=['POST'])
def add_aeroporto():
    nuovi_dati = request.get_json()

    if not nuovi_dati or 'id' not in nuovi_dati or 'nome' not in nuovi_dati or 'codice' not in nuovi_dati or 'citta' not in nuovi_dati:
        return {'errore':'campi obbligatori'}, 400
    if nuovi_dati['citta'] not in dati['Citta']:
        return {'errore':'citta non presente nel sistema'}, 404

    nuovo_aeroporto = {
        'nome': nuovi_dati['nome'],
        'codice': nuovi_dati['codice'],
        'citta': nuovi_dati['citta']
    }

    index = max(dati['Aereoporto'].keys()) + 1
    dati['Aereoporto'][index] = nuovo_aeroporto
    return jsonify(nuovo_aeroporto), 201

@app.route('/aeroporti/<int:id>', methods=['GET'])
def aeroporto(id:int) -> str:
    return jsonify({'aeroporto': dati['Aereoporto'][id]})

#-----------------------------------

@app.route('/compagnie', methods=['GET'])
def get_compagnie():
    return jsonify({'compagnie': dati['CompagniaAerea'], 'totale': len(dati['CompagniaAerea'])})

@app.route('/compagnie', methods=['POST'])
def add_compagnia():
    nuovi_dati = request.get_json()

    if not nuovi_dati or 'id' not in nuovi_dati or 'nome' not in nuovi_dati or 'fondazione' not in nuovi_dati or 'citta' not in nuovi_dati:
        return {'errore':'campi obbligatori'}, 400
    if nuovi_dati['citta'] not in dati['Citta']:
        return {'errore':'citta non presente nel sistema'}, 404
    
    nuova_compagnia = {
        'fondazione': nuovi_dati['fondazione'],
        'nome': nuovi_dati['nome'],
        'citta': nuovi_dati['citta']
    }

    index = max(dati['CompagniaAerea'].keys()) + 1
    dati['CompagniaAerea'][index] = nuova_compagnia
    return jsonify(nuova_compagnia), 201

@app.route('/compagnie/<int:id>', methods=['GET'])
def compagnia(id:int) -> str:
    return jsonify({'compagnia': dati['CompagniaAerea'][id]})


#-----------------------------------

@app.route('/voli', methods=['GET'])
def get_voli():
    return jsonify({'voli': dati['Volo'], 'totale': len(dati['Volo'])})

@app.route('/voli', methods=['POST'])
def add_volo():
    nuovi_dati = request.get_json()

    if not nuovi_dati or 'id' not in nuovi_dati or 'durata_in_minuti' not in nuovi_dati or 'codice' not in nuovi_dati or 'compagniaAerea' not in nuovi_dati or 'aeroporto_partenza' not in nuovi_dati or 'aeroporto_arrivo' not in nuovi_dati:
        return {'errore':'campi obbligatori'}, 400
    if nuovi_dati['compagniaAerea'] not in dati['CompagniaAerea']:
        return {'errore':'compagnia aerea non presente nel sistema'}, 404
    if nuovi_dati['aeroporto_partenza'] not in dati['Aereoporto']:
        return {'errore':'aeroporto di partenza non presente nel sistema'}, 404
    if nuovi_dati['aeroporto_arrivo'] not in dati['Aereoporto']:
        return {'errore':'aeroporto di arrivo non presente nel sistema'}, 404

    nuovo_volo = {
        'durata_in_minuti': nuovi_dati['durata_in_minuti'],
        'codice': nuovi_dati['codice'],
        'compagniaAerea': nuovi_dati['compagniaAerea'],
        'aeroporto_partenza': nuovi_dati['aeroporto_partenza'],
        'aeroporto_arrivo': nuovi_dati['aeroporto_arrivo']
    }

    index = max(dati['Volo'].keys()) + 1
    dati['Volo'][index] = nuovo_volo
    return jsonify(nuovo_volo), 201

@app.route('/voli/<int:id>', methods=['GET'])
def volo(id:int) -> str:
    return jsonify({'volo': dati['Volo'][id]})


app.run(debug=True)

# replica query cielo